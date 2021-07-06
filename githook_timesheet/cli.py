import argparse
import os
import sys
import typing

from githook_timesheet.commit import Commit
from githook_timesheet.git import get_latest_commit
from githook_timesheet.timesheet import add_to_timesheet


def commit_to_timesheet_entry(commit: Commit) -> str:
    """stringify commit object for entry in timesheet"""
    return str(commit)


def parse_args() -> typing.List:
    parser = argparse.ArgumentParser("")
    if "githook_timesheet_basedir" in os.environ:
        parser.add_argument(
            "timesheet_basedirectory",
            default=os.environ["githook_timesheet_basedir"],
            nargs="?",
            help="Directory where timesheet are store",
        )
    else:
        parser.add_argument(
            "timesheet_basedirectory",
            help="Directory where timesheet are store",
        )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    commit = get_latest_commit()
    timesheet_entry = commit_to_timesheet_entry(commit)
    add_to_timesheet(args.timesheet_basedirectory, timesheet_entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
