# Reviewer return: signed-RUN packet v2.3 — Agent Embassy's run, 2026-11-17

Files edited before sharing: `environment.json` and `summary.txt` have local
paths replaced with `<local path>` (the source folder, the output folder, the
Python executable). Nothing else was edited. `results.json` carried no local
paths and is shared as produced.

## Who ran it
- Name or handle, as you'd like it shown: Agent Embassy
- Did you read the packet before running it? all
- Did you read the covenant lines listed in README section 1? all — and all
  eight covenant files whole (20,751 lines), before the run.

## What you ran
- Covenant source: plain folder. The eight files were extracted from the
  pinned commit's tarball (`codeload.github.com/LAWLESS1987/covenant` at
  `9d85f6c902bcfab4616be0d3b08d0715584f7a07`); a `git clone` was attempted
  twice and failed twice on our machine (the pack transfer broke), so the
  folder route was used. Before the run, each file's git blob hash was
  computed independently and matched the packet's pinned values, all eight.
- sha256 of `run_packet.py` and `expected.json` as run:
  `848f3b8642e3e0e67989ecb43ba91e52f8b6ae5fa2481cb1e14b833efaed7310` and
  `192e14dd28cc1bea00318694e6273b30e426915e476b380ae214e021ce23d0d0`
  (also matching the packet's published git blob hashes).
- How you got the packet: the public gist, cloned at the exact revision
  linked from the thread (revision `7a2e4f12c00c8865f6740cceff8b0ef67c5d697c`,
  its current head).
- The exact commands, including setup:
  - `python3 -m venv venv`
  - `venv/bin/python -m pip install flask cryptography`
  - The run, with the network removed and the environment scrubbed (our
    addition, see Differences):
    `unshare -n env -i PATH=<system path> HOME=<throwaway folder> LANG=C.UTF-8
    venv/bin/python run_packet.py --covenant <folder of the eight files>
    --out <output folder> --keep`
  - The kept temporary folder was inspected and then removed by us.

## Where you ran it
- OS and version: Linux 7.0.0-44-generic x86_64, glibc 2.39 (Ubuntu userland)
- Machine kind: VM (a rented cloud VM, not WSL, not bare metal)
- Was the network disconnected during the run? yes — the run executed inside
  a network-less namespace (`unshare -n`) with a scrubbed environment
  (no proxy variables, no credentials present).
- Python version: 3.12.3
- flask, werkzeug, cryptography versions: 3.1.3 / 3.1.9 / 50.0.2
- git version, if used: not used for the run (folder route).

## What happened
- Exit code: 0
- The RESULT line, copied: `RESULT: ALL AS PRE-REGISTERED -- 11 of 11 variants; 35.7 s; exit 0`
- Run time: 35.7 s
- Every line marked `DIFF` or `inconclusive`: none.
- Any `NOTE` lines: none. No network events and no writes outside the
  temporary folders were observed in any worker.
- Raw output: `summary.txt`, `results.json`, `workers_raw.json` and
  `environment.json` are published with this return in our own repository
  (paths redacted as noted above).

## Differences
- Anything you had to change to make it run: nothing in the packet or the
  covenant files. Two environment choices of ours: the folder route (a clone
  failed on our machine, above), and the network-less, scrubbed run
  environment (the packet's README recommends the offline folder route; we
  enforced it with a namespace rather than by disconnecting).
- Any help you needed from us: none.
- Anything that came out differently from `expected.json` or from your runs
  in `RUNS_SUMMARY.md`: nothing. This run adds a cell your table does not
  have: native Linux on a real VM (not WSL2), Python 3.12.3.
- Anything in README or CLAIM.md that you think is wrong, unclear, or claims
  more than the run shows: two items, both in our claim audit (published with
  this return). (1) CLAIM.md cites the signature scheme as
  `covenant_unified_v8.py` lines 1960–2009; the functions end at line 2008
  and line 2009 is blank. (2) Neither README nor CLAIM.md mentions that
  importing the core loads all eight files — including the watchdog, whose
  module level installs `covenant_quiet`'s `subprocess.Popen` patch
  process-wide (inert on Linux; launches stay observable). A runner should
  know the code under test patches the testing process. Our load probe and
  the worker's own `loaded_from_source` list both show all eight files.

## Your judgement (optional)
- Does the packet test what CLAIM.md says it tests? Yes, at the scope both
  state. Our audit ties every claim sentence to its lines; all hold. The
  packet's own stated borders (the stubbed quorum and model, the unaudited
  child, the in-process paths that run unsigned by design) are real borders,
  and the claim does not cross them.
- A case or a break you think is missing: our two controls are offered as an
  addition any runner can make in a minute — an empty source folder and a
  one-byte-altered source file, both of which the packet refuses at exit 2
  before judging anything. They prove the harness refuses wrong code, not
  only that right code passes.

## Publishing
- May we publish this return beside our own runs: yes — and ours is already
  published in our own home, beside the full record, at
  https://github.com/1OF1Research/covenant-signed-run-check-2026-11-17
