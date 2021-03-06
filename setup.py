import setuptools

setuptools.setup(
    name="githook-timesheet",
    version="1.1.3",
    author="Jason Bouchard",
    author_email="jay@dypabo.com",
    description="",
    install_requires=[],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "githook_timesheet_task = githook_timesheet.cli.task:main",
            "githook_timesheet_post_commit = githook_timesheet.cli.post_commit:main",
            "githook_timesheet_weekly_report = githook_timesheet.cli.timesheet_report:main",
        ]
    },
    python_requires=">=3.6",
)
