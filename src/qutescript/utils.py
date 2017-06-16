#!/usr/bin/env python
# coding=utf-8
import os
import tempfile

log_file_path = './qutescript.log'


def write_log(message, file_path=None):
    print('***', message)
    file_path = file_path or log_file_path
    file_path = os.path.abspath(os.path.expanduser(file_path))
    record = ['***' + message, '\n', '\n']
    with open(file_path, 'a') as logfile:
        logfile.writelines(record)


def send_messages_to_browser(*messages):
    """
    Write messages to a temporary file,
    Attempt to open the file through FIFO in the browser.
    """
    [write_log(msg) for msg in messages]
    fifo = os.getenv('QUTE_FIFO')
    if not fifo:
        return
    out_lines = ['<html><body><pre>'] + ['<p>{}</p>'.format(m or '&nbsp;') for m in messages]
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as trace_file:
        trace_file.writelines(out_lines)
        print('***', trace_file.name)
        with open(fifo, 'w') as fifo_file:
            fifo_file.write('open -t file://{}'.format(
                os.path.abspath(trace_file.name)))
