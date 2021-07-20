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


def header(first_day: datetime, last_day: datetime):
    first_day_str = datetime.strftime(first_day, "%Y-%m-%d")
    last_day_str = datetime.strftime(last_day, "%Y-%m-%d")
    res = ""
    res += "#SR&ED\n"
    res += f"{first_day_str} to {last_day_str}\n"
    res += "\n"
    return res


def footer():
    res = "\n"
    res += "Time Allocation:\n"
    res += "0% - Electronic\n"
    res += "0% - Algorithms\n"
    res += "0% - Firmware\n"
    res += "0% - Prototype Interface\n"
    res += "0% - Tests and validations\n"
    res += "0% - Support/Sales/Admin"
    return res


def build_report(base_directory_path: Path, timestamp: datetime):
    days = get_days_in_week(timestamp)
    res = header(days[0], days[-1])
    entries = []
    for day in days:
        entries += get_timesheet_entries(base_directory_path, day)
    entries = sorted(list(set([f"{' - '.join(entry.split(' - ')[1:])}" for entry in entries])))
    for entry in entries:
        res += f"{entry}\n"
    res += footer()
    return res
