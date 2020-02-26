import random
import time


def createRandomList(length):
    startTime = time.time()
    tempList = []
    for x in range(length):
        tempList.append(random.randint(0, 1000))
    elapsedTime = time.time() - startTime
    return [tempList, elapsedTime]