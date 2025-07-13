import numpy as np

# vectors and matrices
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

def dot_product(v1, v2, mode="pure"):
    """
    Computes the dot product of two vectors.

    Parameters:
    - v1: list or np.array -> First vector.
    - v2: list or np.array -> Second vector.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - The dot product as a scalar value.
    """

    pass  # Remove this line when implemented

def matrix_product(A, B, mode="pure"):
    """
    Computes the product of two matrices.

    Parameters:
    - A: list of lists or np.array -> First matrix.
    - B: list of lists or np.array -> Second matrix.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - A matrix with the result of A * B.
    """
    pass  # Remove this line when implemented


dot_result_pure = dot_product(vector1, vector2, "pure")
dot_result_numpy = dot_product(vector1, vector2, "numpy")


matrix_result_pure = matrix_product(matrix1, matrix2, "pure")
matrix_result_numpy = matrix_product(matrix1, matrix2, "numpy")

print("Dot product in pure Python:", dot_result_pure)
print("Dot product in NumPy:", dot_result_numpy)
print("Matrix product in pure Python:", matrix_result_pure)
print("Matrix product in NumPy:", matrix_result_numpy)
