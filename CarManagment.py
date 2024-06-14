class Car:
    def __init__(self,make,model,year,mileage, price) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
    def display_details(self):
        return f"{self.year} {self.make} {self.model} - {self.mileage} miles - ${self.price}"
    

class CarManagementSystem:
    def __init__(self) -> None:
        self.cars = []
    def new_car(self, car):
        self.cars.append(car)
    def updateexistingcar(self, make, model, **kwargs):
            for car in self.cars:
                if car.make == make and car.model == model:
                    car.year = kwargs.get('year', car.year)
                    car.mileage = kwargs.get('mileage', car.mileage)
                    car.price = kwargs.get('price', car.price)
                return True
            return False
    def deletecar(self):
        pass
    def displayallcars(self):
        print([car.display_details() for car in self.cars])   
    def savecarstofile(self):
        pass
    def loadcarsfromfile(self):
        pass

def main():
    cms = CarManagementSystem()
    while True:
        print("\nCar Management System")
        print("1. Add new car")
        print("2. Update car details")
        print("3. Delete a car")
        print("4. Display all cars")
        print("5. Save to file")
        print("6. Load from file")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = int(input("Enter car year: "))
            mileage = int(input("Enter car mileage: "))
            price = float(input("Enter car price: "))
            car = Car(make, model, year, mileage, price)
            cms.new_car(car)
            print("Car added successfully.")

        if choice == "2":
            make = input("Enter car make to update: ")
            model = input("Enter car model to update: ")
            year = int(input("Enter new year (or press enter to skip): ") or 0)
            mileage = int(input("Enter new mileage (or press enter to skip): ") or 0)
            price = float(input("Enter new price (or press enter to skip): ") or 0.0)
            updated = cms.updateexistingcar(make, model, year=year, mileage=mileage, price=price)
            if updated:
                print("Car details updated successfully.")
            else:
                print("Car not found.")

        
        if choice == '4':
            cars = cms.displayallcars()
            if cars:
                for car in cars:
                    print(car)
        
        if choice == '7':
            break


main()