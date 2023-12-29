# keyworded variable length arguments or **kwargs

def person(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i ,":", j)

person('sure', age=21, year='5th year', lang='python')
