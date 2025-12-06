#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        prin('a')
    except NameError:
        raise NameError(message)
