"""hello world module"""


def hello(who):
    """function that greats"""

    text = "hello "

    try:
        with open('../hello.txt') as f:
            text = f.read()
    except FileNotFoundError:
        pass

    return text + who
