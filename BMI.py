class BMI(object):
    def __init__(self):
        self.Height = 0
        self.Weight = 0
        self.BMI = 0
        self.Name = "No Name"
        self.Category = "No category"
    
    def SetName(self, Name):
        self.Name = Name

    def SetHeight(self, Height):
        self.Height = Height

    def SetWeight(self, Weight):
        self.Weight = Weight

    def Test(self):
        self.Name = "Max"
        self.Height = 1.9
        self.Weight = 85

    def Calculate(self):
        self.BMI = self.Weight / self.Height ** 2

    def Evaluate(self):
        Marker = self.BMI # To type less
        # Source (https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html)
        if Marker < 18.5: 
            self.Category = "Underweight"
        elif Marker > 18.5 and Marker < 24.9:
            self.Category = "Healthy Weight"
        elif Marker > 25 and Marker < 29.9:
            self.Category = "Overweight"
        else:
            self.Category = "Obesity"
                
    def Diagnosis(self):
        print("• DIAGNOSIS •")
        print("* Your data: *")
        print("Your name: ", self.Name)
        print("Your height: ", self.Height)
        print("Your weight: ", self.Weight)
        print("• RESULT •")
        print("BMI: ", self.BMI)
        print("This puts you in the category of: ", self.Category)

BMI = BMI()

# Example
Test = False

if Test == True:
    BMI.Test()
else:
    Name = str(input("Your name: "))
    BMI.SetName(Name)
    Height = float(input("Your height (in Meters): "))
    BMI.SetHeight(Height)
    Weight = float(input("Your weight (in kg): "))
    BMI.SetWeight(Weight)

BMI.Calculate()
BMI.Evaluate()
BMI.Diagnosis()



