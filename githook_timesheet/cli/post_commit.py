import sys

from githook_timesheet.commit import Commit
from githook_timesheet.git import get_latest_commit
from githook_timesheet.timesheet import add_to_timesheet

from .common import default_args_parser


def commit_to_timesheet_entry(commit: Commit) -> str:
    """stringify commit object for entry in timesheet"""
    return str(commit)


def main() -> int:
    """entry point for the post_commit script"""
    parser = default_args_parser("Take last commit and add it to the timesheet")
    args = parser.parse_args()
    commit = get_latest_commit()
    timesheet_entry = commit_to_timesheet_entry(commit)
    add_to_timesheet(args.timesheet_basedirectory, timesheet_entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
