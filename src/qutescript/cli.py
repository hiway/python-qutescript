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

import click
import os


# ---

# script_cli_parser = argparse.ArgumentParser(description='Qutebrowser userscript.')
# script_cli_parser.add_argument('--install', action='store_true', help='Setup permissions and show install
# instructions.')

class NoSubCommands(Exception):
    pass


@click.group(invoke_without_command=True)
@click.pass_context
def userscript(ctx):
    """
    Qutebrowser Userscript
    """
    if ctx.invoked_subcommand is None:
        raise NoSubCommands()


@userscript.command(name='install')
def userscript_install():
    from .installer import install
    userscript_path = os.path.abspath(sys.argv[0])
    path = os.path.abspath(userscript_path)
    name = os.path.basename(userscript_path)
    click.echo_via_pager(install(path, name=name))
    sys.exit(0)
