# Tuner integration evidence

## Identity and qualification boundary

- Production proposal: `tuner`, `0.1.0-experimental`, under `sdk/octabam/modules/tuner` on `tuner-0.1-promotion`.
- Preserved refreshed draft on `tuner-0.1`: `5a56f1f8d4c1c426c07195c26e552c677a8c44ac`. The location change does not establish publication qualification.
- Current author source: `timhastie/octatrick-modules` v2.20, commit `fd18f5530989be348e6aa4c6e38f93beba555e6d`; all four upstream files, including the stock-guard reader, are copied unchanged.
- Current documentation/draft base: Modwerk `4e2226f1be6347f74d51a0d5b99ee572ba3a82bb`.
- Preserved native candidate build baseline: `916ce01bbfc60f3aedd7156066354fedb521e6f4`, private `relay-tuner` facade, Tuner only, stock FX and static stock DSP; no USB base.
- The delivered BIN/bus have **not** been rebuilt from this v2.20 source, current main, the hash-guard wrapper, or the new draft/promotion commit. They are historical candidate evidence, not exact-current-commit qualification.

The wrapper now preserves the upstream runtime/source declarations while replacing its three detour expectations with verified Modwerk-form guards. [guard-provenance.json](evidence/guard-provenance.json) records the adapter change. It is not a rebuilt-image result. No hardware, resource, timing or publication qualification object is fabricated.

## Immutable source pin after the tag update

The integration intentionally retains immutable upstream commit `fd18f5530989be348e6aa4c6e38f93beba555e6d`. ORDER-069 records that the movable v2.20 tag subsequently points to `9b62d5d` (tag object `609b4a92`), a synth README-only change with identical `tuner/` content. The lead will repin all three PRs to the final tag at submission. This note does not change the vendored files or import pin.

The canonical OCTAMOD79 artifact was built from promotion commit `ab3db4f570f1ad869686ad20d03fd227bb97de22`; a later documentation-only commit is not the artifact's built source. No build, test or runtime is rerun for this note.

## Source update, not a test result

The v2.20 source copy is recorded in [source-revendor.json](evidence/source-revendor.json). No build, manifest import, test, generator or runtime was run during this update. The immutable upstream reader requires `out/raw/section_3_MAIN_OS.bin` relative to the build working directory when its manifest is imported. The wrapper preserves Modwerk-form digest guards.

Source inspection of `sdk/tests/test_requested_imports.py:39–55` shows that the named lazy-fingerprint check only parses paths listed in the separate `octabam-363861e.json` import record, which does not select Tuner. No predicted two-argument rejection by that named check is claimed; no test was executed. This does not establish that other no-firmware manifest-import paths accept the new eager upstream reader.

All build, compatibility, USB-source and capture records below remain historical. In particular, the seven PNGs belong to the v2.19/card-sdk image with bus hash `91bf159e…`, not this source update.

## Observed outcomes

| Item | Observed result and limit |
| --- | --- |
| Private native candidate build | Passed once, exit 0; not canonical Docker or browser parity evidence. |
| Private declaration compatibility | Passed once on the earlier activation fixture; not runtime companion proof. |
| Original retained-emulator candidate capture | Signal 11 before panel input, no screenshots. Host crash localized to a DSP memory-write callback; triggering image property unresolved. |
| No-Tuner control A | Build and seven-image capture passed using the retained emulator. It omits the Tuner hooks and the additional native DRAM platform path. |
| Private diagnostic emulator | Same candidate reached ready and exited cleanly; separately sourced tooling did not reproduce the original fault. |
| Candidate capture with substituted tooling | Seven images captured and visually reviewed; window navigation observed. No live pitch, audio or needle-response qualification. |
| Standalone 2.19 reference | Exited 1 before UI commands; zero screenshots, no paired comparison. Cause unresolved. |
| Earlier draft check | Overall exit 1 in application tests; not a successful readiness gate. |
| Earlier promotion/catalogue run | The prior 7b33f608 promotion failed its one catalogue attempt because qualification was missing. No catalogue run has been made for this v2.20 update. |

## Preserved native build

One private build ran on 25 October 2026 with `make image REMIX=relay-tuner BUILD=1 VERSION=MWTUN0.1`. It exited 0 in 7.748408 seconds. Evidence: [native-build.json](evidence/native-build.json) and the retained private `relay-062/CARD_NATIVE_ATTEMPT.json` receipt. This evidence is unchanged by this documentation update.

