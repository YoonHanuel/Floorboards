from __future__ import annotations

import argparse

from .core import audit, choose_specimen, find_specimen, load_specimens, render_specimen


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="floorboards",
        description="Turn attractive conclusions back into testable assumptions.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="list known specimens")

    show = sub.add_parser("show", help="show one specimen")
    show.add_argument("specimen_id")

    sub.add_parser("random", help="shake the house and see what creaks")
    sub.add_parser("audit", help="check specimen files for obvious structural nonsense")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    specimens = load_specimens()

    if args.command == "list":
        if not specimens:
            print("No specimens. The house is either perfect or uninspected.")
            return 0
        for specimen in specimens:
            print(f"{specimen.id:28} {specimen.title}")
        return 0

    if args.command == "show":
        try:
            specimen = find_specimen(args.specimen_id, specimens)
        except KeyError as exc:
            print(exc.args[0])
            return 2
        print(render_specimen(specimen))
        return 0

    if args.command == "random":
        print(render_specimen(choose_specimen(specimens)))
        return 0

    if args.command == "audit":
        problems = audit(specimens)
        if problems:
            print("THE HOUSE CREAKS STRUCTURALLY")
            for problem in problems:
                print(f"- {problem}")
            return 1
        print(f"{len(specimens)} specimens inspected. Null Signal working as designed.")
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
