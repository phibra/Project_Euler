import math as m

#Function to break the loops after the first match
def find():
    for a in range(1, 1000, 1):
        for b in range(1, 1000, 1):
            c = m.sqrt(a ** 2 + b ** 2)
            if (a + b + c == 1000):
                return int(a  * b * c)

                
print(find())
