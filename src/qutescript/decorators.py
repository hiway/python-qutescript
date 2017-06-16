# coding=utf-8

import sys

import os

from .request import build_request

log_file_path = './qutescript.log'


def write_log(message, file_path=None):
    file_path = file_path or log_file_path
    file_path = os.path.abspath(os.path.expanduser(file_path))
    with open(file_path, 'a') as logfile:
        logfile.writelines([message])


def qutescript(func):
    def wrapper():
        request = build_request()
        command = func(request)
        if not command:
            return
        if not request.fifo:
            write_log('ERROR: userscript returned command: {}, '
                      'but QUTE_FIFO was not found in passed environment.\n'
                      'Try: :spawn --userscript /path/to/script ?')
            sys.exit(1)
        with open(request.fifo, 'w') as fifo:
            fifo.write('{}\n'.format(command))

    return wrapper
