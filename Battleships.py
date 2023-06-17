import random
import sys

# Functions
def draw(list):
    for z in list:
        for sp in z:
            print(sp, end='\t')
        print()

# 2D array (a = hidden field) (b = game field)
n = 10
m = 10
a = [0] * n
for i in range(n):
    a[i] = [0] * m

b = [0] * n
for e in range(n):
    b[e] = ['X'] * m

# Random ship placement
for i in range(0,10):
    r = random.randint(0,9)
    a[i][r] = 1

# !!! START !!!
print("|- Battleships -|")
print("Conditions: ")
print("The ships are all 1 space big")
print("Row and line input cannot be greater than 10")
end = 0

while True:

    draw(b)

    # Shooting
    line = int(input("Which line? "))
    row = int(input("Which row? "))

    if line > 10 or row > 10:
        print("Numbers out of bounds")
        continue
    

    field = a[line-1][row-1]
    print(field)

    # Hit detection
    if field == 1:
        print("You hit a Ship!1!11!11! WOOOOO")
        b[line-1][row-1] = 1
        end += 1
    else:
        print("No ship = big sad :'((")
        b[line-1][row-1] = 0

    #Game end
    if end == 10:
        print("You won!")
        break



