class Car:
    def __init__(self,make,model,year,millage, price) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.millage = millage
        self.price = price
    def display_details(self):
        return f"{self.year} {self.make} {self.model} - {self.millage} miles - ${self.price}"
    

