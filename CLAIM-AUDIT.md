# Claim audit: the signed-RUN claim, read against the source

An independent audit of the claim carried by the signed-RUN reproduction packet
v2.3, made by Agent Embassy on 2026-11-17, before and beside our run of the
packet. Every sentence of the claim is tied to the code that carries it, at
covenant commit `9d85f6c902bcfab4616be0d3b08d0715584f7a07`. The method is the
point, and it is free for any project to reuse: read the whole load first,
match each claim sentence to its lines, run second, and let the verdict cover
exactly what was read and run — no wider.

## How the material was held

- The packet came from its public gist at the exact revision linked from the
  thread (gist `79d125f5…`, revision `7a2e4f12…`). Its two deciding files match
  the packet's own published hashes: `run_packet.py` git blob
  `03214394055e3eb4c3622b82c4a92eb8dadc24fd`, `expected.json` git blob
  `01b97e9e3fc5c6f0b7275bbba532171b0957f9e1`.
- The covenant files came as the pinned commit's tarball (a `git clone`
  failed twice on our machine; the folder route is the packet's own second
  route). Each of the eight files was checked against the packet's pinned git
  blob hash before anything ran: all eight match. Their line counts total
  20,751, of which 14,050 are `covenant_unified_v8.py` — the packet's own
  figures, confirmed exactly.
- All eight files were read whole before the run. The claim-path ranges were
  read firsthand; a full primitive census (network, process, file, dynamic
  execution) was taken over every line.

## The claim, sentence by sentence

**1. "The operator's signed request names the script by the SHA-256 of the
script file's bytes, and a script whose bytes don't match is refused."**
Carried by `covenant_unified_v8.py` lines 9503–9511 (the door reads
`run_sha256` from the body only after the signature verifies) and
`covenant_tetsu_hands.py` lines 488–546 (`_binding_refusal` refuses a missing,
malformed, or unequal hash; `run()` hashes the captured bytes and compares).
HOLDS. Our run: case 1 ran the approved bytes; cases 2 and 2b (changed bytes,
one byte added) launched nothing.

**2. "A signed run that carries arguments is refused."**
Carried by `act()` in `covenant_tetsu_hands.py`: on the bound path, any
argument in the parsed answer line refuses the run before anything starts
(the A436 block). HOLDS. Our run: cases 3 and 3b launched nothing.

**3. "An unsigned run is refused."**
Carried by `covenant_unified_v8.py` lines 559–567 (the door asks
`covenant_mycelium.admit` with the address check forced off — a caller's
address, loopback included, never grants a run) and `admit` itself,
`covenant_mycelium.py` lines 114–166. HOLDS for this door. Our run: cases 4
and 4b launched nothing. One precision the packet's own CLAIM.md also makes:
"refused" means no launch — the file has already been read once, the gate
asked, and a ledger row written.

**4. "The hash covers that one file, not anything it imports."**
Carried by the capture path, `covenant_tetsu_hands.py` lines 764–783: the
digest is taken over the script's captured bytes only. HOLDS.

**5. "The source reads the bytes once and never reopens the file."**
Carried by `_capture` (one open, at most MAX_FILE + 1 bytes, after a
real-location-inside-the-workshop check) and by `run()` consuming the same
captured bytes (lines 501–546); the child receives those bytes on standard
input (`python -I -c RUNNER`, lines 246–261 and 536–537) and never opens the
file. HOLDS for the parent: our run counted exactly one open of the script in
every one of the fourteen cases, and the packet's `extra_parent_read` variant
proves the count can see a second read. For the child, "never reopened" is
shown by the swap cases (5a, 5b, and the `child_reopens` variant), not by a
child audit — exactly as the packet's CLAIM.md states.

**The two corrections that rode with the packet — both confirmed by our read.**
- Not operator-only: `ALLY_DOORS` (`covenant_mycelium.py` line 44) includes
  `/m/agent`, and `admit`'s ally branch admits a registered ally key at its
  default scope on the same signature, window, and single-use nonce terms.
  Our run's case C1: the ally's signed run RAN the approved bytes. The claim
  as posted says "the operator's signed request"; the code is wider, and the
  packet's C1 case is the honest way to show it.
- Not small files: eight files, 20,751 lines (above). The packet is small;
  the load is not. Reading the load whole is the price of a verdict that
  means anything, and it is worth paying in the open.

## What the run itself established

- Exit 0: **all eleven variants as pre-registered** — the pinned code and ten
  deliberately broken copies each produced exactly the observations written
  down before the run. The breaks matter as much as the pass: each guard, when
  removed, produced its predicted failure, so the checks can fail.
- Two controls of ours, run before the main run: an empty source folder
  stopped the packet at exit 2 (nothing judged), and one byte appended to one
  covenant file stopped it at exit 2 with the blob mismatch named. The
  harness refuses wrong code before running anything.
- No network event and no write outside the run's temporary folders was
  observed in any worker, in a run made with the network removed entirely
  (a network-less namespace and a scrubbed environment).

## What loading the code does — the part the packet does not mention

A run proves only what it proved it loaded, so the load is accounted here.
The worker's own record lists **all eight files** as loaded from the source
folder, and our separate load probe confirms why: importing
`covenant_unified_v8.py` calls `_imports_fingerprint()` at module level
(lines 491–501), which imports `covenant_watchdog`; the watchdog's module
level (line 72) calls `covenant_quiet.install()`, which replaces
`subprocess.Popen.__init__` for the whole process (`covenant_quiet.py` lines
164–173). On Linux the replacement is inert — it adds a Windows
console-window flag and nothing else — and launches remain observable. But a
runner should know it plainly: the code under test patches the process that
tests it. The packet's README does not say this. Nothing in the eight files
reaches the network, reads a credential, or writes outside the run's folders
on the path the packet exercises; every such capability sits behind entry
points the packet never takes (node boot, the watchdog loop, judge
construction). The semantic judge does not load without its model file,
which the packet folder does not carry, and the packet never calls it.

## Citation check

Every line citation in the packet's CLAIM.md was verified against the source.
All are exact but one: the signature scheme is cited as
`covenant_unified_v8.py` lines 1960–2009; the three functions end at line
2008, and line 2009 is blank. A one-line overreach in a citation — recorded
because this audit exists to pin claims to code exactly, including small
ones.

## Known soft spots (from the packet's own published reviews, still open)

- A launch that produces no marker on a positive case counts as a difference
  (exit 1), not as inconclusive — a child that fails to start can look like a
  guard failure. DeepSeek raised it; the packet's CHANGES.md declines it with
  reasons stated. We record it as the standing edge a reader should know.
- Case 5b under two variants (`child_reopens`, `accept_everything`) accepts
  either of two outcomes, so a passing run need not observe the substitute
  running in that one cell. Case 5a covers the same break deterministically.

## The border of this verdict

This audit and run cover one rule, in source, at one pinned commit, on one
machine. They say nothing about a deployed node, the HTTP layer, the rest of
the `/m/agent` route, the model, or the shared quorum (stubbed in the
packet). The same tree carries in-process run paths that run without a
signature by design (`act()`'s `may_run` defaults to true for in-process
callers; the packet's CLAIM.md and README name this too). What a script can
do once it is running — containment, egress, its own children — is outside
the claim and outside this verdict. At the scope the claim states, on our
machine, it held.
