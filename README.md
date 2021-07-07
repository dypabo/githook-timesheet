# githook-timesheet

The command must be run from inside a GIT Repository.

Once the command is run, it will fetch the last commit and extract the commit title and create an entry in the timesheet files.

The timesheet file have the following formats
2021-07-05 10:01 - REPO NAME - COMMIT TITLE

There is one timesheet file per day.

You can copy the file `post-commit` include in the repo and copy it in the directory `./git/hooks/` inside all repositories you are working on.

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
export githook-timesheet-basedir
```

## Non software timetracking
for tracking time on non software project. You can create personnal repos and adding the `post-commit` file to the hooks directory.

you then have to do a commit to track your time.
```
git commit --allow-empty -m "I am workig on this issue right now"
```

## Weekly Report
to get a report for all the work done in a week. run the following command.
```
githook_timesheet_weekly_report 2021-07-07
```
It will find all items in the week starting on the Monday of the supplied date.
