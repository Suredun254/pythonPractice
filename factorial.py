# finding the factorial of a number

def fact(n):
    x = 1
    for i in range(1, n + 1):
        x = x * i
    return x


n = int(input('Enter a number to determine the factorial: '))
result = fact(n)

print(result)
