# factorial using recursion

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


n = int(input('Enter to find factorial : '))

result = fact(n)

print('Factorial of {} is {}'.format(n,result))
