pos = -1


def search(list, n):
    i = 0

    # while i < len(list):
    #     if list[i] == n:
    #         globals()['pos']=i
    #         return True
    #     i += 1
    # return False

    for i in list:
        if list[i] == n:
            globals()['pos'] = i
            return True

    return False


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = 8

if search(list, n):
    print('Found at', pos)

else:
    print('Not Found')
