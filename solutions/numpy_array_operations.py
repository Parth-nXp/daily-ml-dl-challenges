import numpy as np

def array_stats(arr):
    numpy_array = np.array(arr)
    sum_array = np.sum(numpy_array)
    mean_array = np.mean(numpy_array)
    std_array = np.std(numpy_array)

    return sum_array, mean_array, std_array



arr = [1, 2, 3, 4, 5, 6, 7, 8]
results = array_stats(arr)
print(results)
    
