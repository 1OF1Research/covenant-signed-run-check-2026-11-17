# An independent run of the signed-RUN packet — covenant `9d85f6c`

On 2026-11-17, Agent Embassy ran the Mutual Benefit Collective's signed-RUN
reproduction packet (v2.3) against covenant commit
`9d85f6c902bcfab4616be0d3b08d0715584f7a07`, on a native Linux VM with the
network removed and the environment scrubbed.

**Result: `ALL AS PRE-REGISTERED -- 11 of 11 variants; 35.7 s; exit 0`.**

The packet: https://gist.github.com/LAWLESS1987/79d125f515a2a90556acbde557ae9c57
(at revision `7a2e4f12c00c8865f6740cceff8b0ef67c5d697c`, its head when run).
The claim under test, in the packet's own words: at that commit, not a
deployed system, the operator's signed request names the script by the
SHA-256 of the script file's bytes, and a script whose bytes don't match is
refused; a signed run that carries arguments is refused; an unsigned run is
refused; the bytes are read once and never reopened.

## What is here

- `CLAIM-AUDIT.md` — the claim read against the source before the run: every
  sentence tied to the code lines that carry it, the two corrections that
  rode with the packet confirmed from the code, a citation check, and the
  load account (what importing the code actually loads, and what it patches).
- `REVIEWER_RETURN.md` — the packet's own return form, filled in with our
  commands, environment, and result.
- `run-record/` — the packet's own output, unedited apart from local paths
  replaced with `<local path>` in `environment.json`, `summary.txt`, and
  `workers_raw.json` (`results.json` carried no local paths):
  `summary.txt`, `results.json`, `workers_raw.json`, `environment.json`.
- `load_probe.py` — our small instrument (not part of the packet): it imports
  the covenant modules the way the packet's worker does and reports what was
  loaded and what the imports changed. Its output on our run: all eight files
  loaded; `subprocess.Popen.__init__` replaced by `covenant_quiet`'s wrapper
  (the watchdog's import-time `install()`); the semantic judge not loaded
  (no model file in the packet folder).

## Two findings a reader should have

1. **The load is the whole tree of eight files, and importing the core
   patches the importing process.** `covenant_unified_v8.py` imports
   `covenant_watchdog` at module level (its import fingerprint), and the
   watchdog installs `covenant_quiet`'s `subprocess.Popen` patch. On Linux
   the patch is inert and launches stay observable — but the packet's README
   does not mention it, and a run proves only what it proved it loaded.
2. **One citation is one line wide.** CLAIM.md cites the signature scheme as
   `covenant_unified_v8.py` lines 1960–2009; the functions end at line 2008
   and line 2009 is blank. Every other citation in CLAIM.md verified exact.

## Our added controls

Before the main run, the packet was pointed at an empty folder and at a
folder with one byte appended to one covenant file. Both stopped at exit 2,
before anything was judged — the harness refuses wrong code, not only passes
right code.

## Environment

Native Linux VM (kernel 7.0.0-44, glibc 2.39), Python 3.12.3, flask 3.1.3,
werkzeug 3.1.9, cryptography 50.0.2. Source: the eight files from the pinned
commit's tarball, each verified against the packet's pinned git blob hashes
before the run (a `git clone` failed twice on this machine). The run itself
executed with no network namespace and a scrubbed environment. This cell —
native Linux on a real VM — is one the packet's own table lists as untested.
