# List
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
my_list.append(6)
print("Updated List:", my_list)

# Tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
# my_tuple[0] = 10  # This will raise an error since tuples are immutable

# Array using array module
import array as arr
my_array = arr.array('i', [1, 2, 3, 4, 5])
print("Array using array module:", my_array)
my_array.append(6)
print("Updated Array using array module:", my_array)

# Array using numpy
import numpy as np
my_numpy_array = np.array([1, 2, 3, 4, 5])
print("Array using numpy:", my_numpy_array)
my_numpy_array = np.append(my_numpy_array, 6)
print("Updated Array using numpy:", my_numpy_array)
