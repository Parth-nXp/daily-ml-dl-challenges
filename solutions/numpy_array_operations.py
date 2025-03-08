import numpy as np

arr = [1, 2, 3, 4, 5, 7, 8]

numpy_arr = np.array(arr)
print(numpy_arr, type(numpy_arr))


sum_array = np.sum(numpy_arr)
mean_array = np.mean(numpy_arr)
std_array = np.std(numpy_arr)

print(sum_array, mean_array, std_array)