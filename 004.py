def isPalindrome (input):    
    input = [int(i) for i in str(input)]
    length = int(len(input))
    
    if length % 2 == 0:
        part1 = (input[0: int(length / 2)])
        part2 = (input[int(length / 2):])
        part2 = list(reversed(part2))
    else:
        part1 = (input[0: int(length // 2)])
        part2 = (input[int(length // 2) + 1:])
        part2 = list(reversed(part2))

    return (part1 == part2)


curVal = 0    
maxVal = 0

for i in range(999, 0, -1):
    for j in range (999, 0, -1):
        curVal = i * j
        if (curVal > maxVal) and (isPalindrome(curVal)):
            maxVal = curVal

print(maxVal)
