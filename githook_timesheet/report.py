from datetime import datetime
from typing import List
from pathlib import Path

from .timesheet import get_timesheet_entries

MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7


def get_days_in_week(timestamp: datetime) -> List[datetime]:
    """return all days in the week of `timestamp`. Week start on Monday"""
    year, week, weekday = timestamp.isocalendar()
    days = [
        datetime.strptime(f"{year} {week} {weekday}", "%G %V %u")
        for weekday in range(1, 8)
    ]
    return days


def build_report(base_directory_path: Path, timestamp: datetime):
    days = get_days_in_week(timestamp)
    res = ""
    for day in days:
        for entry in get_timesheet_entries(base_directory_path, day):
            res += entry + "\n"
    return res
