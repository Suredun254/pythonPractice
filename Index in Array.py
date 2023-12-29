from array import *
arr=array('i',[])
n=int(input('Enter Lenth of array: '))

for i in range(n):
    x=int(input('enter a value: '))
    arr.append(x)
print(arr)

val=int(input('enter a value to search: '))
k=0

for e in arr:
    if val==e:
        print(k)
        break
    k+=1