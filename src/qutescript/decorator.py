# coding=utf-8

import sys
import traceback

import os

from qutescript.utils import log_to_browser
from .cli import main_cli
from .request import build_request


def userscript(func):
    def wrapper():
        """
        Wraps a qutebrowser-userscript in a warm blanket
        of easy to access parameters and a sprinkling
        of debugging goodness.
        """
        script_path = sys.argv[0]
        prefix = os.path.basename(script_path)  # example: my_script.py
        try:
            # Check if "--install" was passed, and handle it.
            main_cli()
        except Exception as e:
            log_to_browser(traceback.format_exc(),
                           'Cannot execute cli handler',
                           prefix=prefix,
                           script_path=script_path)
            sys.exit(1)
        # main_cli() may call sys.exit() if --install was passed at command line.
        # If sys.exit() was called by main_cli(), we would never reach here.
        # Since ^that^ did not happen...
        try:
            request = build_request()
        except Exception as e:
            log_to_browser(traceback.format_exc(),
                           'Cannot build request.',
                           prefix=prefix,
                           script_path=script_path)
            sys.exit(5)
        # We now have a request to handle.
        try:
            # Wrapper for future use; disabled for now.
            # func = userscript_cli(func)
            command = func(request)
            if not command:
                # No command to execute, our work is done.
                return
        except Exception as e:
            log_to_browser(traceback.format_exc(),
                           'Userscript error.',
                           prefix=prefix,
                           script_path=script_path)
            sys.exit(10)
        # We also have a command to execute.
        if not request.fifo:
            message = ('ERROR: userscript returned command: {}, '
                       'but QUTE_FIFO was not found in passed environment.\n'
                       'Try: :spawn --userscript /path/to/script ?')
            log_to_browser(traceback.format_exc(),
                           message,
                           prefix=prefix,
                           script_path=script_path)
            sys.exit(20)
        try:
            # Send the returned command to qutebrowser.
            with open(request.fifo, 'w') as fifo:
                fifo.write('{}\n'.format(command))
        except Exception as e:
            log_to_browser(
                traceback.format_exc(),
                'Cannot write to FIFO: {!r}'.format(request.fifo),
                prefix=prefix,
                script_path=script_path)
            sys.exit(30)

    return wrapper
