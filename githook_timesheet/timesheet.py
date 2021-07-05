import datetime
import os
import pathlib

TIMESHEET_FILENAME_FORMAT = "%Y-%m-%d.txt"


def get_current_timesheet_filename(base_directory_path: str) -> str:
    filename = datetime.datetime.now().strftime(TIMESHEET_FILENAME_FORMAT)
    directory = pathlib.Path(base_directory_path)
    if not os.path.exists(directory / filename):
        pathlib.Path(directory / filename).touch()
    return directory / filename


def add_to_timesheet(base_directory_path: str, entry: str) -> None:
    path = get_current_timesheet_filename(base_directory_path)
    with open(str(path), "a") as f:
        f.write(entry)
        f.write("\n")
