#!/usr/bin/env python
# coding=utf-8
import subprocess

from qutescript import userscript
from qutescript.cli import parser

parser.add_argument('-c',
                    action='store',
                    help='Command to execute.',
                    default='')
parser.add_argument('--insert',
                    action='store_true',
                    help='Type output into current tab?',
                    default=False)


@userscript
def shell_command(request):
    args = parser.parse_args()
    if not args.c:
        request.send_text("Please specify a command: {} -c'uname -a' ".format(request.script_name))
        return
    r = subprocess.check_output(args=args.c, shell=True)
    text = str(r, 'utf-8').strip()
    if args.insert:
        request.send_command('insert-text {}'.format(text))
    else:
        request.send_text(text)


if __name__ == '__main__':
    shell_command()
