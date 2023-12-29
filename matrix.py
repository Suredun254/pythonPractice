# multidimensional array
from numpy import *

arr1 = array([
    [1, 2, 3, 4, 5,6],
    [45, 46, 47, 48,49,50]
])

print(arr1)

#print dimension of array
print(arr1.ndim)

# print shape of array
print(arr1.shape)

# convert a multidimensional array to a single dimensional array
arr2=arr1.flatten()
print(arr2)

# to convert a one dimensional to a multidimensional array
array3=arr2.reshape(2,2,3)
print(array3)

#===================== Matrices ======================#
m=matrix(arr1)
print(m)

# given a string
n=matrix('1 2 3 4;5 6 7 8')
print(n)

# to obtain diagonal elements
print(diag(m))

# multiplication of matrices
m1=matrix('1 2 3 ;6 7 8;4 5 10')
m2=matrix('11 12 14; 15 16 18;13 19 20')
m3=m1*m2
print(m3)