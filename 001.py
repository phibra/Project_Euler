a, b = 0, 1
sum = 0

while (b < 1000):
    if (b % 3 == 0) or (b % 5 == 0):
        sum += a
        
    a, b = b, a + b
    
print(sum)
