# coding=utf-8

import sys
import traceback

import os
from .cli import script_cli

from .request import build_request

log_file_path = './qutescript.log'


def write_log(message, file_path=None):
    print('***', message)
    file_path = file_path or log_file_path
    file_path = os.path.abspath(os.path.expanduser(file_path))
    record = [message, '\n', '\n']
    with open(file_path, 'a') as logfile:
        logfile.writelines(record)


def qutescript(func):
    def wrapper():
        script_cli(args=sys.argv[1:])
        try:
            request = build_request()
        except Exception as e:
            write_log(traceback.format_exc())
            write_log('Cannot build request.')
            sys.exit(1)
        try:
            command = func(request)
            if not command:
                return
        except Exception as e:
            write_log(traceback.format_exc())
            write_log('Userscript error.')
            sys.exit(2)
        if not request.fifo:
            write_log('ERROR: userscript returned command: {}, '
                      'but QUTE_FIFO was not found in passed environment.\n'
                      'Try: :spawn --userscript /path/to/script ?')
            sys.exit(3)
        try:
            with open(request.fifo, 'w') as fifo:
                fifo.write('{}\n'.format(command))
        except Exception as e:
            write_log(traceback.format_exc())
            write_log('Cannot write to FIFO: {!r}'.format(request.fifo))
            sys.exit(4)
    return wrapper