| Artifact | Bytes | Whole-file SHA-256 |
| --- | ---: | --- |
| `mainos_bus.bin` | 1114801 | `91bf159ee5a25c1d6b9356fe3eb0f43d8985f569bbfdeee3a7f85ba0da3770b3` |
| `OCTATRACK_MWTUN0.1.bin` | 448024 | `beb2628bb981fed62f1113a69ae331deb27d649ac5ddd5e2c6471efc6889bed2` |
| `OCTATRACK_OS1.40C_MWTUN0.1.syx` | 625821 | `207c57d7eb0bac1fb42a3350c3261f7ff3cb6e5bc9491c5a065d9ce1c795196a` |

Private artifacts remain in `relay-062/card-sdk/out/`; they are not committed. This was a native SDK build, not canonical Docker proof, a USB-base image, browser parity or an exact build of the rebased draft.

## Declaration compatibility

The single `npm run modules:compat -- tuner --json` attempt used a disposable copy of earlier main `916ce01b`, with Tuner activated only in its private catalogue. It returned exit 0, `notActive: []`, 28 active IDs, 378 pair contexts, 72 base events and zero Tuner problems. The six-byte Tuner frame claim ends where the adjacent base claim begins. [declaration-compatibility.json](evidence/declaration-compatibility.json) retains the evidence.

This establishes declaration checks in that fixture, not current-main hardware behavior, runtime safety or module publication. No additional compatibility attempt is claimed.

## Capture provenance and observations

The original capture used emulator SHA-256 `07a7c08e3d4562f7b51ee5985bd2595cced383f1b8090995f1dfecfb404f092d` and failed with signal 11 before any panel command. [ui-startup.json](evidence/ui-startup.json) preserves that result. Existing macOS crash evidence identifies the host DSP write callback, not a guest Tuner or loader PC. The exact triggering image property remains unresolved; no Tuner firmware fix was made.

The 26 October capture used a separate source-built emulator from revision `5581c68532f55c4325445c9e49c332e9c8e765c2`, binary SHA-256 `7ab0cc133ce493fc6f4f0e3b39bdac3ccc496f0946adc2a7edb1188417129621`, with numeric-only fault diagnostics. This is an explicit tooling substitution. Equivalence to the retained emulator is not established.

The candidate attempt ran from 01:43:40.496737 to 01:44:41.467114 UTC, exited 0 and saved seven PNGs. The MKII panel, stopped transport, main output off, 150 ms key interval and fresh 32 MiB scratch card are recorded in the unmodified [capture.json](media/capture.json). All seven images were reviewed:

| Capture | Visible observation |
| --- | --- |
| 01 | Unobstructed track source-parameter page. |
| 02 | Tuner overlay and pitch ruler visible; pitch readout unpopulated. |
| 03 / 04 / 05 | Tuner absent and track page restored after the planned NO / YES / TEMPO routes. |
| 06 | Ordinary tempo popup visible. |
| 07 | Ordinary tempo-tapping dialog visible. |

No audio was played or recorded. A ruler/center mark is not proof of a moving needle or measured pitch. Track following, signal threshold behavior, pitch accuracy, audio continuity and the toggle-off gesture remain hardware items.

The same tooling launched the standalone 2.19 bus (`2db6a88885f39250ba2b8eb2727ba8937d351948abc1a80eca0c0b5ea84246af`) once. It exited 1 before UI commands and produced no screenshots. No paired visual equivalence is available and no retry occurred. Both attempts ran serially with fresh Tim-session waits; their own emulators were reaped, owned leases released and scratch cards removed. [ui-capture-2026-10-26.json](evidence/ui-capture-2026-10-26.json) records this boundary.

## Earlier draft check

The retained `npm run check -- --base origin/main` attempt on 25 October ended with exit 1 after 182.482477 seconds. The receipt records two failed application test files, 325 passed files, two failed tests, 2,598 passed tests and two skipped tests. The named failures include the firmware API tests; their safe diagnostics are retained in `relay-062/draft-check/full-check.json`. Earlier metadata and compatibility phases passing does not turn the overall check into a readiness pass. No rerun or current-rebased-check result is asserted here.

## Card-only delivery and future USB work

Card builds only: the base has no removal refusal for ordinary modules. Tim accepted card-only delivery; USB support is optional and is not a blocker for this draft. The earlier [USB admission proposal](evidence/usb-admission.md) remains a later design idea, not an implemented runtime feature or required test plan.

The open window/input layer retains callbacks into module memory. No safe hot-removal result, USB package, installation, Keep/Undo, replacement or persistence result is claimed. The source adds no tuner setting to a Part, project or battery RAM; that does not establish general USB module-set persistence.

## Qualification still required

