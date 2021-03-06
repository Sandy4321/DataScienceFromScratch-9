def shape(matrix): return len(matrix), len(matrix[0])


def get_row(matrix, row_idx): return matrix[row_idx]


def get_col(matrix, col_idx): return [matrix[row_idx][col_idx] for row_idx in matrix]


def make_matrix(num_of_rows, num_of_cols, generate_elem):
    return [[generate_elem(row_idx, col_idx) for col_idx in range(num_of_cols)] for row_idx in range(num_of_rows)]


def is_identity_elem(row_idx, col_idx): return 1 if row_idx == col_idx else 0


def main():
    example_matrix = [[1, 2, 3], [4, 5, 6]]
    print(shape(example_matrix))

    num_of_rows, num_of_cols = 5, 5
    identity_matrix = make_matrix(num_of_rows, num_of_cols, is_identity_elem)
    print(identity_matrix)


if __name__ == '__main__':
    main()
