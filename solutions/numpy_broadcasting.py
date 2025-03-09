import numpy as np

def numpy_broadcasting():
    A = np.random.randint(1, 50, size=(3,3))
    B = np.random.randint(1, 10, size=(1,3))
    result = {
        "Original Matrix": A.tolist(),
        "1D Array": B.tolist(),
        "Results after Broadcasting": (A + B).tolist()
    }

    return result


result = numpy_broadcasting()
print(result)