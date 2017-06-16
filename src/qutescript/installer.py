# coding=utf-8
import sys

import os
import stat

REVIEW_TEMPLATE = """\
Qutebrowser userscript {name!r} was installed at:
 
    {userscripts_path!r}

You can try it out by running the command:

    :spawn --userscript {name}

"""

LOADER_TEMPLATE = """\
#!/usr/bin/env bash
{interpreter}"{path}" "$@"
"""


def setup_permissions(path):
    file_stat = os.stat(path)
    os.chmod(path, file_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def get_interpreter():
    interpreter = sys.executable
    if interpreter.startswith('/usr') or interpreter.startswith('/opt'):
        interpreter = ''
    else:
        interpreter = interpreter + ' '
    return interpreter


def link_to_qutebrowser_userscripts_directory(path, name):
    import appdirs
    appdir = appdirs.user_data_dir('qutebrowser', 'qutebrowser')
    userscripts_dir = os.path.join(appdir, 'userscripts')
    userscripts_path = os.path.join(userscripts_dir, name)
    interpreter = get_interpreter()
    if not os.path.exists(userscripts_dir):
        os.makedirs(userscripts_dir, exist_ok=False)
    with open(userscripts_path, 'w') as bin_file:
        bin_file.write(LOADER_TEMPLATE.format(
            interpreter=interpreter,
            path=path,
        ))
    setup_permissions(userscripts_path)
    return userscripts_path


def install(path, name=None):
    """
    Sets permissions for qutescript at path and returns
    instructons and commands to integrate with qutebrowser.
    """
    path = os.path.abspath(os.path.expanduser(path))
    name = name or os.path.basename(path)
    interpreter = get_interpreter()
    setup_permissions(path)
    userscripts_path = link_to_qutebrowser_userscripts_directory(path, name)
    return REVIEW_TEMPLATE.format(userscripts_path=userscripts_path, name=name, interpreter=interpreter)
