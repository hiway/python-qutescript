========
Overview
========


Painless userscripts for qutebrowser.

* Free software: BSD license

Status
======

Very alpha, "works for me" on MacOS Sierra with Python 3.6;
if you like what you see, please test it on your platform
and help by submitting pull-requests if your current skills
allow.


Installation
============

::

    git clone https://github.com/hiway/python-qutescript.git qutescript
    cd qutescript
    pip install -e .


Usage
=====

::

    #!/usr/bin/env python

    from qutescript import userscript


    @userscript
    def hello_world(request):
        request.send_text('Hello, world!')


    if __name__ == '__main__':
        hello_world()


