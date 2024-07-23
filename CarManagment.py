import json

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
    def update_existing_car(self, make, model, **kwargs):
            for car in self.cars:
                if car.make == make and car.model == model:
                    car.year = kwargs.get('year', car.year)
                    car.mileage = kwargs.get('mileage', car.mileage)
                    car.price = kwargs.get('price', car.price)
                return True
            return False
    def delete_car(self, make, model):
         for car in self.cars:
            if car.make == make and car.model == model:
                self.cars.remove(car)
            return True
         return False

    def display_all_cars(self):
        print([car.display_details() for car in self.cars])   
    def save_cars_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([car.__dict__ for car in self.cars], file)
    def load_cars_from_file(self):
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
            updated = cms.update_existing_car(make, model, year=year, mileage=mileage, price=price)
            if updated:
                print("Car details updated successfully.")
            else:
                print("Car not found.")
        if choice == "3":
            make = input("Enter car make to delete: ")
            model = input("Enter car model to delete: ")
            deleted = cms.delete_car(make,model)
            if deleted:
                print("Car details deleted successfully.")
            else:
                print("Car not found.")

        if choice == '4':
            cars = cms.display_all_cars()
            if cars:
                for car in cars:
                    print(car)
        if choice == "5":
            filename = input("Enter filename to save to (e.g., cars.json): ")
            cms.save_cars_to_file(filename)
            print("Car details saved successfully.")

        if choice == "6":
            pass
        
        if choice == '7':
            break


main()