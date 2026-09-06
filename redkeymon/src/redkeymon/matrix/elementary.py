import torch


def rowSwap(matrix, source, target):
    result = matrix.clone()
    result[[source, target]] = result[[target, source]]
    return result


def rowScale(matrix, row, factor):
    result = matrix.clone()
    result[row] = result[row] * factor
    return result


def rowReplacement(matrix, row1, row2, j, k):
    result = matrix.clone()
    scaled_row1 = rowScale(result, row1, j)[row1]
    result[row1] = scaled_row1 + k * result[row2]
    return result


def rref(matrix, tol=1e-10):
    result = matrix.clone().to(torch.float64)
    n_rows, n_cols = result.shape
    pivot_row = 0

    for col in range(n_cols):
        if pivot_row >= n_rows:
            break

        pivot = None
        for r in range(pivot_row, n_rows):
            if abs(result[r, col].item()) > tol:
                pivot = r
                break

        if pivot is None:
            continue

        if pivot != pivot_row:
            result = rowSwap(result, pivot, pivot_row)

        result = rowScale(result, pivot_row, 1.0 / result[pivot_row, col].item())

        for r in range(n_rows):
            if r != pivot_row and abs(result[r, col].item()) > tol:
                factor = -result[r, col].item()
                result = rowReplacement(result, r, pivot_row, 1.0, factor)

        pivot_row += 1

    return result


if __name__ == "__main__":
    test_matrix = torch.tensor([[1., 3., 0., 0., 3.],
                                 [0., 0., 1., 0., 9.],
                                 [0., 0., 0., 1., -4.]])

    print("Original matrix:")
    print(test_matrix)

    step1 = rowSwap(test_matrix, 0, 1)
    print("\nAfter R1 <-> R2:")
    print(step1)

    step2 = rowScale(step1, 0, 1 / 3)
    print("\nAfter (1/3)R1:")
    print(step2)

    step3 = rowReplacement(step2, 2, 0, 1, -3)
    print("\nAfter R3 = -3R1 + R3:")
    print(step3)

    print("\nFull RREF of the original test matrix:")
    print(rref(test_matrix))
