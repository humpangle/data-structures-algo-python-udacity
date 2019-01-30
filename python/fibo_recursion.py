"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""


def get_fib1(pos):
    if pos < 0:
        return -1
    if pos == 0:
        return 0
    a, b = 0, 1
    while pos >= 1:
        a, b = b, a+b
        pos -= 1
    return a


def get_fib(pos):
    if pos < 0:
        return -1
    if pos == 0 or pos == 1:
        return pos
    return get_fib(pos-1) + get_fib(pos-2)
