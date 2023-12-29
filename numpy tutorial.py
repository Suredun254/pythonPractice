from numpy import *
arr=array([1,2,3,4,5])
print(arr)
print(arr.dtype)

arr1=linspace(0,10,4)
print(arr1)

arr3=logspace(1,2,5)
print(arr3)
# difference between values is of log though w have five steps

# to print  5 zeros
arr4=zeros(5)
print(arr4)

# to print  5 ones
arr5=ones(5)
print(arr5)

arr6=array([1,2,3,4,5,6])
arr6+=5
print(arr6)

# to join two arrays
print(concatenate([arr,arr6]))

# copying array without use of function
arr2=arr1

# Shallow copy-> copying an array but them remaining linked
arr7=array([21,22,23,24,25])
arr8=arr7.view()
print(arr8)

# Deep copy -> arrays not linked to each other
arr9=array([31,32,33,34,35])
arr10=arr9.copy()
print(arr10)