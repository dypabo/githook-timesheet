import sys


from .common import default_args_parser


def main() -> int:
    """entry point for timesheet_report script"""
    parser = default_args_parser("Generate the weekly timesheet report")
    args = parser.parse_args()
    return 0


if __name__ == "__main__":
    sys.exit(main())
