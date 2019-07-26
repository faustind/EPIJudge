from test_framework import generic_test


def convert_base(num_as_string, b1, b2):
    int_mapped = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    sign, n = 1, 0
    for d, i in zip(reversed(num_as_string), range(len(num_as_string))):
        if d == '-':
            sign = -1
            continue
        n += int(d, base=b1) * b1 ** i

    q, r = divmod(n, b2)
    res = []
    while q >= b2:
        res.append(int_mapped.get(r, str(r)))
        q, r = divmod(q, b2)
    res.append(int_mapped.get(r, str(r)))
    res.append(int_mapped.get(q, str(q)))

    if res[-1] == '0':
        del(res[-1])

    return ('-' if sign < 0 else '') + ''.join(reversed(res))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
