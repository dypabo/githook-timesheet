from argparse import ArgumentParser
from os import environ


def add_optional_arg_if_env_var_exists(
    parser: ArgumentParser,
    argument_name: str,
    env_var_name: str,
    help_str: str,
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
    parser.add_argument(argument_name, **optional_args, help=help_str)


def default_args_parser(app_description: str) -> ArgumentParser:
    """the base argument parser for all command line utilities in this packages"""
    parser = ArgumentParser(app_description)
    add_optional_arg_if_env_var_exists(
        parser,
        "timesheet_basedirectory",
        "githook_timesheet_basedir",
        "Directory where timesheet are store",
    )
    return parser
