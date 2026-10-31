# FM Synth — 0.1.4 experimental

## Overview

FM SYNTH is a dedicated track machine beside FLEX, STATIC, THRU, NEIGHBOR and PICKUP. It is Tim Hastie’s two-operator FM engine from his Octatrick 2.21 line: a sine carrier with a sine modulator, feedback and an index-decay envelope, one to four paraphonic voices with chord shapes, MIDI, legato and glide, through the track’s existing AMP, filter and effects. The scale quantizer that the engine reads (SCALE, ROOT and GLIDE) is bundled privately and follows the scale on FM SYNTH tracks.

`upstream/synth` and `upstream/quantizer` are the author’s files at `3531b8eae8d782795cfbcc8596e6e9c29b251162`, byte for byte (not yet published): release 2.21’s engine and machine list (tag `v2.21`, `9e4d34adc63fbb1732b125697d6738262e1eae85`), his quantizer with the per-track switches as the SEQUENCER rows TRACK and FOLLOW (`990eff8`, the source Scale Quantizer 0.1.4 carries), `poly.s` exporting the engine state the quantizer’s panel transaction reads in a remix without SY DRUM, and `poly.s` reading the scale as OFF on an FM SYNTH track whose FOLLOW is OFF (`3531b8e`, 30 October 2026: before it only ROOT was skipped and the keys were still snapped). The author’s [README](upstream/synth/README.md) describes every feature and its measurements.

What changes for players since 0.1.2:

