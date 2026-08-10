#!/usr/bin/env python3
# [fix: rational_agents orig (results review)] 2026-08-10 — re-render already-published visualizer pages in place.
"""Refresh published episode/comparison pages against the CURRENT interlens visualizer, without their run data.

Most hubs here were exported from run directories on RunPod volumes that no longer exist, so a viz fix cannot be
picked up by re-exporting. Every page is self-contained, though: it embeds the exact ``viz-payload`` JSON the
browser reads. This inflates that payload (``viz.unslim_payload``), backfills any derived chart keys a newer
interlens expects — currently ``game.deals.pareto_ir`` and ``game.envelope_ir``, the IR-feasible frontier, traced
with ``viz.staircase`` so it is the same sweep ``GameGeometry.envelope`` runs rather than a copy — and re-renders
through the normal ``render_episode_html`` / ``render_compare_html``, so the page picks up the current JS and CSS.
The exporter-injected navigation group is lifted off the old page and put back into the new one's marker, because
that content is a property of the whole run and cannot be recovered from one page's payload. Index pages carry no
chart payload and are left untouched.

Round-trip safety was checked before the first bulk run: for a published page, ``slim_payload(unslim_payload(p))``
is byte-identical to the embedded payload, and a re-rendered page's payload equals the original once the newly
derived keys are removed. Run ``--dry-run`` first regardless — a bulk pass rewrites 1000+ files::

    python tools/rerender_pages.py --dry-run .
    python tools/rerender_pages.py five-seat-opus-five-arm-complete
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import numpy as np

from interlens.arena import viz

PAYLOAD_RE = re.compile(r'<script type="application/json" id="viz-payload">(.*?)</script>', re.S)
NAV_RE = re.compile(r"<span class='navgrp'>.*?</span></span>", re.S)


def backfill(game: dict) -> bool:
    """Add ``deals.pareto_ir`` and ``envelope_ir`` to one game payload. True if anything changed."""
    d = game.get("deals")
    if not isinstance(d, dict) or "pareto" not in d or "ir" not in d:
        return False
    if "pareto_ir" in d and "envelope_ir" in game:
        return False
    reachable = np.array(d["pareto"], dtype=bool) & np.array(d["ir"], dtype=bool)
    d["pareto_ir"] = [int(v) for v in reachable]
    game["envelope_ir"] = viz.staircase(d["wx"], d["wy"], reachable)
    return True


def games_of(payload: dict):
    """Every game payload on a page: one on an episode page, one per side on a comparison page."""
    for side in ("left", "right"):
        node = payload.get(side)
        if isinstance(node, dict) and isinstance(node.get("game"), dict):
            yield node["game"]
    if isinstance(payload.get("game"), dict):
        yield payload["game"]


def rerender(path: Path, *, dry_run: bool) -> str:
    html = path.read_text()
    m = PAYLOAD_RE.search(html)
    if not m:
        return "skipped (no chart payload)"
    payload = viz.unslim_payload(json.loads(m.group(1)))     # pages embed the wire form; the renderers want views
    changed = [backfill(g) for g in games_of(payload)]
    if not changed:
        return "skipped (payload carries no game)"
    render = viz.render_compare_html if "left" in payload and "right" in payload else viz.render_episode_html
    out = render(payload)
    nav = NAV_RE.search(html)
    if nav:
        if viz.NAV_MARKER not in out:
            return "FAILED (nowhere to put the run navigation this page already had)"
        out = viz.inject_nav(out, nav.group(0))
    suffix = "" if any(changed) else " (payload was already current)"
    if dry_run:
        return f"would render{suffix}"
    path.write_text(out)
    return f"rendered{suffix}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("roots", nargs="+", type=Path,
                    help="Directories to walk (every *.html beneath each) and/or individual .html files.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Report what would happen without writing — use to check a hub before touching 300+ files.")
    args = ap.parse_args()
    files = sorted({p for root in args.roots for p in ([root] if root.is_file() else root.rglob("*.html"))})
    counts: Counter[str] = Counter()
    for p in files:
        try:
            status = rerender(p, dry_run=args.dry_run)
        except Exception as exc:                                  # a malformed page must not stop the batch
            status = f"FAILED: {type(exc).__name__}: {exc}"
        if status.startswith("FAILED"):
            print(f"  {p}: {status}", file=sys.stderr)
        counts[status] += 1
    for status, n in sorted(counts.items()):
        print(f"{n:6d}  {status}")
    return 1 if any(s.startswith("FAILED") for s in counts) else 0


if __name__ == "__main__":
    raise SystemExit(main())
