# fibonacci series of any number that a user might need
# checks if the number is negative
# Prints fibonacci series less than the number given
def fib(n):
    a = 0
    b = 1

    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c

        if c>=n:
           break
        print(c)


n = int(input("Enter the number to obtain fibonaccii: "))

if n<0:
    print('Please a value greater than 1')

else:
    print('Fibonacci Series less than {}'.format(n))
    fib(n)