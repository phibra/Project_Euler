MAX = 2000000

if MAX % 2 == 0: 
    MAX += 1
    
numbers = [True] * MAX
numbers[0],numbers[1] = [False] * 2
sum = 0

for i,val in enumerate(numbers):
    if val is True and i > MAX ** 0.5 + 1:
        sum += i
    elif val is True:         
        numbers[i*2::i] = [False] * (((MAX - 1)//i) - 1)
        sum += i

print(sum)
