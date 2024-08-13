import json
import psycopg2
import sys
from datetime import datetime

# Database connection details
dbname = 'CarManagment'
user = 'postgres'
password = 'flipper'
host = 'localhost'
port = '5432'

# Database Connection Action
connection = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

# Create a cursor object to interact with the database
cursor = connection.cursor()



class Car:
    def __init__(self,id,make,model,year,mileage, price) -> None:
        self.id = id
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
    
    # Logic to Add new Cars within the DataBase
    def new_car(self, make, model, year, mileage, price):
        cursor.execute("""
                    INSERT INTO cars (make, model, year, mileage, price)
                    VALUES (%s, %s, %s, %s, %s)
                """, (make, model, year, mileage, price))
        connection.commit()
        cursor.close

    # Logic to Update Cars within the DataBase
    def update_existing_car(self, id, **kwargs):
        # Build the SET clause dynamically based on provided kwargs
        update_fields = []
        update_values = []
        
        if 'make' in kwargs and kwargs['make']:
            update_fields.append("make = %s")
            update_values.append(kwargs['make'])
            
        if 'model' in kwargs and kwargs['model']:
            update_fields.append("model = %s")
            update_values.append(kwargs['model'])
            
        if 'year' in kwargs and kwargs['year']:
            update_fields.append("year = %s")
            update_values.append(kwargs['year'])
            
        if 'mileage' in kwargs and kwargs['mileage']:
            update_fields.append("mileage = %s")
            update_values.append(kwargs['mileage'])
            
        if 'price' in kwargs and kwargs['price']:
            update_fields.append("price = %s")
            update_values.append(kwargs['price'])

        if update_fields:
            update_values.append(id)
            # Construct and execute the UPDATE query
            cursor.execute(f"""
                UPDATE cars
                SET {', '.join(update_fields)}
                WHERE id = %s
            """, update_values)
            connection.commit()
            return True
        return False

    # Logic to Delete existing Cars
    def delete_car(self, id):
        cursor.execute("""
                    DELETE FROM cars
                    WHERE id = %s
                """, (id,))
        connection.commit()
        
    # Logic to Display existing Cars
    def display_all_cars(self):
        cursor.execute("SELECT * FROM cars")
        car_items = cursor.fetchall()  # Corrected to call fetchall()
        for item in car_items:
            print(f"ID: {item[0]}, Make: {item[1]}, Model: {item[2]}, Year: {item[3]}, Miles: {item[4]}, Price: ${item[5]}")
    

def main():
    cms = CarManagementSystem()
    while True:
        print("\nCar Management System")
        print("1. Add new car")
        print("2. Update car details")
        print("3. Delete a car")
        print("4. Display all cars")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = int(input("Enter car year: "))
            mileage = int(input("Enter car mileage: "))
            price = float(input("Enter car price: "))
            cms.new_car(make, model, year, mileage, price)
            print("Car added successfully.")

        if choice == "2":
            id = input("Enter the ID you want to Update: ")
            make = input("Enter car make to update: ")
            model = input("Enter car model to update: ")
            year = int(input("Enter new year (or press enter to skip): ") or 0)
            mileage = int(input("Enter new mileage (or press enter to skip): ") or 0)
            price = float(input("Enter new price (or press enter to skip): ") or 0.0)
            updated = cms.update_existing_car(id, make=make, model=model, year=year, mileage=mileage, price=price)
            if updated:
                print("Car details updated successfully.")
            else:
                print("Car not found.")

        if choice == "3":
            id = int(input("Enter car ID to delete: "))
            cms.delete_car(id)
            print("Car details deleted successfully.")


        if choice == '4':
            cms.display_all_cars()
                
        if choice == '5':
            break


main()