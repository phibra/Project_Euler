a, b = 0, 1
count = 0
length = 1000

while (a / 10**(length-1) <= 1):        
    a, b = b, a + b
    count += 1

print(count)
