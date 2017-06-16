========
Overview
========


Painless userscripts for qutebrowser.

* Free software: BSD license

Installation
============

::

    git clone https://github.com/hiway/python-qutescript.git qutescript
    cd qutescript
    pip install -e .


Example
=======

::

    #!/usr/bin/env python

    from qutescript import userscript


    @userscript
    def hello_world(request):
        request.send_text('Hello, world!')


    if __name__ == '__main__':
        hello_world()


Tutorial
========

At the time of writing this, I know of qutebrowser for only two days.
That is a testament to how addictive this new keyboard-access browser
can be if you prefer that kind of a thing. If you haven't heard of it
yet, and you like vim and python - qutebrowser might be just for you.

It is a lightweight browser built on top of PyQt5 toolkit, works
with current Python (3.6.x) and has affinity for doing things the
unix way - clean, simple, no bullshit.

As with unix philosophy, it can pipe commands with webpage text,
current URL etc to your shell scripts or binaries, and can accept
commands through a temporary FIFO/pipe back to the browser.

The qutebrowser documentation can get you started:

https://github.com/qutebrowser/qutebrowser/blob/master/doc/userscripts.asciidoc

Although if you, like me are interested in writing custom userscripts
to automate tasks and kinda prefer Python to shell scripts, you will
need some boilerplate code that gets copy-pasted to every new userscript.

qutescript is an attempt at reducing that boilerplate, while also adding
a few helpful features for debugging the script directly from qutebrowser.
Get exception traceback for a failing script in a new tab instead of
switching to the terminal to check logs, you were logging to a file instead
of terminal, weren't you? ;)

Alright, enough talk... let's set this up!

1. Install qutebrowser:
    https://github.com/qutebrowser/qutebrowser

2. Clone qutescript:
    `git clone https://github.com/hiway/python-qutescript.git qutescript`

3. Install qutescript:
    `$ cd qutescript; pip install -e .`

4. Install an example or two:
    `$ python examples/debug.py --install --bin=debug`
    `$ python examples/shell.py --install --bin=shell`

5. Run qutebrowser and run:
    `:spawn --userscript debug --kaboom`

6. Create a new file:
    `vim my_hello.py`

::

    #!/usr/bin/env python
    # coding=utf-8

    from qutescript import userscript


    @userscript
    def hello_world(request):
        request.send_text('Hello, me! :P')


    if __name__ == '__main__':
        hello_world()

7. Install your script:
    `$ python examples/my_hello.py --install --bin=myhello`

8. Try it in qutebrowser:
    `:spawn --userscript myhello`

9. Continue reading the reference section for details.


Reference
=========

@userscript
-----------

This is a python decorator, it allows qutescript
to "wrap" your function with extra capabilities such as:

    - Inject "request" parameter in the wrapped function.
    - Access environment variables passed by qutebrowser
        as properties on request.
        example: `os.getenv('QUTE_URL', '')` maps to => `request.url`
    - Catch any exceptions and log them to file.
    - Also log exceptions to a new browser tab if possible.
    - Interact with the browser through request.send_text() etc.
    - Adds a shortcut: if your function returns a string,
        it is sent to the browser as a command.
    - Install the script to qutebrowser's application directory,
        so you can access the scripts without typing full
        absolute path every time. Remembers to change permissions.

request
-------

Your function will get an instance of Request() object which has
the following properties set from environment variables as defined
here:

https://github.com/qutebrowser/qutebrowser/blob/master/doc/userscripts.asciidoc

- `mode`
- `user_agent`
- `fifo`
- `html`
- `text`
- `config_dir`
- `data_dir`
- `download_dir`
- `commandline_text`
- `url`:
- `title`
- `selected_text`
- `selected_html`

Additional information is available on:

- `script_name`: Basename of the running script.
- `script_path`: Absolute path of the running script.

Request also defines a some utility methods:

- `as_dict()` returns the above properties as a dictionary.

You can interact with the browser with:

- `send_text(text)`: send pre-formatted text to new tab.
- `send_html(html)`: send raw html to new tab.
- `send_command(command)`: sends a command to the browser.

Remember to look at the examples directory for inspiration.


Status
======

Very alpha, "works for me" on MacOS Sierra with Python 3.6;
if you like what you see, please test it on your platform
and help by submitting pull-requests if your current skills
allow. This readme is all the documentation there is, apart
from the code and comments. Oh, and no tests so far…
however the code is written to be testable, it's a matter
of someone taking the effort ;)

Please open a new issue if you have questions.

Code of Conduct
===============

TL;DR:

Aggressive, hateful, derogatory or discriminatory
remarks will not be tolerated: contributions in code
are never more important than the well-being of our
communities. That said, it's great to be kind to one
another, whether writing code or not - let us all
try more of that? :D
