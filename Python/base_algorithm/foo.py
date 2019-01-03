# coding: utf-8

__author__ = "lau.wenbo"


def foo(tom):
    fred = 0
    for bill in range(1, tom + 1):
        barney = bill
        fred = fred + barney
    return fred

print(foo(100))