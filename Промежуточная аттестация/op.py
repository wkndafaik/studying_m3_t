# op.py

def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    return a/b
