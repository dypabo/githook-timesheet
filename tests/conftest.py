import random
import string
import subprocess

import pytest


def get_random_string(
    length: int,
    letters: bool = True,
    digits: bool = True,
    spaces: bool = True,
    hex: bool = False,
) -> str:
    valid_characters = []
    if letters:
        valid_characters.extend(list(string.ascii_letters))
    if digits:
        valid_characters.extend(list(string.digits))
    if spaces:
        valid_characters.extend([" "])
    if hex:
        valid_characters.extend(list("0123456789abcdef"))

    return "".join(random.choice(valid_characters) for _ in range(length))


@pytest.fixture(name="temp_git_branch")
def fixture_temp_branch() -> str:
    current_branch = (
        subprocess.run(
            ["git", "branch", "--show-current"], stdout=subprocess.PIPE, check=True
        )
        .stdout.decode()
        .strip()
    )
    temp_branch_name = get_random_string(15, spaces=False)
    # checkout to a temporary branch
    subprocess.run(["git", "checkout", "-b", temp_branch_name], check=True)
    yield temp_branch_name
    # go back to original branch
    subprocess.run(["git", "checkout", current_branch], check=True)
    # delete temporary branch
    subprocess.run(["git", "branch", "-D", temp_branch_name], check=True)


@pytest.fixture(name="commit_msg")
def fixture_commit(temp_git_branch: str) -> str:
    commit_msg = get_random_string(20).strip()
    subprocess.run(["git", "commit", "--allow-empty", "-m", commit_msg], check=True)
    yield commit_msg
