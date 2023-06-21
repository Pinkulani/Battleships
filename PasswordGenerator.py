from random import randint

print("Password Generator \n", "Passwords will generate like this XXXXX-XXXXX-XXXXX \n", "With random letters (upper and lowercase) and numbers")

Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def PassArray():
    L = []
    for i in range (0,5):
        character = randint(0, 1)

        
        match character:
            case 0:
                number = randint(0, 9)
                L.append(number)
            case 1:
                letter = randint(0, 25)
                L.append(Letters[letter])
    
    return L



characters1 = PassArray()
characters2 = PassArray()
characters3 = PassArray()

print(characters1, "-", characters2, "-", characters3)