- Step and scene locks on every FM control; VOIC and CHRD under LFOs and scenes ([#751](https://github.com/repeat98/modwerk/issues/751)).
- Chords on the chromatic keys keep their notes with a scale set, however fast the keys are pressed together, and the first chord after power-on in a saved project plays as a chord (both new in the author’s 2.21).
- The click at note start and end is gone ([#557](https://github.com/repeat98/modwerk/issues/557)); a chord’s first trig follows the AMP envelope ([#710](https://github.com/repeat98/modwerk/issues/710)).
- LFOs and scene locks on AMP ATK, HOLD and REL shape the sound, and an LFO on PTCH moves the pitch as far as on FLEX, following Jan Kolkmeier’s report and fix in [#883](https://github.com/repeat98/modwerk/issues/883) / [#884](https://github.com/repeat98/modwerk/pull/884).
- A selection guard: a Part holds at most two FM SYNTH tracks, and the voices are capped so the Part stays inside the CPU budget. A machine change to or from FM SYNTH resets the track’s machine parameters to init (locks are kept, as in stock).
- The bundled scale quantizer is FM Synth’s own: it follows the scale on FM SYNTH tracks. MIDI tracks, and the trig-time pitch of sample tracks, are the public Scale Quantizer’s ([#555](https://github.com/repeat98/modwerk/issues/555)); SEQUENCER shows SCALE, ROOT and GLIDE.
- **With Scale Quantizer.** A declared conflict for now, as agreed with the owner on [#555](https://github.com/repeat98/modwerk/issues/555) (30 October 2026): both carry the same quantizer source and would patch the same sites. The octabam SDK rule `shared_supply` (`tools/remix/machine_composition.py`, a separate base PR) lets the card build keep one quantizer: Scale Quantizer’s hooks and rows, aimed at FM Synth’s bundled copy, and FM Synth’s own quantizer hooks and rows left out. SEQUENCER then shows SCALE, ROOT, GLIDE, TRACK and FOLLOW once; MIDI tracks, a sample track’s trigs and the chromatic keyboard’s mark follow the scale too, and FOLLOW OFF takes any audio track, FM SYNTH tracks included, or MIDI track out of it. That image (TEST2, TESTING.md) was built with the rule and tested on the author’s MKI on 30 October 2026; the conflict goes in a follow-up once the rule is merged.
- Card builds keep the SRC page out of the 16 bytes the stock DELAY reads past its 508-entry table at a slow tempo with a long TIME (zero on a stock unit; 0.1.2 kept page code there): the page is a DRAM unit, as in Jannik Aßfalg’s [#895](https://github.com/repeat98/modwerk/pull/895) for 0.1.3, which the author’s 2.21 adopted. Nothing you see or play on FM Synth changes.
- Level: about 12 dB louder than 0.1.2 at the same settings. The engine keeps 6 dB of headroom instead of 0.1.2’s 18 dB; AMP VOL 0 is the reference, and VOL above it can clip a full-scale voice.

## Controls

| Page | Control | Initial value / range | Function |
| --- | --- | --- | --- |
| SRC A | PTCH | raw 64; −64…+63 semitones | Carrier pitch; chromatic and scale edits constrain notes. |
| SRC B | RATO | raw 12 = 1; 32 ratios 0.25…16 | Modulator/carrier frequency ratio. |
| SRC C | INDX | 32; 0…127 | FM depth; 0 gives the unmodulated carrier. |
| SRC D | FINE | raw 64 = 0; −64…+63 cents | Fine pitch tuning. |
| SRC E | FDBK | 0; 0…127 | Modulator feedback. |
| SRC F | DEC | 40; 0…127 (127 = hold) | Decay of the modulation index, separate from amplitude. |
| FUNC+SRC (SETUP) | VOIC | 1; 1…4 | Paraphonic voices (the former LOOP box). |
| FUNC+SRC (SETUP) | CHRD | none; 32 shapes × 4 inversions | Chord shape and inversion (the former SLIC box). |
| FUNC+AMP F | LEG | OFF / MONO / POLY | Retrigger or overlapping mono/paraphonic legato. |
| PROJECT > CONTROL > SEQUENCER | SCALE, ROOT, GLIDE | OFF; 24 scales / C…B / OFF, 1…127 | Scale quantization, its key, the legato slide time. |

AMP ATK, HOLD and REL drive the engine’s own gain envelope, with their locks, scenes and LFOs. An LFO on PTCH moves the pitch 0.2 semitone per unit of depth, as on FLEX; FLEX’s PTCH stops at ±12.8 semitones, an FM SYNTH track’s range goes further.

## Usage

FM SYNTH is chosen per track in SRC SETUP’s machine list, like FLEX or STATIC, and needs no sample. A Part holds at most two FM SYNTH tracks. The SRC page holds the FM controls, SRC SETUP (FUNC+SRC) holds VOIC and CHRD, AMP shapes the gain envelope as on any track, and the scale, its root and the glide time are set in PROJECT > CONTROL > SEQUENCER.

### Quick tutorial: play FM Synth

1. Open a disposable project with FM Synth firmware. Select an audio track, hold FUNC and press SRC, select FM SYNTH with UP/DOWN and press YES. No sample is required.
2. Press SRC. Set RATO to 1 and turn INDX from 0 upwards to hear a sine tone acquire FM harmonics. PTCH transposes it; FINE tunes it in cents; FDBK adds feedback; DEC shortens the modulation envelope.
3. Place a trig and press PLAY. In SRC SETUP (FUNC+SRC) set VOIC to 2–4 and CHRD to a chord if wanted. AMP ATK/HOLD/REL shape the gain envelope; FUNC+AMP exposes LEG.
4. Press STOP twice to silence the voice. To return to a sample machine, hold FUNC and press SRC, select FLEX or STATIC and press YES; assign the desired sample in the normal way.

For scales and glide, open PROJECT > CONTROL > SEQUENCER.

## Compatibility and limitations

OS 1.40C only. Parts store internal FLEX kind 1 plus `FM/1` in unused NEIGHBOR bytes. A stock build reads the track as FLEX and cannot synthesize FM; select a stock machine explicitly before downgrading.

The matching quantizer is bundled privately because the engine shares its mailbox and scale accessor. Do not combine with Analog BD: their hooks overlap. The public Scale Quantizer is a declared conflict until the `shared_supply` rule is merged (above). With FM Synth alone, MIDI tracks are not quantized; on STATIC and FLEX tracks the PTCH knob, PTCH locks and chromatic keys still step through the scale, but a trig’s PTCH is not snapped as it plays and the chromatic keyboard marks the key pressed rather than the note sounded. A project saved with Scale Quantizer or Octatrick keeps the audio tracks it set OFF out of the scale here, FM SYNTH tracks included (their chromatic keys, chords and PTCH play plain semitones); FM Synth has no row to change it (Scale Quantizer’s TRACK and FOLLOW, once the two can be built together).

LFO SETUP names an FM SYNTH track’s six PLAYBACK destinations with FLEX’s names (PTCH STRT LEN RATE RTRG RTIM). Which FM control each one modulates follows the author’s LFO routing, which this version keeps. Giving the entries their FM names is the base’s ([#589](https://github.com/repeat98/modwerk/issues/589)); the author’s own fix meets the base’s machine-name table and is not in this module. Beside POLY8 this version does not build yet: POLY8’s composition record covers 0.1.2’s machine-list sites, not 0.1.4’s (see TESTING.md, [#941](https://github.com/repeat98/modwerk/issues/941)). FM Synth installs alone: the author’s SY DRUM rows are not assembled here, and his trig-mute rule (2.19, which in his own builds reads Mute Modes’ words) reads two words of this module’s `port.s` instead. Over USB those words would carry the base’s answer to `ev_trig_muted` ([#912](https://github.com/repeat98/modwerk/pull/912)), so a track a mute module silences starts no new FM note; on a card build, and on a base without that event, they stay 0 and every trig plays, as in 0.1.2.

This version installs with a card build. Its USB package for the Octatrack base cannot be built yet: the engine’s DRAM regions (the step-lock work table, the scene table, the project migration buffers) and the units’ generated includes are refused in a runtime package. The machine-port lines for the base (`sdk/machines/octatrack/module-adapters/machine-ports.json`) are prepared: the machine record does the author’s selection guard, its popup and his machine-change init at the base’s chooser commit, and two hooks still meet base sites (see TESTING.md).

## Tests and measurements

See [TESTING.md](TESTING.md). The author reports this build’s image (TEST7) working on his MKI on 30 October 2026, every item of its test sheet; the TEST4 report of 26 October 2026 was for the 2.20 cut.

## Authorship and licences

Tim Hastie: FM engine, machine list, PLAYBACK page, step and scene locks, voices/chords, MIDI/legato and the bundled quantizer, pinned to `3531b8eae8d782795cfbcc8596e6e9c29b251162` (Octatrick 2.21, tag `v2.21`, with the TRACK / FOLLOW quantizer, the `sy_state` export and an FM SYNTH track's FOLLOW OFF reading the scale as OFF; not yet published). Jan Kolkmeier: the report and fix of the AMP envelope under LFOs and scenes and of the LFO PTCH depth (#883 / #884), folded into 2.20 and carried in 2.21. Jannik Aßfalg: the SRC page as a DRAM unit, out of the stock DELAY’s table tail (#895), for 0.1.3, which the author’s 2.21 adopted. Sam Banks: octabam wrapper/platform. Modwerk contributors: the chooser the author’s machine list is adapted from, Part signature, sample-free source transport, verification, docs and original SVG. Full MIT terms are in [LICENSE](LICENSE) and [upstream/LICENSE](upstream/LICENSE).

No firmware, extracted stock byte blobs/tables, cards, RAM dumps or compiled images are distributed. Every stock expectation is a Modwerk `stock_guard(address, length, sha256)` in `manifest.py` (listed in `stock-guards.json`) and resolves lazily from the verified developer-owned OS. The author’s manifests carry no stock bytes: both read every guard through their `stock_guard.py`, which this wrapper answers from its own table, and the PLAYBACK page is ratified by its length and SHA-256. The eight hooks this module leaves out (manifest.py `_DROPPED`) are declared by nothing; their spans are only answered for the author’s manifests.

## Screens and audio

The captures are from this version’s native card build (headless ot_emu, MAIN `8d89d596`, the author’s 2.21, 30 October 2026); all six are byte-identical to the 2.20 cut’s, and five of them to 0.1.2’s. The audio preview is from 0.1.2 and has not been retaken.

![FM SYNTH is the dedicated sixth machine row in SRC SETUP.](media/ot-location.png)

![PTCH, RATO, INDX, FINE, FDBK and DEC replace the FLEX source controls.](media/ot-controls.png)

![LEG selects OFF, MONO or POLY on an FM track.](media/ot-legato.png)

![The privately bundled quantizer adds SCALE; this example selects MAJOR.](media/ot-scale.png)

![ROOT chooses the key; this example uses C.](media/ot-root.png)

![GLIDE sets pitch slide time; this example shows OFF.](media/ot-glide.png)

