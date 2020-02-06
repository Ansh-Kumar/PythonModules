import time

#Brute Force Bubble Sort

def swapPos(lstS, pos1, pos2):
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


def bruteBubble(lst):
    print(lst)
    isWorking = False
    while isWorking == False:
        for i in range(len(lst)):
            if (i == 0):
                continue
            elif (lst[i-1] > lst[i]):
                swapPos(lst, i, i-1)
        print(lst)
        isWorking = checkList(lst)
    print(lst)

lst = [3, 2, 5, 1]
bruteBubble(lst)
