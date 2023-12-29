# Fetching user input
x=int(input('enter a number: '))
y=int(input('enter a number: '))
z=x+y
print(z)

# # input in char format
ch=input('Enter a char: ')
print(ch)

# to access a value in cmd
import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
z=x+y
print(z)


# x=int(input('enter a number : '))
# if(x==1):
#     print('one')
# elif(x==2):
#     print('two')
# else:
#     print('number not found')

# i=1
# while i<=5:
#     print('sure',end=" ")
#     j = 1
#     while j<=4:
#         print('task done',end=" ")
#         j+=1
#     i+=1
#     print()

# print all elements in a list
x=[1,2,3,4,5,6]
for i in x:
    print(i,end=',')
print()

#to print perfect squares btween 1 and 500
for n in range(1,500):
    x=n**2
    if x<= 501:
        print(x)

for i in range(1,100):
    if i%3==0 and i%5==0:
        continue
    print(i, end=' ')
print()

# print pattern in a 4 by 4 matrix

    for i in range(0, 5):
        print('#', end=' ')
    print()

# Prints pattern in ascending order the following will apply

for i in range(4):
    for j in range(i+1):
        print('#', end=' ')
    print()

# prints the format below
        #
        # #
        # # #
        # # # #

# to print in reverse order the following will apply

for i in range(4):
    for j in range(4-i):
        print('#', end=' ')
    print()
# prints the format below
            # # # #
            # # #
            # #

 ## for and else
nums=[12,15,17,18,33]
for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print('number not found')

