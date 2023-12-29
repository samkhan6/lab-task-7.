class Car:
    def __init__(self, car_id, brand, model, year, is_available=True):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.is_available = is_available

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} (ID: {self.car_id})"

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def __str__(self):
        return f"{self.name} (ID: {self.customer_id})"

class Rental:
    def __init__(self):
        self.rented_cars = []

    def rent_car(self, customer, car):
        if car.is_available:
            car.is_available = False
            self.rented_cars.append((customer, car))
            print(f"{customer.name} rented {car}")
        else:
            print(f"{car} is not available for rent.")

    def return_car(self, car):
        for customer, rented_car in self.rented_cars:
            if rented_car == car:
                rented_car.is_available = True
                self.rented_cars.remove((customer, rented_car))
                print(f"{customer.name} returned {car}")
                return
        print(f"This car is not rented or does not exist in the system.")

    def display_rented_cars(self):
        if not self.rented_cars:
            print("No cars are currently rented.")
        else:
            print("List of rented cars:")
            for customer, car in self.rented_cars:
                print(f"{customer.name} rented {car}")

# Example usage:
car1 = Car(1, "Toyota", "Camry", 2020)
car2 = Car(2, "Honda", "Civic", 2021)
customer1 = Customer(101, "John Doe")
customer2 = Customer(102, "Jane Doe")

rental_system = Rental()

rental_system.rent_car(customer1, car1)
rental_system.rent_car(customer2, car2)

rental_system.display_rented_cars()

rental_system.return_car(car1)

rental_system.display_rented_cars()
