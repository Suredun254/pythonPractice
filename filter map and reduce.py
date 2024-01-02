# filter , map and reduce functions

# they all take the format of:

#           function(function, sequence)

# note the use of lambda function

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# filter

odd_nums = list(filter(lambda x: x % 2 != 0, nums))

print(odd_nums)

# map

squares = list(map(lambda x: x ** 2, nums))

print(squares)

# reduce

from functools import reduce

sum = reduce(lambda a, b: a + b, nums)

print(sum)
