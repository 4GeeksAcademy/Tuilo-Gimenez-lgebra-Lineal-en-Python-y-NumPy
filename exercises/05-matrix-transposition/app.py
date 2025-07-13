import numpy as np  

def transpose(matrix, mode="pure"):
    """
    Computes the transpose of a matrix.

    Parameters:
    - matrix: list of lists or np.array -> Matrix to transpose.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - The transposed matrix.
    """
    A = [[1, 2, 3], [4, 5, 6]]
    pure = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    print(pure)



def transpose2(matrix, mode="numpy"):



    A1 = np.array([[1, 2, 3], [4, 5, 6]])
    numpy = A1.T
    print(numpy)


matrix = [[1, 2, 3], [4, 5, 6]]

transpose(matrix, "pure")
transpose(matrix, "numpy")