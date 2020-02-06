import time
# Insertion

lst = [3, 2, 5, 1]


def swapPos(lstS, pos1, pos2):
    print("swapPos has entered the arena")
    lstS[pos1], lstS[pos2] = lstS[pos2], lstS[pos1]
    return lstS


def checkList(lst):
    for x in range(len(lst)):
        if (x+1 < len(lst)):
            if lst[x] < lst[x+1]:
                continue
            else:
                return False
    return True

def insertionTD(lst, n):
    if (n <= 0):
        return
    else:
        print("-------",lst[n-1])
        insertionTD(lst, n-1)

    j = n-1
    print("j: ", j, 'n:', n)
    while j >= 0 and lst[j] > lst[j+1]:
        print(lst)
        print(lst[j])
        print(lst[j+1])
        print(j, j+1)
        swapPos(lst, j, j+1)
        print(lst)
        j -= 1
#insertionTD([3, 2, 5, 1], 3)

def insertionBU(lst, n):
    if (n <= 0):
        return
    else:
        print("--------", lst[n-1])
        insertionBU(lst, n-1)
    nth = lst[n]
    j = n-1
    while (j >= 0) and (lst[j] > nth):
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = nth
    print(lst)
    return
    
insertionBU(lst, len(lst)-1)

