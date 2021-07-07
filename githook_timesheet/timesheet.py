from datetime import datetime
import os
from pathlib import Path


TIMESHEET_FILENAME_FORMAT = "%Y-%m-%d.txt"


def get_timesheet_entries(base_directory_path: Path, timestamp: datetime):
    filename = get_filename(timestamp)
    timesheet_path = base_directory_path / get_year(timestamp) / filename
    if not os.path.exists(timesheet_path):
        return []
    with open(timesheet_path) as timesheet:
        return [entry.strip() for entry in timesheet.readlines() if entry.strip()]


def get_filename(timestamp: datetime) -> str:
    filename = timestamp.strftime(TIMESHEET_FILENAME_FORMAT)
    return filename


def get_year(timestamp: datetime) -> str:
    return timestamp.strftime("%Y")


def make_directories(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_current_timesheet_filename(
    base_directory_path: Path, timestamp: datetime
) -> str:
    year_dir = get_year(timestamp)
    directory = make_directories(base_directory_path / year_dir)
    filename = get_filename(timestamp)
    if not os.path.exists(directory / filename):
        (directory / filename).touch()
    return directory / filename


def add_to_timesheet(base_directory_path: Path, entry: str, timestamp=None) -> None:
    if timestamp is None:
        timestamp = datetime.now()
    path = get_current_timesheet_filename(base_directory_path, timestamp)
    with open(str(path), "a") as f:
        f.write(entry)
        f.write("\n")
