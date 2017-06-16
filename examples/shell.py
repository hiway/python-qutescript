#!/usr/bin/env python
# coding=utf-8
import subprocess

from qutescript import userscript
from qutescript.cli import parser

parser.add_argument('-c',
                    action='store',
                    help='Command to execute.',
                    default='')


@userscript
def shell_command(request):
    args = parser.parse_args()
    if not args.c:
        request.send_text("Please specify a command: {} -c'uname -a' ".format(request.script_name))
        return
    r = subprocess.check_output(args=args.c.split(' '))
    request.send_text(r)


if __name__ == '__main__':
    shell_command()
