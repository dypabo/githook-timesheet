from githook_timesheet.git import get_repo_name, get_latest_commit


def test_get_latest_commit_one_line_log(commit_msg):
    commit = get_latest_commit()
    print(commit)
    assert commit.title.endswith(commit_msg)


def test_get_repo():
    assert get_repo_name() == "githook-timesheet"
