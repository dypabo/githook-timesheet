from datetime import datetime
import os
from githook_timesheet.timesheet import (
    get_current_timesheet_filename,
    add_to_timesheet,
    get_year,
    get_filename,
    get_timesheet_entries,
)


def test_add_to_timesheet_file_exists(tmp_path):
    filename = get_filename(datetime.now())
    year = get_year(datetime.now())
    # new file
    add_to_timesheet(tmp_path, "this is the first entry")
    # append to existing file
    add_to_timesheet(tmp_path, "this is the second entry")
    assert os.path.exists(tmp_path / year / filename)
    with open(tmp_path / year / filename) as f:
        assert f.read() == "this is the first entry\nthis is the second entry\n"


def test_add_to_timesheet(tmp_path):
    add_to_timesheet(tmp_path, "this is an entry")
    filename = get_filename(datetime.now())
    year = get_year(datetime.now())
    assert os.path.exists(tmp_path / year / filename)
    with open(tmp_path / year / filename) as f:
        assert f.read() == "this is an entry\n"


def test_get_current_timesheet_filename_file_does_not_exists(tmp_path):
    filename = get_filename(datetime.now())
    year = get_year(datetime.now())
    expected_path = tmp_path / year / filename
    actual_path = get_current_timesheet_filename(tmp_path, datetime.now())
    assert actual_path == expected_path


def test_get_current_timesheet_filename_file_exists(tmp_path):
    filename = get_filename(datetime.now())
    year = get_year(datetime.now())
    expected_path = tmp_path / year / filename
    (tmp_path / year).mkdir(parents=True, exist_ok=True)
    expected_path.touch()
    assert os.path.exists(expected_path)
    actual_path = get_current_timesheet_filename(tmp_path, datetime.now())
    assert actual_path == expected_path


def test_get_timesheet_entries(tmp_path):
    (tmp_path / "2021").mkdir()
    timesheet_path = tmp_path / "2021" / "2021-07-07.txt"
    with open(timesheet_path, "w") as timesheet:
        timesheet.write("line1\n")
        timesheet.write("line2\n")
        timesheet.write("\n")
        timesheet.write("line3\n")
        timesheet.write("\n")
        timesheet.flush()
    entries = get_timesheet_entries(tmp_path, datetime(2021, 7, 7))
    assert entries == ["line1", "line2", "line3"]


def test_get_timesheet_entries_file_not_found(tmp_path):
    entries = get_timesheet_entries(tmp_path, datetime(2021, 7, 7))
    assert entries == []
