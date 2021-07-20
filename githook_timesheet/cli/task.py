from datetime import datetime

from githook_timesheet.commit import Commit
from githook_timesheet.timesheet import add_to_timesheet

from .common import default_args_parser, commit_to_timesheet_entry


def main() -> int:
    """entry point for the post_commit script"""
    parser = default_args_parser("Add task to time sheet manually")

    parser.add_argument("project", help="Project")
    parser.add_argument("details", help="Details about the work done")
    args = parser.parse_args()

    now = datetime.now()
    commit = Commit(now, args.project, args.details)
    timesheet_entry = commit_to_timesheet_entry(commit)
    add_to_timesheet(args.timesheet_basedirectory, timesheet_entry)


if __name__ == "__main__":
    raise SystemExit(main())
