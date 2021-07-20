from datetime import datetime

from pytest import fixture

from githook_timesheet.report import get_days_in_week, build_report

import githook_timesheet.report


@fixture(name="timesheet_repo")
def repo(tmp_path):
    base_dir = tmp_path
    (tmp_path / "2021").mkdir()
    days = [
        "2021-07-05",
        "2021-07-06",
        "2021-07-07",
        "2021-07-08",
        "2021-07-09",
        "2021-07-10",
        "2021-07-11",
    ]
    for day in days:
        path = tmp_path / "2021" / f"{day}.txt"
        print("day", day, path)
        with open(path, "w") as timesheet:
            timesheet.write(f"{day} - line1\n")
            timesheet.write(f"{day} - line2\n")
    yield base_dir


def test_build_report(timesheet_repo):
    old_header = githook_timesheet.report.header
    old_footer = githook_timesheet.report.footer
    githook_timesheet.report.header = lambda *args: ""
    githook_timesheet.report.footer = lambda *args: ""
    report = build_report(timesheet_repo, datetime(2021, 7, 7))
    githook_timesheet.report.header = old_header
    githook_timesheet.report.footer = old_footer
    expected = ( "line1\nline2\n")
    assert report == expected


def test_get_days_in_week_same_month():
    day = datetime(2021, 7, 7, 13, 14)
    expected_days = [
        datetime(2021, 7, 5, 0, 0),
        datetime(2021, 7, 6, 0, 0),
        datetime(2021, 7, 7, 0, 0),
        datetime(2021, 7, 8, 0, 0),
        datetime(2021, 7, 9, 0, 0),
        datetime(2021, 7, 10, 0, 0),
        datetime(2021, 7, 11, 0, 0),
    ]
    actual_days = get_days_in_week(day)
    assert actual_days == expected_days


def test_get_days_in_week_across_two_month():
    day = datetime(2021, 7, 1, 13, 14)
    expected_days = [
        datetime(2021, 6, 28, 0, 0),
        datetime(2021, 6, 29, 0, 0),
        datetime(2021, 6, 30, 0, 0),
        datetime(2021, 7, 1, 0, 0),
        datetime(2021, 7, 2, 0, 0),
        datetime(2021, 7, 3, 0, 0),
        datetime(2021, 7, 4, 0, 0),
    ]
    actual_days = get_days_in_week(day)
    assert actual_days == expected_days


def test_get_days_in_week_across_two_year():
    day = datetime(2021, 12, 29, 13, 14)
    expected_days = [
        datetime(2021, 12, 27, 0, 0),
        datetime(2021, 12, 28, 0, 0),
        datetime(2021, 12, 29, 0, 0),
        datetime(2021, 12, 30, 0, 0),
        datetime(2021, 12, 31, 0, 0),
        datetime(2022, 1, 1, 0, 0),
        datetime(2022, 1, 2, 0, 0),
    ]
    actual_days = get_days_in_week(day)
    assert actual_days == expected_days
