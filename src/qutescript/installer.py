# coding=utf-8
import sys

import os
import stat

TEMPLATE = """\
Qutebrowser userscript {name!r} was installed at:
 
    {path}

You can try it out by running the command:

    :spawn --userscript {interpreter}{path}
"""


def setup_permissions(path):
    file_stat = os.stat(path)
    os.chmod(path, file_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def install(path, name=None):
    """
    Sets permissions for qutescript at path and returns
    instructons and commands to integrate with qutebrowser.
    """
    path = os.path.abspath(os.path.expanduser(path))
    name = name or os.path.basename(path)
    interpreter = sys.executable
    if interpreter.startswith('/usr') or interpreter.startswith('/opt'):
        interpreter = ''
    else:
        interpreter = interpreter + ' '
    setup_permissions(path)

    return TEMPLATE.format(path=path, name=name, interpreter=interpreter)