Untested on physical MKI or MKII hardware for this integration. Current code/data/padding, loader overhead, maximum stack, frame-copy cost, UI detector cost and worst-case load are unmeasured. Historical upstream results are not substituted for current qualification.

Before exact-current-source qualification, build and identify the final source commit and artifact, then collect the actual device/model, test configuration and observed results. The hardware sheet covers UP-first entry, a known 440 Hz tone through the selected THRU track, note/octave/cents/needle response, all closure routes and ordinary tempo gestures. The real catalogue-generation diagnostics must be mapped to those collection items or the necessary software build/evidence work; this document does not pre-fill them as passes or waivers.

## ORDER073 local-check checkpoint — 26 October 2026

**PARTIAL.** These results checked source `87f2be3c04bb232ee3ed3fa935b4b61a98177739` before this documentation appendix. [local-checks-order-073.json](evidence/local-checks-order-073.json) records each completed leaf, its full receipt identity and source pin. Historical evidence above is unchanged.

| Leaf | Result | Boundary |
| --- | --- | --- |
| D01 Docker source packages | FAIL | ours; exit 125; owned container absent |
| L03 Module catalogue qualification | FAIL | qualification; exit 1 |
| L06 Compatibility pairs | PASS | exit 0 |
| L07 Changelog | FAIL | ours; missing prepared input, exit 1 |
| L14 Vitest | NOT_RUN | Pending setup decision |
| L16 Bundle | NOT_RUN | Pending setup decision |

The pair table was generated once successfully and committed as `87f2be3c04bb232ee3ed3fa935b4b61a98177739`; L06 then passed. L03 still fails publication qualification. L07 remains **ours**, because ignored preparation inputs are missing; it is not a qualification-only refusal.

Both D01 failures are ours; the owned processes were reaped, stream drains completed and container cleanup recorded absence. No successful source-package build is claimed.

The private dependency copies omitted ignored prepared catalogue/changelog inputs and `public/module-media`. The first draft media generation failed once with exit 1 before any media was produced; its exact error was not retained. Source review found that generation lacked an approved base reference, and local `origin/main` metadata has since been restored to `4e2226f1be6347f74d51a0d5b99ee572ba3a82bb` without contacting a remote. That correction does not turn the failed attempt into a pass. The media/setup decision remains unresolved, so L14 and L16 are **NOT_RUN**.

Canonical firmware is unchanged. No USB lifecycle change, emulator session, physical-device test, hardware qualification, cycle measurement or memory-bound measurement is claimed by this checkpoint.

## ORDER074 local-check outcomes — 26 October 2026

**PARTIAL.** Normal preparation passed. The one corrected D01 source-package build passed at `be883d845d36dba7d7bbf77f35a996c5fd3a2107`, and the development importer passed. The imported source/package identities were committed as `4d6b96025e756ca9ce941425c1f8aa30827af7c3`; this is not a new canonical firmware build or Tuner publication qualification.

| Check | Recorded outcome and source |
| --- | --- |
| L07 changelog | FAIL at `be883d845d36dba7d7bbf77f35a996c5fd3a2107`; Tuner's existing notes are outside the generated qualified catalogue |
| L14 Vitest | FAIL at `4d6b96025e756ca9ce941425c1f8aa30827af7c3`; 2,588 passed, 14 failed out of 2,602 |
| L16 bundle | PASS at `4d6b96025e756ca9ce941425c1f8aa30827af7c3` |
| Prior L03 | Qualification FAIL retained from ORDER073; not rerun |

The 14 failed assertions occur in seven file records. Source-based classification identifies **13 qualification/build-readiness dependencies, one ours, and zero owner-only**; the reporter's 13 failed suite nodes are not 13 files. Qualified generated catalogue data has 31 entries while the SDK catalogue lists 32 including Tuner. Tuner remains `build.pending` and correctly absent from compiled module versions, although its authored inputs are covered by the complete source fingerprint. A successful package import or hardware evidence alone does not establish browser build readiness or resolve that mismatch.

The independent failure that is ours is the Analog BD proof's stale `moduleSourceTreeSha256` binding against the newly imported package source-tree identity. It is not merely a source-commit mismatch. The proof has not been regenerated, edited or retagged; its failing assertion is preserved. L07's newly retained category is catalogue/qualification-dependent, unlike the earlier ORDER073 missing-preparation failure, which remains historical.

The setup used 251 unchanged published assets copied from the successful draft media generation after catalogue and corresponding input equivalence. Tuner was excluded. No generated qualification catalogue or waiver was changed. The earlier failed generation and D01 receipts remain preserved; the corrected attempts do not erase them.

