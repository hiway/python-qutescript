#!/usr/bin/env python
# coding=utf-8
import os
import tempfile

HTML_TEMPLATE = """\
"""

log_file_path = './qutescript.log'


def write_log(message, file_path=None, console=False):
    if console:
        print('***', message)
    file_path = file_path or log_file_path
    file_path = os.path.abspath(os.path.expanduser(file_path))
    with open(file_path, 'a') as logfile:
        logfile.write('*** {}\n\n'.format(message))


def normalize_prefix(prefix):
    if prefix:
        prefix = prefix.replace('.', '_')
        if not prefix.endswith('_'):
            prefix = prefix + '_'
    return prefix


def log_to_browser(*messages, prefix: str = None, console=True):
    """
    Write messages to logs and a temporary file,
    Attempt to open the file through FIFO in the browser.
    """
    [write_log(msg, console=console) for msg in messages]
    send_to_browser('\n'.join(messages), prefix=prefix)


def send_to_browser(text, prefix: str = None):
    fifo = os.getenv('QUTE_FIFO')
    if not fifo:
        return

    prefix = normalize_prefix(prefix)
    prefix = 'qutescript_{}'.format((prefix or ''))
    with tempfile.NamedTemporaryFile(mode='w', prefix=prefix, suffix='.html', delete=False) as out_file:
        out_file.writelines(HTML_TEMPLATE.format(text))
        with open(fifo, 'w') as fifo_file:
            fifo_file.write('open -t file://{}'.format(
                os.path.abspath(out_file.name)))
