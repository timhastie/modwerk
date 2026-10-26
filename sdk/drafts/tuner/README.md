# Tuner

Version 0.1.0-experimental. Tim Hastie’s Tuner, packaged as an unqualified Modwerk draft from the exact v2.20 source.

## Overview

Hold **UP first, then press TEMPO** to open a pitch readout for the selected audio track. The source provides note and octave, signed cents, frequency and a needle around the nearest note, with A4 fixed at 440 Hz. It reads after track effects and before the fader, uses no effect slot and is designed to leave the audio unchanged.

**Card builds only: the base has no removal refusal for ordinary modules.** USB support is optional future work; the earlier admission proposal is retained in [evidence/usb-admission.md](evidence/usb-admission.md), not implemented or required for this card-only draft.

The preserved v2.19/card-sdk candidate has a successful historical build and seven reviewed emulator UI captures. It was **not rebuilt from this v2.20 source or current main**. Exact-current-source build, hardware, live pitch, timing and resource qualification remain pending. [TESTING.md](TESTING.md) separates those gaps from the observed window behavior.

## Controls

| Action | Intended result |
| --- | --- |
| Hold UP first, then press TEMPO | Open the tuner, or close it if already open. |
| TEMPO, YES or NO while open | Close the tuner window. |
| Select an audio track | Read that track; MIDI mode retains the selected audio track. |
| TEMPO alone | Ordinary tempo window. |
| FUNC + TEMPO | Ordinary tapping gesture. |

There are no editable tuner parameters, locks, LFO destinations or calibration controls. Below the signal or confidence threshold, the source retains the last valid reading. A held reading is not a fresh pitch estimate. Before the first valid reading, the display has no pitch result.

## Usage

### Quick tutorial: tune a steady sound

1. Use an identified card build and select an audio track receiving a steady pitched sound. No effect slot is required.
2. Hold UP first, then press TEMPO to open Tuner. Pressing TEMPO first follows the ordinary tempo-window route instead.
3. Adjust the sound at its source while watching the readout. The intended reference is A4 at 440 Hz, with the cents reading and needle near the center. Accuracy and live response on this integration still require the hardware check.
4. Press TEMPO, YES or NO to close. The opening gesture also toggles the window; its toggle-off path remains a hardware checklist item.

## Screens and audio

These are preserved LCD pixels from the earlier native candidate using a separately identified source-built emulator. This is a tooling substitution, not a firmware fix. No audio was played or recorded, and the standalone 2.19 reference exited before capture, so no paired visual equivalence is established.

Select an audio track before opening Tuner. The starting page is unobstructed.

![Track source-parameter page with no modal window](media/01-track-page.png)

Hold UP first, then press TEMPO. The tuner window is visible here, but its pitch readout is unpopulated; the ruler and center mark do not prove a working live needle.

![Tuner overlay with an unpopulated pitch readout and a pitch ruler](media/02-tuner-open.png)

Press TEMPO to close. The track page is visible again, with no tuner overlay.

![Track page after the tuner window closes](media/05-closed-tempo.png)

More screenshots retain the alternate [NO close state](media/03-closed-no.png), [YES close state](media/04-closed-yes.png), [ordinary tempo window](media/06-normal-tempo.png) and [tempo-tapping dialog](media/07-func-tempo.png). All seven images were reviewed. The unmodified [capture record](media/capture.json) binds their identities and input plan; [the UI evidence note](evidence/ui-capture-2026-10-26.json) records the tooling and qualification limits. The [thumbnail](presentation/thumbnail.svg) is conceptual artwork, not an instrument capture.

## Compatibility and limitations

- Targets OS 1.40C and declares `key:UP+TEMPO`. The historical source describes both Octatrack models; this capture used an MKII panel, not physical hardware.
- It estimates one pitch. Complex, noisy or inharmonic sounds can wander or select an octave. Track effects can change the estimate.
- Track level and the crossfader act after the tapped signal; lowering final output does not necessarily stop the readout.
- No tuner setting is stored in a Part, project, card or battery RAM. The window and working history are temporary.
- The private declaration compatibility check passed on the earlier fixture. Companion behavior and current-base runtime compatibility remain unqualified.
- An older retained emulator failed in its DSP write callback. Which image property triggers that fault remains unresolved; the current capture does not justify a Tuner firmware correction.
- Card-only acceptance does not supply hardware, timing, resource or exact-build qualification, and does not waive the catalogue’s evidence requirements.

## Tests and measurements

The earlier private native build and declaration compatibility check passed. A no-Tuner control booted with the retained emulator. The candidate subsequently completed the seven-image UI walk with substituted tooling; the reference image failed before UI commands. The prior draft check failed in application tests. [TESTING.md](TESTING.md) preserves these separate outcomes.

Current code/data/padding, loader overhead, maximum stack, worst-case cycles, pitch accuracy, audio continuity and behavior under load remain unqualified. Historical upstream measurements explain the design but do not qualify this draft or its current source revision.

## Authorship and licences

Tuner is by **Tim Hastie (@timhastie)**, from `timhastie/octatrick-modules` tag `v2.20`, commit `fd18f5530989be348e6aa4c6e38f93beba555e6d`. All four files in `upstream/` are unchanged. The local wrapper preserves the upstream runtime/source declarations and replaces the three detour expectations with verified Modwerk-form hash guards; [guard provenance](evidence/guard-provenance.json) records that adapter change. The preserved card image predates both that adapter and this source update. The immutable upstream reader needs the build working directory's local MAIN section before manifest import; the Modwerk wrapper then replaces the three expectations with lazy digest guards. No current-source build or check was run during the re-vendor.

The upstream MIT terms remain in [LICENSE](LICENSE). Octabam supplies the native platform. Documentary screenshots retain the underlying interface rights; firmware is not included. No hardware endorsement or affiliation is asserted.
