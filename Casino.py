from tkinter import *

# Tkinter Cheatsheet

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.title("Casino")
        self.Window.geometry("630x430")

        # Background
        self.Background = LabelFrame(self.Window, bg = 'hot pink')
        self.Background.place(x = 0, y  = 0, width = 630, height = 430)
        
        Text = ["Bets", "Winnings", "Game", "Results"]
        self.LabelFrame = [0, 0, 0, 0]
        for C in range(0,4):
            match C:
                case 0:
                    DistanceX = 10
                    DistanceY = 10
                    
                case 1:
                    DistanceX = 320
                    DistanceY = 10
     
                case 2:
                    DistanceX = 10
                    DistanceY = 220
         
                case 3:
                    DistanceX = 320
                    DistanceY = 220

                case _:
                    print("???")
                    
            self.LabelFrame[C] = LabelFrame(self.Window, text = Text[C], bg = 'deep pink')
            self.LabelFrame[C].place(x = DistanceX, y = DistanceY, width = 300, height = 200)

        self.Button = [0, 0, 0]
        for M in range(0,3):
            self.Button[M] = Button(self.LabelFrame[0], text='Count',command=lambda:self.Action('count'))
            self.Button[M].place(x = (20 * M), y = 10, width = 50, height = 20)

        mainloop()

    def Action(self, Act):
        hi = 0
        
            
class Bank:
    def __init__(self):
        self.Bank = 1000
        self.Player = 50

    def Pay(self, Recipient, Amount):
        match Recipient:
            case "Bank":
                self.Bank += Amount

            case "Player":
                self.Player += Amount

        
class Casino(object):
    def __init__(self):
        GUI()
        Bank()

if __name__ == '__main__':
    App = Casino()
