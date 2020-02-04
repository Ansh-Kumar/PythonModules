# SieveOfEratosthenes
import time


def sieveOfEratosthenes(n):
    startTime = time.time()
    notPrimeList = []
    primeList =[]
    for x in range(2, n+1):
        if x not in notPrimeList:
            primeList.append(x)
            for i in range(x*x, n+1, x):
                notPrimeList.append(i)
    elapsedTime = round(time.time() - startTime, 2)
    print(primeList)
    print(elapsedTime)
    
sieveOfEratosthenes()
