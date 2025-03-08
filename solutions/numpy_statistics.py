import numpy as np

def numpy_statistics(size):
    array= np.random.randint(1,100, size=(size,size))
    array_stats = {
                    'Min': np.min(array),
                    'Max': np.max(array),
                    'Mean': np.mean(array),
                    'Standard Deviation': np.mean(array)
                }
    return array, array_stats


array, results = numpy_statistics(5)
print("Generated Array:\n", array)
print("Statistics:\n", results)