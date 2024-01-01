# Lambdas
# Use of function only once so not a msut of defining it
# examole to find square of a number

# defining a function

def x(n):
    return n * n


# use of lambda

x = lambda n: n * n

n = int(input('Enter n: '))
result = x(n)

print('The square of {} is {}'.format(n, result))
