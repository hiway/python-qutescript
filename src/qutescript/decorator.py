# coding=utf-8

import sys
import traceback

import os
from qutescript.utils import send_messages_to_browser

from .cli import main_cli, userscript_cli
from .request import build_request


def qutescript(func):
    def wrapper():
        userscript_name = os.path.basename(sys.argv[0])
        try:
            main_cli()
        except Exception as e:
            send_messages_to_browser(traceback.format_exc(), 'Cannot execute cli handler', script_name=userscript_name)
            sys.exit(1)
        try:
            request = build_request()
        except Exception as e:
            send_messages_to_browser(traceback.format_exc(), 'Cannot build request.', script_name=userscript_name)
            sys.exit(5)
        try:
            func_ = userscript_cli(func)
            command = func_(request)
            if not command:
                return
        except Exception as e:
            send_messages_to_browser(traceback.format_exc(), 'Userscript error.', script_name=userscript_name)
            sys.exit(10)
        if not request.fifo:
            message = ('ERROR: userscript returned command: {}, '
                       'but QUTE_FIFO was not found in passed environment.\n'
                       'Try: :spawn --userscript /path/to/script ?')
            send_messages_to_browser(traceback.format_exc(), message, script_name=userscript_name)
            sys.exit(20)
        try:
            with open(request.fifo, 'w') as fifo:
                fifo.write('{}\n'.format(command))
        except Exception as e:
            send_messages_to_browser(
                traceback.format_exc(),
                'Cannot write to FIFO: {!r}'.format(request.fifo), script_name=userscript_name)
            sys.exit(30)

    return wrapper
