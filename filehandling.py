f = open('myCode', 'r')
f = open('myCode', 'w')
f.write('hello sure')

f1 = open('myCode', 'r')
print(f1.read())

f2 = open('myCode', 'a')
f2.write('welcome to coding')

f3 = open('myCode', 'r')
print(f3.readline())

f4 = open('newfile', 'w')

f5 = open('myCode', 'r')
for data in f5:
    print(data)
    f4.write(data)
