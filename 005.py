#Returns True if even divisible through 1 - 20
def checkDivisors(input):
    for i in range(20, 2, -1):
        if (input % i != 0):
            return False 
    return True


cont = True
curVal = 0

while (cont == True):
    curVal += 1    
    
    if checkDivisors(curVal):
        cont = False
    
print(curVal)   #232792560
