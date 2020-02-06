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
