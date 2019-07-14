from test_framework import generic_test


def plus_one(A):
    for i in reversed(range(len(A))):
        if A[i] + 1 < 10:
            A[i] += 1
            break
        if i == 0:
            A[i] = 1
            A.append(0)
        else:
            A[i] = 0
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
