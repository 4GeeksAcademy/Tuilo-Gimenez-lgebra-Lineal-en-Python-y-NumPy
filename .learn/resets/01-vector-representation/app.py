import numpy as np  # Import NumPy to use it later

def create_vector(lst, mode="pure"):
    """
    Converts a list into a vector in pure Python or in NumPy.

    Parameters:
    - lst: list -> List of numbers that will form the vector.
    - mode: str -> "pure" for normal list, "numpy" for NumPy array.

    Returns:
    - A vector in the specified format.
    """
    pass # Remove this line when implemented
    

# Test the function with the following values:
vector1 = create_vector([1, 2, 3], "pure")
vector2 = create_vector([1, 2, 3], "numpy")

print("Vector in pure Python:", vector1)
print("Vector in NumPy:", vector2)