Both branches remain based on main `4e2226f1be6347f74d51a0d5b99ee572ba3a82bb`, not newer main `814f6c556e6d518ba7cac77ac3cecc9f15cadf68`. [local-checks-order-074.json](evidence/local-checks-order-074.json) contains the per-leaf source pins, full receipt hashes, import binding and assertion-by-assertion analysis. This later documentation was not part of the checked commits. Canonical firmware and the runtime USB mechanism are unchanged. No new hardware, cycle, complete-memory or runtime qualification is claimed.

## Emulator qualification — 29 October 2026

**Emulator evidence for the qualification record; hardware untested.** Numbers and identities: [qualification-emulator-2026-10-29.json](evidence/qualification-emulator-2026-10-29.json). The record itself waits in [qualification.example.json](qualification.example.json) (complete except `hardware`) until Tim's report on the exact card image exists; `tests.qualification` is not set and `tests.hardwareStatus` stays `untested`.

### What ran

| Item | Identity |
| --- | --- |
| Image | canonical card `OCTATRACK_MWTUN0.1.bin` (448,024 B, `b87ab778…`), whose MAIN OS is the bus `91bf159e…` that ran; built from promotion `ab3db4f5`, upstream Tuner `fd18f553` (the `tuner/` files are identical in v2.21) |
| Unit check | the Tuner's 2,830 B of code in emulated RAM compared equal to `runtime.elf` `.text` (`492f1b52…`) before any measurement |
| Emulator | `ot_emu` `c81d13dc…` (source build 27 Oct), `--dsp --frame --mkii`, unsandboxed, one rig slot |
| Fixture | `tuner-load8` card (`90bef7e1…`): T1–T7 FLEX playing a sample with stock FX1 and FX2 on every track, trigs and retrigs on every track at 120 BPM; T8 THRU on input A |
| Signal | `--audio-in` WAV, the same 0.5 FS signal on the four input slots, scheduled: 440, 82.41, 445, 110 Hz sines, white noise, silence, 440 Hz again. No firmware, memory or code was changed: the tone reaches the tap through the stock input, the THRU machine, the track's effects and the read-back DMA |

### The tap

`tu_frame` (upstream `tuner.s` lines 97–127) runs at frame_isr's tail (`0x4000d99a`) on every 16-sample block while the window is open. It reads `0x80003190 + bank × 1024 + track × 128`, with the bank from `0x800000e4` and the track from `0x80000000 & 7`: sixteen L/R pairs of 32-bit left-justified words, the selected track after its effects and before its fader. It writes `(L >> 1) + (R >> 1)`, top 16 bits, into a 4,096-sample ring. `tu_tick` (UI task loop head `0x40056c72`) analyses the ring and redraws every 400 blocks.

The emulator fills this arena. The earlier attempts' zero peak was a fixture level: at the 0.1 FS built-in tones T8 THRU reaches about 26 at the tap (gate 64), and T1 of this fixture is silent at the tap after its effects. At 0.5 FS, T8 reaches 100–184.

### Readings (LCD and RAM agree; five readings 0.4 s apart unless noted)

| Input on T8 | Expected | Read | State |
| --- | --- | --- | --- |
| 440 Hz | A4 +0.0c | A4 +0c 440.0Hz ×5 (and ×3 at the end) | live |
| 82.41 Hz | E2 +0.1c | E2 +0c 82.4Hz ×5 | live |
| 445 Hz | A4 +19.6c | A4 +19c 445.0Hz ×5 | live |
| 110 Hz | A2 +0.0c | A2 −1c 109.9Hz ×3 | live |
| white noise | no pitch | first reading A2 +43c 112.7Hz (ring half tone, half noise), then HOLD | HOLD |
| silence | HOLD | HOLD (ring peak 15, under the gate) | HOLD |

The 445 Hz and 110 Hz readings sit one cent low: the cents come from a 12-bit ratio table (0.42 cents per step), as the upstream README says. Captures: `media/08-tuner-a4-440.png`, `media/09-tuner-e2-82.png`, `media/10-tuner-a4-445.png`.

T2 of the fixture (FLEX with EQ and CHORUS) carries a DC offset at the tap: ring mean 1,912, swing ±1,062, so the normalised difference never goes negative and every analysis ends in HOLD. The detector removes no DC. See *Open* below.

### Cost (instruction-count model)

The emulator counts executed ColdFire instructions; PC watches on the Tuner's entries and exits and on the stock frame-interrupt body (`0x4000aad8`–`0x4000d9a6`) give per-call counts. Converted with the toolkit's calibration, the FM Synth record's model: **9.44 ns per instruction at 264 MHz = 2.49216 cycles per instruction**; one block is 16 samples at 44.1 kHz = 362.8 µs = **95,779 cycles**; Modwerk's ColdFire module allowance is 10 % of it, **9,577 cycles per block**. This is not chip timing and not opcode cycles.

