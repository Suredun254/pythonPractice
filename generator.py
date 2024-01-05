def square():
    n = 1
    while n <= 10:
        sq = n ** 2
        yield sq
        n += 1


values = square()

for i in values:
    print(i)
