from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    res = []
    sign = 1
    if x < 0:
        x, sign = abs(x), -1
    while x:
        res.append(chr(x % 10 + ord('0')))
        x //= 10
    result = ''.join(reversed(res)) if res else '0'
    return '-' + result if sign < 0 else result


def string_to_int(s):
    res = 0
    sign, start = (-1, 1) if s[0] == '-' else (1, 0)
    for d in s[start:]:
        res = res * 10 + (ord(d) - ord('0'))
    return sign * res


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
