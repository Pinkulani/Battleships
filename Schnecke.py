import random, time, os

class Schnecke:
    def __init__(self, MaxGeschwindigkeit: int, Name: str):
        self.MaxGeschwindigkeit = MaxGeschwindigkeit
        self.Name = Name
        self.Strecke = 0

    def Kriechen(self):
        self.Strecke += (random.random() * self.MaxGeschwindigkeit) # Float zwischen 0 und 1

    def GetStreckenMarker(self):
        Block = int(self.Strecke) // 10 # Ein Block "=" ist 10 Millimeter
        for X in range(Block):
            print("=", end="")
        
        print("")
        return ""

class SchneckenRennen:
    def __init__(self, MaxTeilnehmer: int, Strecke: int):
        self.MaxTeilnehmer = MaxTeilnehmer
        self.Teilnehmer = []
        self.Strecke = Strecke # Strecke in Millimeter
        self.Beendet = False
        self.Sieger = None

    def AddSchnecke(self, MaxGeschwindigkeit: int, Name: str):
        if len(self.Teilnehmer) != self.MaxTeilnehmer:
            self.Teilnehmer.append(Schnecke(MaxGeschwindigkeit, Name))
        else:
            print("Maximale Teilnehmer erreicht!")

    def IstBeendet(self):
        return self.Beendet

    def GetSieger(self):
        return self.Sieger

    def Weiterkriechen(self):
        for X in range(len(self.Teilnehmer)):
            self.Teilnehmer[X].Kriechen()
            if self.Teilnehmer[X].Strecke >= self.Strecke:
                self.Beendet = True
                self.Sieger = self.Teilnehmer[X].Name

    def Slow(self):
        while self.Beendet != True:
            for X in range(len(self.Teilnehmer)):
                self.Weiterkriechen()
                print(X + 1, self.Teilnehmer[X].Name)
                print(self.Teilnehmer[X].GetStreckenMarker(), end="")
            
            time.sleep(1)
            if self.Beendet != True:
                os.system("clear")
        
        print("==> Sieger ist", self.Sieger + "!")
            
R = SchneckenRennen(10, 200)
R.AddSchnecke(6, "Jeff")
R.AddSchnecke(7, "Mia")
R.AddSchnecke(2, "Michael")
R.AddSchnecke(9, "Raphael")
R.AddSchnecke(1, "Emilia")
R.AddSchnecke(4, "Moritz")
R.AddSchnecke(4, "Max")
R.AddSchnecke(3, "David")
R.AddSchnecke(5, "Claudia")
R.AddSchnecke(8, "Luna")
R.Slow()