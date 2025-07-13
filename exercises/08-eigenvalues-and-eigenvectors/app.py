import numpy as np  

def compute_eigen(A, mode="numpy"):
    """
    Computes the eigenvalues and eigenvectors of a square matrix.

    Parameters:
    - A: list of lists or np.array -> Square matrix.
    - mode: str -> "pure" for manual calculation, "numpy" for np.linalg.eig().

    Returns:
    - List of eigenvalues (and eigenvectors if mode="numpy").
    """
   
   
    autovalores, autovectores = np.linalg.eig(A)


def compute_eigen(A, mode="pure"):
    a, b = A[0]
    c, d = A[1]

    # Resolvemos det(A - λI) = 0
    lambda1 = ((a + d) + ((a + d)**2 - 4*(a*d - b*c))**0.5) / 2
    lambda2 = ((a + d) - ((a + d)**2 - 4*(a*d - b*c))**0.5) / 2

    return [lambda1, lambda2]
    




A = [[3, 2], [1, 4]]
compute_eigen(A, "pure")
compute_eigen(A, "numpy")