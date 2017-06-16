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
import sys
import argparse

import os

# ---

parser = argparse.ArgumentParser(description='Qutebrowser userscript.')
parser.add_argument('--install', action='store_true',
                    help='Setup permissions and show install instructions.')


class NoSubCommands(Exception):
    pass


def main_cli():
    """
    Qutebrowser Userscript
    """
    args = parser.parse_args()
    if not args.install:
        return
    main_install()


def main_install():
    from .installer import install
    userscript_path = os.path.abspath(sys.argv[0])
    path = os.path.abspath(userscript_path)
    name = os.path.basename(userscript_path)
    print(install(path, name=name))
    sys.exit(0)


def userscript_cli(func):
    def wrapper(request):
        return func(request)

    return wrapper
