import random, time, os

class Snail:
    def __init__(self, MaxSpeed: int, Name: str):
        self.MaxSpeed = MaxSpeed
        self.Name = Name
        self.Distance = 0

    def Crawl(self):
        self.Distance += (random.random() * self.MaxSpeed) # Float between 0 and 1

    def PrintDistanceBar(self):
        Block = int(self.Distance) // 10 # One block of = is 10 millimeters
        for X in range(Block):
            print("=", end="")
        
        print("")
        return ""

class Race:
    def __init__(self, MaxContestants: int, Distance: int):
        self.MaxContestants = MaxContestants
        self.Contestants = []
        self.Distance = Distance # Distance in millimeters
        self.Finished = False
        self.Winner = None

    def AddSnail(self, MaxSpeed: int, Name: str):
        if len(self.Contestants) != self.MaxContestants:
            self.Contestants.append(Snail(MaxSpeed, Name))
        else:
            print("Max contestants reached")

    def IsFinished(self):
        return self.Finished

    def GetWinner(self):
        return self.Winner

    def Crawl(self):
        for X in range(len(self.Contestants)):
            self.Contestants[X].Crawl()
            if self.Contestants[X].Distance >= self.Distance:
                self.Finished = True
                self.Winner = self.Contestants[X].Name

    def Run(self):
        while self.IsFinished() != True:
            for X in range(len(self.Contestants)):
                self.Crawl()
                print(X + 1, self.Contestants[X].Name)
                print(self.Contestants[X].PrintDistanceBar(), end="")

            time.sleep(1)
            if self.IsFinished() != True:
                os.system("clear")

        print("==> Winner is", self.GetWinner() + "!")

Race = Race(10, 200)
Race.AddSnail(6, "Jeff")
Race.AddSnail(7, "Mia")
Race.AddSnail(2, "Michael")
Race.AddSnail(9, "Raphael")
Race.AddSnail(1, "Emilia")
Race.AddSnail(4, "Moritz")
Race.AddSnail(4, "Max")
Race.AddSnail(3, "David")
Race.AddSnail(5, "Claudia")
Race.AddSnail(8, "Luna")
Race.Run()