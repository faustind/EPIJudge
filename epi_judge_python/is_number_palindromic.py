from test_framework import generic_test

from reverse_digits import reverse


def is_palindrome_number(x):
    if x <= 0:
        return x == 0
    return x == reverse(x)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
