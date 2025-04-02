import numpy as np


def numpy_stack_concatenate():
    np.random.seed(42)
    mat_A = np.random.randint(1, 50, size = (3,3))
    mat_B = np.random.randint(1, 50, size = (3,3))

    h_stack = np.hstack((mat_A, mat_B))
    v_stack = np.vstack((mat_A, mat_B))

    concat_axis_0 = np.concatenate((mat_A, mat_B), axis = 0)
    concat_axis_1 = np.concatenate((mat_A, mat_B), axis = 1)

    results = {
        "Matrix A": mat_A,
        "Matrix B": mat_B,
        "Stacked Vertically": v_stack,
        "Stacked Horizontally": h_stack,
        "Concatenated along axis=0": concat_axis_0,
        "Concatenated along axis=1": concat_axis_1
    }
    return results



print(numpy_stack_concatenate())