pos = -1


def search(list, n):
    lower = 0
    upper = len(list) - 1

    while lower <= upper:
        mid = (lower + upper) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                lower = mid
            else:
                upper = mid


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = 8

if search(list, n):
    print('Found at', pos)

else:
    print('Not Found')
