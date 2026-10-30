"""Tuner: retain the author's source, with local credits and stock guards.

The upstream directory is an unchanged copy of Tim Hastie's Tuner: v2.21 plus
his DC-removal commit (evidence/source-revendor-2026-10-30.json).
Its manifest derives its linked source path from its own file location, so
the native card build resolves that same source. The local wrapper replaces
only detour expectations with Modwerk guards; USB loading is unsupported.
The unchanged upstream reader requires the build working directory to contain
the local MAIN section before this wrapper can replace the expectations.
Qualification is recorded in TESTING.md.
"""
import dataclasses
import pathlib
import runpy

from remix.schema import Proof
from remix.stock_guard import stock_guard

_UPSTREAM = pathlib.Path(__file__).resolve().parent / "upstream" / "manifest.py"
_MODULE = runpy.run_path(str(_UPSTREAM), run_name="tuner_upstream_manifest")["MODULE"]
# Derived from verified local OS 1.40C; provenance is in evidence/guard-provenance.json.
_GUARDS = {
    0x40059ef0: stock_guard(0x40059ef0, 6, "f6a3ca67f755cf77cada82cbb69793ccf442a7994c8ec87a9dff56f83ca048c5"),
    0x4000d99a: stock_guard(0x4000d99a, 6, "9a7d100114ea50c9317af4f9de9210dd0eeae82f9ce03b255ac0d7bb5f707b91"),
    0x40056c72: stock_guard(0x40056c72, 6, "9c0a1089c078d792bc2cdac2cf3b905c17ad1f4466addf54f4b84f2fa2f9cdd0"),
}
if {detour.site for detour in _MODULE.detours} != _GUARDS.keys():
    raise ValueError("Tuner upstream detour inventory differs from its guard declarations")

MODULE = dataclasses.replace(
    _MODULE,
    detours=tuple(
        dataclasses.replace(detour, expect=_GUARDS[detour.site])
        for detour in _MODULE.detours
    ),
    author="timhastie",
    author_url="https://github.com/timhastie/octatrick-modules",
    proof=Proof.UNTESTED,
    proof_note="Modwerk 0.1.0 card integration is unqualified; hardware and timing checks pending; USB loading unsupported.",
)
