import numpy as np

def matrix_operations(A, B):
    # Convert lists to NumPy arrays
    A = np.array(A)
    B = np.array(B)


    # Compute transpose of A
    A_tranpose = np.transpose(A)
    
    
    # Compute dot product if valid
    if A.shape[1] == B.shape[0]:
        dot_product = np.dot(A, B)
    else:
        dot_product = "Invalid dimensions"
    
    return A_tranpose, dot_product


A = [[1, 2], [3, 4]]

B = [[5, 6], [7, 8]]

results = matrix_operations(A, B)
print(results)