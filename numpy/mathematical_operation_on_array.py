"""mathematical operation on array"""
import numpy as np

# mathematical operation between arrays vs list
'''
list1=[1,2,3,4]
list2=[6,7,8,9]

array1 = np.array(list1)
array2 = np.array(list2)




print(list1 + list2)
# [1, 2, 3, 4, 6, 7, 8, 9]

print(array1 + array2)
# [ 7  9 11 13]


# print(list1 * list2)
# TypeError: can't multiply sequence by non-int of type 'list'

print(array1 * array2)
# [ 6 14 24 36]

# print(list1 - list2)
# TypeError: unsupported operand type(s) for -: 'list' and 'list'

print(array1 - array2)
# [-5 -5 -5 -5]

# print(list1 / list2)
# TypeError: unsupported operand type(s) for /: 'list' and 'list'

print(array1 / array2)
# [0.16666667 0.28571429 0.375      0.44444444]
'''



# matric operations 
'''
a1 = np.array([1,2,3])
a2 = np.array([[1],[2]])

print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)

print(np.sqrt(a1))
'''


