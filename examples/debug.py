#!/usr/bin/env python3.6
# coding=utf-8
import json

from qutescript import userscript
from qutescript.cli import parser


class KaboomError(Exception):
    pass


parser.add_argument('--kaboom', action='store_true', help='Make things explode.')


@userscript
def dump_to_log(request):
    args = parser.parse_args()
    if args.kaboom:
        raise KaboomError('Oh noes!')
    with open('qutescript.debug.log', 'a') as logfile:
        line = json.dumps(request.dump())
        logfile.writelines([line])


if __name__ == '__main__':
    dump_to_log()
