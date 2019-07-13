from test_framework import generic_test


def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


def bf_reverse(x, length):
    shift_width = length // 2
    for j, pos_i in enumerate(range(shift_width)):
        pos_j = length - pos_i - 1
        x = swap_bits(x, pos_i, pos_j)
    return x

pre = [bf_reverse(x, 16) for x in range(2 ** 16)]

def reverse_bits(x):
    mask_size = 16
    bit_mask = 0xFFFF
    return (pre[x & bit_mask] << (3 * mask_size) |
            pre[(x >> mask_size) & bit_mask] << (2 * mask_size) |
            pre[(x >> (2 * mask_size)) & bit_mask] << mask_size |
            pre[(x >> (3 * mask_size)) & bit_mask])



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
