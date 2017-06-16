"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mqutescript` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``qutescript.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``qutescript.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse

import os
import sys

parser = argparse.ArgumentParser(description='Command description.')
parser.add_argument('names', metavar='NAME', nargs=argparse.ZERO_OR_MORE,
                    help="A name of something.")


def main(args=None):
    args = parser.parse_args(args=args)
    print(args.names)


# ---

script_cli_parser = argparse.ArgumentParser(description='Qutebrowser userscript.')
script_cli_parser.add_argument('--install', action='store_true', help='Setup permissions and show install instructions.')


def script_cli(args=None):
    args = script_cli_parser.parse_args(args=args)
    if not args.install:
        return
    from .installer import install
    userscript_path = os.path.abspath(sys.argv[0])
    path = os.path.abspath(userscript_path)
    name = os.path.basename(userscript_path)
    print(install(path, name=name))
    sys.exit(0)
