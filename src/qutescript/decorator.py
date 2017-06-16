# coding=utf-8

import sys
import traceback

import tempfile
import os

from .cli import NoSubCommands, userscript
from .request import build_request

log_file_path = './qutescript.log'


def write_log(message, file_path=None):
    print('***', message)
    file_path = file_path or log_file_path
    file_path = os.path.abspath(os.path.expanduser(file_path))
    record = ['***' + message, '\n', '\n']
    with open(file_path, 'a') as logfile:
        logfile.writelines(record)


def send_traceback_to_browser(trace, *messages):
    """
    Write trace and messages to a temporary file,
    Attempt to open the file through FIFO in the browser.
    """
    write_log(trace)
    [write_log(msg) for msg in messages]
    fifo = os.getenv('QUTE_FIFO')
    out_lines = ['<html><body><pre>', trace] + ['<p>{}</p>'.format(m or '&nbsp;') for m in messages]
    if not fifo:
        return
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as trace_file:
        trace_file.writelines(out_lines)
        print('***', trace_file.name)
        with open(fifo, 'w') as fifo_file:
            fifo_file.write('open -t file://{}'.format(
                os.path.abspath(trace_file.name)))


def qutescript(func):
    def wrapper():
        try:
            userscript()
        except NoSubCommands as e:
            pass
        except Exception as e:
            send_traceback_to_browser(traceback.format_exc(), 'Cannot execute cli handler')
            sys.exit(1)
        try:
            request = build_request()
        except Exception as e:
            send_traceback_to_browser(traceback.format_exc(), 'Cannot build request.')
            sys.exit(5)
        try:
            command = func(request)
            if not command:
                return
        except Exception as e:
            send_traceback_to_browser(traceback.format_exc(), 'Userscript error.')
            sys.exit(10)
        if not request.fifo:
            message = ('ERROR: userscript returned command: {}, '
                       'but QUTE_FIFO was not found in passed environment.\n'
                       'Try: :spawn --userscript /path/to/script ?')
            send_traceback_to_browser(traceback.format_exc(), message)
            sys.exit(20)
        try:
            with open(request.fifo, 'w') as fifo:
                fifo.write('{}\n'.format(command))
        except Exception as e:
            send_traceback_to_browser(
                traceback.format_exc(),
                'Cannot write to FIFO: {!r}'.format(request.fifo))
            sys.exit(30)

    return wrapper
