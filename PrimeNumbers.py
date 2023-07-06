# Emilia @ 5.7.23

def CheckPrime(Number):
        Prime = True
        for i in range(2, Number):
            if (Number % i) == 0:
                Prime = False
                break

        if Prime == True:
            print(Number, "is a prime number")
        #else:
            #print(Number, "is not a prime number")
    
# Start   
for i in range(2, 1000 + 1):
    CheckPrime(i)