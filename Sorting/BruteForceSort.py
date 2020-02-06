import time
import random
# Brute Force


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





def bruteForce(lst):
    counter = 0
    position = 0
    isWorking = False
    while isWorking == False:
        for x in range(len(lst)):
            if (x == counter):
                minVal = lst[counter]
            elif (x < counter):
                continue
            elif lst[x] < minVal:
                minVal = lst[x]
                position = x
            elif x == len(lst):
                break
        swapPos(lst, counter, position)
        position = counter + 1
        counter += 1
        isWorking = checkList(lst)
    print(lst)
lst = [36, 148, 80, 65, 99, 17, 138, 149, 96, 176, 150, 146, 187, 75, 195, 58, 160, 67, 7, 179, 38, 42, 105, 22, 117, 142, 159, 164, 143, 97, 116, 37, 125, 14, 113, 78, 172, 45, 89, 84, 151, 104, 23, 1, 165, 18, 35, 32, 173, 30]
lstA = [65, 152, 89, 15, 142, 44, 122, 21, 51, 8, 179, 78, 53, 57, 157, 160, 119, 91, 177, 39, 106, 11, 118, 159, 170, 109, 98, 33, 10, 191, 22, 107, 144, 32, 64, 184, 55, 183, 108, 198, 143, 199, 97, 100, 131, 9, 37, 90, 137, 156]
lstB = [103, 43, 161, 10, 148, 19, 74, 117, 21, 142, 138, 55, 58, 28, 172, 173, 166, 133, 20, 102, 50, 105, 80, 159, 141, 146, 34, 77, 115, 82, 144, 65, 104, 101, 13, 109, 86, 171, 75, 143, 87, 180, 192, 130, 44, 25, 11, 124, 84, 15]
lstC = [100, 164, 177, 1, 20, 15, 118, 155, 174, 146, 69, 188, 6, 94, 200, 138, 169, 31, 187, 143, 133, 4, 24, 195, 51, 49, 95, 11, 80, 194, 70, 184, 103, 137, 111, 175, 93, 19, 41, 181, 54, 59, 191, 193, 166, 105, 199, 13, 65, 157]


print(lst)
startTime = time.time()
bruteForce(lst)
bruteForce(lstA)
bruteForce(lstB)
bruteForce(lstC)
print(time.time() - startTime)
