# global and local variables

a = 10


def output():
    a = 9
    print('local variable : ', a)


output()

print("global variable : ", a)


# changing the local variable and using it outside function scope

def output1():
    global a
    a = 9
    print('local variable : ', a)


output1()

print("global variable : ", a)


# changing the global variable from within the function scope using globals()[]
def output2():
    a = 9
    print('local variable : ', a)
    x=globals()['a']
    print('within function value is', x)
    globals()['a']=20


output2()

print("global variable : ", a)
