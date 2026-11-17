#!/usr/bin/env python3
"""Our load probe (not part of his packet): import the covenant modules the
same way the packet's worker does, then report what was actually loaded and
what state the imports left behind. Run only in the isolated environment."""
import json
import os
import subprocess
import sys

root = sys.argv[1]
src = sys.argv[2]
sys.dont_write_bytecode = True
for k in [k for k in os.environ if k.startswith("COVENANT_")]:
    del os.environ[k]
os.environ["COVENANT_TETSU_WORKSHOP"] = os.path.join(root, "unused_default_workshop")
os.environ["COVENANT_TETSU_HANDS_LEDGER"] = os.path.join(root, "unused_default_hands.jsonl")
os.environ["COVENANT_TETSU_PROPOSALS"] = os.path.join(root, "unused_default_proposals")
os.environ["COVENANT_MYCELIUM_PEERS"] = os.path.join(root, "no_allies.json")
os.environ["COVENANT_MYCELIUM_LEDGER"] = os.path.join(root, "mycelium.jsonl")
sys.path.insert(0, src)

before = subprocess.Popen.__init__
import covenant_daily_plan  # noqa: F401
import covenant_mycelium  # noqa: F401
import covenant_tetsu_hands  # noqa: F401
import covenant_unified_v8 as cov  # noqa: F401

loaded = sorted(os.path.relpath(m.__file__, src) for m in list(sys.modules.values())
                if getattr(m, "__file__", None) and os.path.abspath(m.__file__).startswith(src + os.sep))
after = subprocess.Popen.__init__
print(json.dumps({
    "loaded_from_source": loaded,
    "popen_init_before": getattr(before, "__qualname__", str(before)),
    "popen_init_after": getattr(after, "__qualname__", str(after)),
    "popen_patched_by_quiet": getattr(after, "__module__", "") == "covenant_quiet",
    "semantic_judge_model": cov.SEMANTIC_JUDGE_MODEL,
    "imports_sha12_set": bool(cov.IMPORTS_SHA12),
}, indent=1, sort_keys=True))
