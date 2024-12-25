from car import Car

class GasCar(Car):

    #Contructor

    def __init__(self, brand, model,mileage:int , tank_capacity:int):
        super().__init__(brand, model,mileage)
        self.__tank_capacity = tank_capacity
        self.__fuel_level = tank_capacity
    
    
    #Properties  

    @property
    def cost_per_km(self):
        return 1.5

    @property
    def tank_capacity(self):
        return self.__tank_capacity

    @property
    def fuel_level(self):
        return self.__fuel_level

    @fuel_level.setter
    def fuel_level(self, value):
        assert value <= self.__tank_capacity, f"Fuel level cannot exceed tank capacity of {self.__tank_capacity} ls."
        self.__fuel_level = value
    
     #Fuel related methods

    def refuel(self, value):
        assert value > 0, "Fueling value must be a positive number."
        self.fuel_level = min(self.fuel_level + value, self.__tank_capacity)  
        print(f"Refueling {self.brand} {self.model} to {self.fuel_level} liters of fuel.")

    def check_fuel_level(self):
        print(f"{self.brand} {self.model} fuel level: {self.fuel_level}/{self.tank_capacity} liters.")


    #implementing abstract methods

    def vehicle_range(self):
        range_km = self.fuel_level * self.mileage
        return f"{self.brand} {self.model} can travel approximately {range_km} km on current fuel level."
       

    def drive(self, distance):
        assert super().is_engine_on(), "Turn on the engine"

        fuel_required = distance / self.mileage
        if fuel_required > self.fuel_level:
            print("Not enough fuel. Please refuel.")
            print(self.vehicle_range())
            raise ValueError("Not enough fuel. Please refuel.")

        self.fuel_level -= fuel_required
        self.km_ran+=distance
        print(f"Driving {distance} km. Remaining fuel: {self.fuel_level}/ {self.tank_capacity} liters.")


    def operationalcost(self):
        return f"{self.brand}'s {self.model} Operational cost till date {self.cost_per_km * self.km_ran}"