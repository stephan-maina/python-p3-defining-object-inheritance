class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number
        self.tank_capacity = 0  # New attribute for tank capacity (in gallons)
        self.current_fuel = 0  # New attribute for current fuel level (in gallons)

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        if self.current_fuel < self.tank_capacity:
            fuel_needed = self.tank_capacity - self.current_fuel
            self.current_fuel = self.tank_capacity
            return f"Filled up {fuel_needed} gallons of fuel."
        else:
            return "The tank is already full."

    def add_fuel(self, gallons):
        if self.current_fuel + gallons <= self.tank_capacity:
            self.current_fuel += gallons
            return f"Added {gallons} gallons of fuel."
        else:
            return f"Cannot add {gallons} gallons, it exceeds the tank capacity."

    def check_fuel_level(self):
        return f"Current fuel level: {self.current_fuel} gallons out of {self.tank_capacity} gallons."

# Example usage:
car = Vehicle(wheel_size=17, wheel_number=4)
car.tank_capacity = 15  # Set the tank capacity
print(car.fill_up_tank())  # Fill up the tank
print(car.add_fuel(10))  # Add 10 gallons of fuel
print(car.check_fuel_level())  # Check the current fuel level
