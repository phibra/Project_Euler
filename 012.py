def primeListLen(end):
    list = []
    
    if end < 2: 
        return 0
    if end == 2: 
        return 2
    if end % 2 == 0: 
        end += 1
    
    numbers = [True] * end
    numbers[0],numbers[1] = [False] * 2
    sum = 0

    for i,val in enumerate(numbers):
        if val is True and i > end ** 0.5 + 1:
            list.append(i)
        elif val is True:         
            numbers[i*2::i] = [False] * (((end - 1)//i) - 1)
            list.append(i)

    return((int(len(list)) + 2)

def triangleNumber(n):
    value = 0
    numbers = list(range(1,1000,1)) 
    
    for i in range(0,n,1):
        value += numbers[i]
    
    return value
    

len = 0
counter = 0
    
while len < 500:
    counter += 1
    len = primeListLen(triangleNumber(counter))

print(triangleNumber(counter))    
