from test_framework import generic_test


def reverse(x):
    res, sign = 0, 1
    if x < 0:
        x, sign = -x, -1
    while x:
        res = res * 10 + x % 10
        x = x // 10
    return sign * res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
