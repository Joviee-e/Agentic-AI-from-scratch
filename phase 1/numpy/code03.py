#shapes 

import numpy as np

arr = np.array([
    [1 , 2],
    [3 , 4]]
)

print(arr.shape)

#Zero matrix
print(np.zeros((3,3)))

#Similarly

print(np.ones((2,2)))

#Printing number directly in a range of choice 

print(np.arange(1,11))

#statistics
arr1 = np.array([10, 20, 30, 40])
print(int(arr1.mean()))

print(arr1.max())

print(arr1.min())

print(arr1.sum())