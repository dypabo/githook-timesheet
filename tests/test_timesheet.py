import datetime
import os
import pathlib

from githook_timesheet.timesheet import (
    get_current_timesheet_filename,
    TIMESHEET_FILENAME_FORMAT,
    add_to_timesheet,
)


def test_add_to_timesheet_file_exists(tmp_path):
    filename = datetime.datetime.now().strftime(TIMESHEET_FILENAME_FORMAT)
    # new file
    add_to_timesheet(tmp_path, "this is the first entry")
    # append to existing file
    add_to_timesheet(tmp_path, "this is the second entry")
    assert os.path.exists(tmp_path / filename)
    with open(tmp_path / filename) as f:
        assert f.read() == "this is the first entry\nthis is the second entry\n"


def test_add_to_timesheet(tmp_path):
    add_to_timesheet(tmp_path, "this is an entry")
    filename = datetime.datetime.now().strftime(TIMESHEET_FILENAME_FORMAT)
    assert os.path.exists(tmp_path / filename)
    with open(tmp_path / filename) as f:
        assert f.read() == "this is an entry\n"


def test_get_current_timesheet_filename_file_does_not_exists(tmp_path):
    filename = datetime.datetime.now().strftime(TIMESHEET_FILENAME_FORMAT)
    expected_path = tmp_path / filename
    actual_path = get_current_timesheet_filename(tmp_path)
    assert actual_path == expected_path


def test_get_current_timesheet_filename_file_exists(tmp_path):
    filename = datetime.datetime.now().strftime(TIMESHEET_FILENAME_FORMAT)
    expected_path = tmp_path / filename
    pathlib.Path(expected_path).touch()
    assert os.path.exists(expected_path)
    actual_path = get_current_timesheet_filename(tmp_path)
    assert actual_path == expected_path
