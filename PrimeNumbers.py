# Emilia @ 5.7.23

from math import sqrt

def CheckPrime(Number):
        Prime = True
        for i in range(2, int(sqrt(Number))):
            if (Number % i) == 0:
                Prime = False
                break

        if Prime == True:
            print(Number, "is a prime number")
        #else:
            #print(Number, "is not a prime number")
    
# Start   
for i in range(2, 10000000 + 1):
    CheckPrime(i)
