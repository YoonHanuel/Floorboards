from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import random
from typing import Iterable


@dataclass(frozen=True)
class Ferret:
    intervention: str
    if_claim: str
    if_floorboard: str


@dataclass(frozen=True)
class Specimen:
    id: str
    title: str
    observed: tuple[str, ...]
    concluded: str
    floorboard: str
    missing_evidence: tuple[str, ...]
    ferret: Ferret
    tags: tuple[str, ...] = ()

    @classmethod
    def from_dict(cls, raw: dict) -> "Specimen":
        ferret_raw = raw["ferret"]
        return cls(
            id=raw["id"],
            title=raw["title"],
            observed=tuple(raw.get("observed", [])),
            concluded=raw["concluded"],
            floorboard=raw["floorboard"],
            missing_evidence=tuple(raw.get("missing_evidence", [])),
            ferret=Ferret(
                intervention=ferret_raw["intervention"],
                if_claim=ferret_raw["if_claim"],
                if_floorboard=ferret_raw["if_floorboard"],
            ),
            tags=tuple(raw.get("tags", [])),
        )


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def specimen_dir() -> Path:
    return repo_root() / "specimens"


def load_specimens(path: Path | None = None) -> list[Specimen]:
    root = path or specimen_dir()
    specimens: list[Specimen] = []
    for file in sorted(root.glob("*.json")):
        with file.open("r", encoding="utf-8") as handle:
            specimens.append(Specimen.from_dict(json.load(handle)))
    return specimens


def find_specimen(specimen_id: str, specimens: Iterable[Specimen] | None = None) -> Specimen:
    pool = list(specimens if specimens is not None else load_specimens())
    for specimen in pool:
        if specimen.id == specimen_id:
            return specimen
    known = ", ".join(s.id for s in pool) or "none"
    raise KeyError(f"unknown specimen {specimen_id!r}; known: {known}")


def choose_specimen(specimens: Iterable[Specimen] | None = None) -> Specimen:
    pool = list(specimens if specimens is not None else load_specimens())
    if not pool:
        raise RuntimeError("the floorboards are suspiciously silent: no specimens found")
    return random.choice(pool)


def render_specimen(specimen: Specimen) -> str:
    lines = [
        "FOUND A FLOORBOARD",
        "",
        f"specimen: {specimen.id}",
        f"title: {specimen.title}",
        "",
        "observed:",
    ]
    lines.extend(f"  - {item}" for item in specimen.observed)
    lines.extend([
        "",
        "concluded:",
        f"  {specimen.concluded}",
        "",
        "floorboard:",
        f"  {specimen.floorboard}",
        "",
        "missing evidence:",
    ])
    if specimen.missing_evidence:
        lines.extend(f"  - {item}" for item in specimen.missing_evidence)
    else:
        lines.append("  - none recorded; either excellent news or suspicious confidence")
    lines.extend([
        "",
        "suggested ferret:",
        f"  intervention: {specimen.ferret.intervention}",
        f"  if claim:     {specimen.ferret.if_claim}",
        f"  if floorboard:{' ' if specimen.ferret.if_floorboard else ''}{specimen.ferret.if_floorboard}",
    ])
    if specimen.tags:
        lines.extend(["", "tags: " + ", ".join(specimen.tags)])
    return "\n".join(lines)


def audit(specimens: Iterable[Specimen] | None = None) -> list[str]:
    pool = list(specimens if specimens is not None else load_specimens())
    problems: list[str] = []
    seen: set[str] = set()

    for specimen in pool:
        if specimen.id in seen:
            problems.append(f"duplicate id: {specimen.id}")
        seen.add(specimen.id)

        if not specimen.observed:
            problems.append(f"{specimen.id}: observation list is empty")
        if not specimen.floorboard.strip():
            problems.append(f"{specimen.id}: floorboard is empty")
        if not specimen.ferret.intervention.strip():
            problems.append(f"{specimen.id}: ferret has no intervention")

    return problems
