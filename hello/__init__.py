"""hello world module"""

import sys

def hello(who):
    """function that greats"""

    text = "hello "

    try:
        with open('../hello.txt') as f:
            text = f.read()
    except FileNotFoundError:
        pass

    print(f"/path/file.ext:123: warning: {text + who}\n", file=sys.stdout)
    print(f"/path/file.ext:321: warning: {text + who}\n", file=sys.stderr)

    return text + who
