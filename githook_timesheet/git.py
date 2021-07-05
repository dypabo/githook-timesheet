import datetime
import os
import subprocess

from .commit import Commit

COMMIT_INFO_TIMESTAMP = slice(0, 25)
COMMIT_INFO_TITLE = slice(26, None)
GIT_LOG_FORMAT = "--format=%ci %s"
GIT_LOG_TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S %z"


def get_repo_name() -> str:
    res = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        stdout=subprocess.PIPE,
        check=True,
    )
    full_repo_name = res.stdout.decode().strip()
    _, repo_name = os.path.split(full_repo_name)
    return repo_name


def get_latest_commit() -> Commit:
    """
    git latest commit with this format
    2021-07-05 13:01:02 -0400 commit msg
    """
    res = subprocess.run(["git", "log", GIT_LOG_FORMAT, "-n1"], stdout=subprocess.PIPE)
    info = res.stdout.decode().strip()
    repo = get_repo_name()
    commit_msg = info[COMMIT_INFO_TITLE]
    timestamp = datetime.datetime.strptime(
        info[COMMIT_INFO_TIMESTAMP], GIT_LOG_TIMESTAMP_FORMAT
    )
    return Commit(timestamp, repo, commit_msg)
