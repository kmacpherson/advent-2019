file = open('input.txt', 'r')

inputCodes = file.readline().split(',')

def processCode(codeIndex, codeList):
    result = 0
    if (codeList[codeIndex] == '1'):
        result = int(codeList[int(codeList[codeIndex+1])]) + int(codeList[int(codeList[codeIndex+2])])
        codeList[int(codeList[codeIndex+3])] = str(result)
        processCode(codeIndex+4, codeList)
    elif (inputCodes[codeIndex] == '2'):
        result = int(codeList[int(codeList[codeIndex+1])]) * int(codeList[int(codeList[codeIndex+2])])
        codeList[int(codeList[codeIndex+3])] = str(result)
        processCode(codeIndex+4, codeList)
    elif (codeList[codeIndex] == '99'):
        return codeList
    else:
        print(f"Error invalid code at position {codeIndex}: {codeList[codeIndex]}")

def checkCodes(codeList):
    iC = []
    for i, j in pairGenerator():
        del iC[:]
        iC = codeList.copy()
        iC[1] = str(i)
        iC[2] = str(j)
        processCode(0, iC)
        if (iC[0] == '19690720'):
            break
    print(str(100*int(iC[1]) + int(iC[2])))

def pairGenerator():
    for i in range(100):
        for j in range(100):
            yield i, j


checkCodes(inputCodes)