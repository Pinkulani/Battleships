from random import randint

bubblelist = []

for x in range(0,1000):
    x = randint(1,100)
    bubblelist.append(x)

unsorted = bubblelist

print("List: ")
print("")
print(bubblelist)

    
for i in range(len(bubblelist)):
    for b in range(len(bubblelist)-1-i):
        if bubblelist[b] > bubblelist[b+1]:
            bubblelist[b],bubblelist[b+1] = bubblelist[b+1], bubblelist[b]
            
            
print("Sorted List: ", bubblelist)
