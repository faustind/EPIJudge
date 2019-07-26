import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    count_a = 0
    count_b = 0
    for _, c in zip(range(size), s):
        if c == 'a':
            count_a += 1
        elif c == 'b':
            count_b += 1

    resize = size - count_b + count_a

    write_pos = resize - 1
    for c in reversed(s[:size]):
        if c == 'a':
            s[write_pos-1] = s[write_pos] = 'd'
            write_pos -= 2
        elif c != 'b':
            s[write_pos] = c
            write_pos -= 1

    return resize


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
