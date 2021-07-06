import setuptools

setuptools.setup(
    name="githook-timesheet",
    version="0.1.0",
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
            "githook_timesheet = githook_timesheet.cli:main",
        ]
    },
    python_requires=">=3.6",
)
