import math

file = open('input.txt', 'r')

elements = file.readlines()
fuelTotal = 0

def calcFuel(elementSize):
    fuelForElement = math.floor(int(elementSize)/3) - 2

    return fuelForElement

for element in elements:
    fuelForElement = calcFuel(element)
    while True:
        if fuelForElement > 0:
            fuelTotal = fuelTotal + fuelForElement
            fuelForElement = calcFuel(fuelForElement)
        else:
            break

print(fuelTotal)