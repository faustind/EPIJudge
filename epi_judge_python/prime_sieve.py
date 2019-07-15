from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    # TODO - you fill in here.
    if n < 2:
        return []
    is_prime = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            for j in range( 2 * i, n + 1, i):
                is_prime[j] = False
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
