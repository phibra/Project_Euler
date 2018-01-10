#Sieve of Eratosthenes
# Very Inefficient!

MAX = 2000001

numbers = list(range(2, MAX, 1))
primesVal = 0
count = 0


while(len(numbers) > 0):    
    numbers = sorted(numbers)    
    temp = numbers[0]
    primesVal += numbers[0]
    del numbers[0]
    
    multiples = list(range(temp*temp, MAX, temp))
    numbers = list(set(numbers).difference(set(multiples)))
    
    #Debugging
    count += 1
    if (count % 250 == 0):        
       print("Numbers ", len(numbers))

print(primesVal)
