from datetime import datetime

from githook_timesheet.cli.common import default_args_parser
from githook_timesheet.report import build_report


def main() -> int:
    """entry point for timesheet_report script"""
    parser = default_args_parser("Generate the weekly timesheet report")
    parser.add_argument(
        "date",
        default=datetime.now(),
        nargs="?",
        help="date for the report",
    )
    args = parser.parse_args()
    if isinstance(args.date, str):
        args.date = datetime.fromisoformat(args.date)
    report = build_report(args.timesheet_basedirectory, args.date)
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
