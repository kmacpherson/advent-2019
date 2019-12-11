file = open('input.txt', 'r')

inputCodes = file.readline().split(',')

def processCode(codeIndex):
    result = 0
    if (inputCodes[codeIndex] == '1'):
        result = int(inputCodes[int(inputCodes[codeIndex+1])]) + int(inputCodes[int(inputCodes[codeIndex+2])])
        inputCodes[int(inputCodes[codeIndex+3])] = str(result)
        processCode(codeIndex+4)
    elif (inputCodes[codeIndex] == '2'):
        result = int(inputCodes[int(inputCodes[codeIndex+1])]) * int(inputCodes[int(inputCodes[codeIndex+2])])
        inputCodes[int(inputCodes[codeIndex+3])] = str(result)
        processCode(codeIndex+4)
    elif (inputCodes[codeIndex] == '99'):
        print(inputCodes[0])
    else:
        print(f"Error invalid code at position {codeIndex}: {inputCodes[codeIndex]}")

processCode(0)