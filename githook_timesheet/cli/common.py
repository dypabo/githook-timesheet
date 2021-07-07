from argparse import ArgumentParser
from os import environ
from pathlib import Path
from typing import Optional, Type


def add_optional_arg_if_env_var_exists(
    parser: ArgumentParser,
    argument_name: str,
    env_var_name: str,
    help_str: str,
    cast_type: Optional[Type] = None,
) -> None:
    """
    add to `argument_name` to `parser`
    if `env_var_name` is in the environment variables,
    it makes the argumetn optional with the environment variable content as the argument default value
    """
    optional_args = {}
    if env_var_name in environ:
        optional_args["default"] = environ[env_var_name]
        optional_args["nargs"] = "?"
        if cast_type is not None:
            optional_args["type"] = cast_type
    parser.add_argument(argument_name, **optional_args, help=help_str)


def default_args_parser(app_description: str) -> ArgumentParser:
    """the base argument parser for all command line utilities in this packages"""
    parser = ArgumentParser(app_description)
    add_optional_arg_if_env_var_exists(
        parser,
        argument_name="--timesheet_basedirectory",
        env_var_name="githook_timesheet_basedir",
        help_str="Directory where timesheet are store",
        cast_type=Path,
    )
    return parser
