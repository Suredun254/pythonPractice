# decorators are used inadding exra features in exisitng fuctions

def div(a, b):
    print(a / b)


def new_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div = new_div(div)

div(2, 4)
