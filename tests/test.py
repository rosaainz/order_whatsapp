import unittest
from order_whatsPython.lib.main import main

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