| Path | Window | Instructions | Where |
| --- | --- | ---: | --- |
| `tu_frame` (frame interrupt, every block) | open | 195 (min = max over 60,708 blocks) | — |
| `tu_frame` | closed | 4 | — |
| `tu_tick` not due (UI loop head, ~108 visits/s) | open / closed | 7 / 4 | — |
| analysis + redraw (UI task, every 400 blocks) | open, pitched tone | mean 998,000–1,000,500, **max 1,008,258** | 440 Hz under load |
| analysis + redraw | open, noise (clarity reject) | max 935,298 | |
| analysis + redraw | open, silence (gate reject) | max 56,115 | |
| `tu_analyse` alone | open, pitched | max 1,002,725 | |
| `tu_draw` alone | open | 5,418–5,863 | |
| open (UP + TEMPO to the first draw, key task) | event | 13,749 | |
| close (TEMPO, `tu_close`) | event | 5,968 | |

UI-task counts exclude the frame-interrupt bodies that preempt them; any other interrupt inside the span stays in the count, so they are upper bounds. The counts depend on the signal, not on the load: open with the transport stopped (only T8's input) gives the same 195 and max 1,005,617.

**Per block, worst case (window open, pitched tone, fixture playing):** 195 + 1,008,258 / 400 + 7 × 108 / 2,756 = **2,716 instructions = 6,769 cycles per block, 71 % of the 9,577 allowance.** The frame interrupt itself carries 195 instructions = 486 cycles (5.1 %); the rest is UI-task work, 9.5 ms every 145 ms (6.6 % of the core), which the frame interrupt preempts. Window closed: 4 + 4 × 108 / 2,756 instructions = 10 cycles per block.

The whole frame-interrupt body under the fixture: closed mean 25,158, max 40,890; open mean 25,410, max 41,219 instructions. The fixture's own peak is above the 38,432 instruction-times of a block at 9.44 ns (it fits at 8.38 ns, 43,294) with or without the Tuner; the Tuner adds its 195.

### Memory (exact)

From `runtime.elf`, `layout.json` and the appended bytes of the canonical build:

| Region | Space | Bytes |
| --- | --- | ---: |
| Tuner code and tables (`.text` `0x40a955e0`–`0x40a960ee`) | sdram | 2,830 |
| State 44, ring 8,192, snapshot 8,192, decimated 2,048, NSDF 740, lobes 256, YIN 28 (`.data` `0x40a980f0`–`0x40a9cd1c`) | sdram | 19,500 |
| Unused gap the link leaves between `.text` and `.data` | sdram | 8,194 |
| Platform loader (232) and packed unit (2,009) appended to the image | cpu-flash | 2,241 |
| Three hook sites rewritten in place (3 × 6 B) | cpu-flash | 18 |
| UI-task stack below the loop head, measured peak | sdram | 236 |
| DRAM platform reserve (Flex sample RAM given up, `0x40a955e0`–`0x41495de0`, 10,487,808 B) less the unit span | sdram | 10,457,284 |

The Tuner's own bytes: 33,019; with the reserve 10,490,303. One global instance; no heap, no SRAM, battery RAM or DSP memory; the window object is the stock TEMPO window's (class 5), created by the stock routine.

Stack: `tu_frame` uses registers only (0 B; it runs on whatever stack the frame interrupt has). In the UI task the deepest write inside `tu_draw` (writes trace filtered to the UI task, interrupt chains excluded) is 236 B below the loop-head SP `0x460d59a8`: the Tuner's own frames are 172 B (`tu_tick` 44, return 4, `tu_draw` 92, helper return 4, 24 B of text arguments, call 4), the stock text routine adds 64. `tu_analyse` pushes nothing. On the key path the draw starts at the `tu_tempo` entry SP and reached 124 B at the watched calls (188 B with the text routine), next to the stock window creation the stock TEMPO opener does anyway. Non-frame interrupt chains reach 528 B below the loop head with or without the Tuner. No hardware canary was measured.

### Limits

- Emulator only; no hardware timing, audio or canary. One run of each configuration.
- The fixture's seven FLEX tracks play the same sample; no USB or MIDI traffic was driven.
- The analysis cost is per update, amortised over its 400 blocks for the per-block figure; a single UI-task pass takes 9.5 ms (16.1 ms including the interrupts that preempt it), which can delay a key or redraw by that much while the window is open.
