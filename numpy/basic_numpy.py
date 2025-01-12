import numpy as np


'''1d array'''
a=np.array([1,2,3,4,5])

# print(a)
# print(type(a))


''' 
cause error because inconsistency in the shape of the elements causes the ValueError.

a_mul = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [4, 5, 6]
])
'''


''' multidimentional array'''
a_mul = np.array([
    [[1, 2, 3]],
    [[4, 5, 6]],
    [[1, 2, 3]],
    [[4, 5, 6]]
])

# print(a_mul)

# print(a_mul[0,1])

# print(a_mul.shape)

# print(a_mul.ndim)

# print(a_mul.size)

# print(a_mul.dtype)


''' multidimentional array with multiple data type '''
a= np.array([[1,2,3],
             [1,"hello",3]])

print(a.dtype)



