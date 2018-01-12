sequenceMax = 0
sequenceMaxLength = 0

for i in range(2,1000000,1):
    sequenceLength = 1
    sequence = i
    
    while sequence > 1:
        sequenceLength += 1
        if sequence % 2 == 0:
            sequence = sequence / 2
        else:
            sequence = 3 * sequence + 1
    
    if sequenceLength > sequenceMaxLength:
        sequenceMax = i
        sequenceMaxLength = sequenceLength
        
print("Sequence: ", sequenceMax, " - Length: ", sequenceMaxLength)
