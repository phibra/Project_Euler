sum1 = 0
sum2 = 0

for i in range(1, 101, 1):
    sum1 += i ** 2
    
for j in range(1, 101, 1):
    sum2 += j

sum2 = sum2 ** 2

print(sum2 - sum1)
