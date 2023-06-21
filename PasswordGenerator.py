from random import randint

print("Password Generator \n", "Passwords will generate like this XXXXX-XXXXX-XXXXX \n", "With random letters (upper and lowercase) and numbers \n")

Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def PassArray(): # Return Array length 5 with randomness applied
    L = []
    for i in range (0,5):
        character = randint(0, 1) # Choose letter/number

        match character:
            case 0:
                number = randint(0, 9)
                L.append(number)
            case 1:
                letter = randint(0, 25)
                shift = randint(0, 1) # Choose upper/lowercase
                
                if shift == 0:
                    L.append(Letters[letter])
                else:
                    L.append(Letters[letter].lower())
    
    return L

characters1 = PassArray()
characters2 = PassArray()
characters3 = PassArray()

print("Password: \n", *characters1, "-", *characters2, "-", *characters3)



