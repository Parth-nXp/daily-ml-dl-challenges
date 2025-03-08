import numpy as np

def numpy_indexing_slicing():
    array = np.random.randint(10, 99, size=(4,4))
    extracted_slices  = {
                        'First Row': array[0,:].tolist(),
                        'Last Column': array[:,-1].tolist(),
                        'Center 2x2 Submatrix': array[1:-1,1:-1].tolist() 
    }
    return sliced_arrays


results = numpy_indexing_slicing()
print(results)