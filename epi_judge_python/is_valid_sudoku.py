from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    def has_duplicate(array):
        target = [x for x in array if x != 0]
        return len(target) != len(set(target))

    # check for rows and cols
    for i in range(9):
        if has_duplicate(partial_assignment[i]) or \
           has_duplicate([partial_assignment[j][i] for j in range(9)]):
            return False

    # check for square regions
    for i in range(3):
        for j in range(3):
            if has_duplicate([partial_assignment[a][b] \
                             for a in range(3*i, 3*(i+1)) \
                             for b in range(3*j, 3*(j+1))]):
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
