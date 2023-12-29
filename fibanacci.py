# fibanacci series of any number that a user might need

def fib(n):
    a=0
    b=1

    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

n=int(input("Enter the number to obtain fibonaccii: "))
fib(n)