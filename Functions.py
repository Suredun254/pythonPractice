# def greet():
#     print('Hello')
#     print('good morning')
#
# # greet()

def add_sub(x, y):
    c = x + y
    d = y - x
    return c, d


result1, result2 = add_sub(4, 5)
print(result1, result2)


# types of arguments--->Formal and actual elements
def add1(a, *b):
    c = a
    for i in b:
        c += i

    print(c)


add1(2, 3, 4, 5)
