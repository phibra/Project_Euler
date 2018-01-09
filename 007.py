def isPrime(value):
    counter = 3
    
    if value <= 1:
        return False
    if value == 2:
        return True
    
    # Remove now to save the steps later
    if value % 2 == 0:
        return False
    
    while counter <= (value // 2 ) + 1:
        if value % counter == 0:
            return False
        else:
            counter += 2
        
    return True


counter = 1
curVal = 1

while (counter < 10001):
    curVal += 2
    if isPrime(curVal):
        counter += 1
        
print(curVal)
