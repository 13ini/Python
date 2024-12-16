class Car:
    def __init__(self, make, model, year, color, vin):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.vin = vin

car1 = Car(make="Toyota", model="Corolla", year=2020, color="Red", vin="123efr567")

print ("Make:", car1.make)
print("Model:", car1.model)
print("Year:", car1.year)
print("Color:", car1.color)
print("VIN:", car1.vin)


#printing bt function methods
class Car:
    def __init__(self, make, model, year, color, vin):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.vin = vin


    def print_details(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Color:", self.color)
        print("VIN:", self.vin)
        
car1 = Car(make="Toyota", model="Corolla", year=2020, color="Red", vin="123efr567")
car1.print_details()
