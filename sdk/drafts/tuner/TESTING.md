# Tuner integration evidence

## Identity and qualification boundary

- Draft module: `tuner`, `0.1.0-experimental`, under `sdk/drafts/tuner`.
- Current author source: `timhastie/octatrick-modules` v2.20, commit `fd18f5530989be348e6aa4c6e38f93beba555e6d`; all four upstream files, including the stock-guard reader, are copied unchanged.
- Current documentation/draft base: Modwerk `4e2226f1be6347f74d51a0d5b99ee572ba3a82bb`.
- Preserved native candidate build baseline: `916ce01bbfc60f3aedd7156066354fedb521e6f4`, private `relay-tuner` facade, Tuner only, stock FX and static stock DSP; no USB base.
- The delivered BIN/bus have **not** been rebuilt from this v2.20 source, current main, the hash-guard wrapper, or the new draft/promotion commit. They are historical candidate evidence, not exact-current-commit qualification.

The wrapper now preserves the upstream runtime/source declarations while replacing its three detour expectations with verified Modwerk-form guards. [guard-provenance.json](evidence/guard-provenance.json) records the adapter change. It is not a rebuilt-image result. No hardware, resource, timing or publication qualification object is fabricated.

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
