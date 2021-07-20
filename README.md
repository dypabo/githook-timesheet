# githook-timesheet

The command must be run from inside a GIT Repository.

Once the command is run, it will fetch the last commit and extract the commit title and create an entry in the timesheet files.

The timesheet file have the following formats
2021-07-05 10:01 - REPO NAME - COMMIT TITLE

There is one timesheet file per day.

You can copy the file `post-commit` include in the repo and copy it in the directory `./git/hooks/` inside all repositories you are working on.

You can also copy it in your `template` directory. That way, every time you `git clone` or `git init` a new repository. The `post-commit` hook will automatically be copy in the new repository.

On Mac the directory is : `/usr/local/opt/git/share/git-core/templates/hooks/`
On Linux (Ubuntu) the directory is : `/usr/share/git-core/templates/hooks/`


## Requirements
- GIT
- python3.9  (Should work with python3.6 and up)

## Installation

in the repo directory run the following command
```
python3 -m pip install .
```

You must set the following environment variable in your `.bashrc` or `.zshrc`
```
export githook-timesheet-basedir=<path to where you want to save timesheet data>
```

## Non software timetracking
For tracking time manually without repository, you simply have to run the following command.

```
githook_timesheet_task <title> <details>
```

## Weekly Report
to get a report for all the work done in a week. run the following command.
```
githook_timesheet_weekly_report 2021-07-07
```
It will find all items in the week starting on the Monday of the supplied date.
