input = 600851475143
i = 2

while input > i:
    if input % i == 0:
        input /= i
        i = 2
    else:
        i += 1
    
print(i)
