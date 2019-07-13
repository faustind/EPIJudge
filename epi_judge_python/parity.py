from test_framework import generic_test


def bf_parity(x):
    parity = 0
    while x:
        parity ^= x & 1
        x >>= 1
    return parity

PRECOMPUTED_PARITY = [bf_parity(x) for x in range(2 ** 16)]

def parity(x):
    mask_size = 16
    bit_mask = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * mask_size)] ^
            PRECOMPUTED_PARITY[(x >> (2 * mask_size)) & bit_mask] ^
            PRECOMPUTED_PARITY[(x >> mask_size) & bit_mask] ^
            PRECOMPUTED_PARITY[x & bit_mask])


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
