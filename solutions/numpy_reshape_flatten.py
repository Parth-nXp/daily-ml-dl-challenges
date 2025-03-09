import numpy as np

def numpy_reshape_flatten():
    A = np.random.randint(10, 99, size= (4,4))
    A_reshape = np.reshape(A, (2,-1))
    A_flatten = A.ravel()
    result = {
            "Original Matrix": A.tolist(),
            "Reshaped (2,8) Matrix": A_reshape.tolist(),
            "Flattened 1D Array": A_flatten.tolist()
        }
    
    return result


result = numpy_reshape_flatten()
print(result)