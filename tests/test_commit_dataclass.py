import datetime

from githook_timesheet.commit import Commit


def test_commit_creation():
    now = datetime.datetime.now()
    commit = Commit(now, "REPO", "TITLE")
    assert commit.title == "TITLE"
    assert commit.repo == "REPO"
    assert commit.timestamp == now


def test_commit_str():
    timestamp = datetime.datetime(2021, 1, 2, hour=3, minute=4, second=5)
    commit = Commit(timestamp, "REPO", "TITLE")
    assert str(commit) == "2021-01-02 03:04 - REPO - TITLE"
