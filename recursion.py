# recursion/ calling function from itself

# example
def greet():
    print('hello')
    greet()


greet()

# to check and increase recursion limit

import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(2000)

i = 0


def greet():
    global i
    i += i
    print('hello')
    greet()
greet()


greet()
