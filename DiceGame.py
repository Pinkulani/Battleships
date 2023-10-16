import random

class Dice(object):
    def __init__(self):
        self.Number = 0

    def GenerateNumber(self):
        self.Number = random.randint(0,6)

    def GetNumber(self):
        return self.Number

    def PrintNumber(self):
        print("Number: ", self.Number)

class Bankaccount(object):
    def __init__(self):
        self.Money = 10
        self.Winnings = 0

    def Profit(self, Hits):
        self.Money -= 1 # Bet
        if Hits > 0:
            self.Money += Hits
            self.Winnings = Hits
        else:
            self.Winnings = 0

    def Status(self):
        print("Bankaccount: ", self.Money)
        print("Last Winnings: ", self.Winnings)

    def Broke(self):
        if self.Money <= 0:
            return True
        else:
            return False
        
class Board(object):
    def __init__(self):
        self.Tip = -1

    def Tipping(self):
        Input = int(input("Your guess: "))
        if Input < 0 and Input > 6:
            print("It's a 6 sided dice!")
        else:
            self.Tip = Input
    
    def GetTip(self):
        return self.Tip

WU = []
for Name in ["Dice1", "Dice2", "Dice3"]:
        Object = Dice()
        Object.Name = Name
        WU.append(Object)
        
Bankaccount = Bankaccount()
Board = Board()

Gameend = False
while Gameend == False:
    Hits = 0
    Gameend = Bankaccount.Broke()
    Bankaccount.Status()
    Board.Tipping()
    for X in range(0, 3):
        WU[X].GenerateNumber()
        WU[X].PrintNumber()

    Tip = Board.GetTip()
    for X in range(0, 3):
        Numbered = WU[X].GetNumber()
        if Numbered == Tip:
            Hits += 1

    Bankaccount.Profit(Hits) # Total Winnings

print("Game ended!")