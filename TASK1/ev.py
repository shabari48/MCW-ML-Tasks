from car import Car

class Ev(Car):

    #Constructor

    def __init__(self, brand, model,mileage:int , battery_capacity=100):
        super().__init__(brand, model,mileage)
        self.__battery_capacity = battery_capacity
        self.__battery_level = battery_capacity
    

    #Properties 

    @property
    def cost_per_km(self):
        return 1.2
    

    @property
    def battery_capacity(self):
        return self.__battery_capacity

        

    @property
    def battery_level(self):
        return self.__battery_level

    @battery_level.setter
    def battery_level(self, value):
        assert 0 <= value <= 100, "Battery level must be between 0 and 100."
        self.__battery_level = value


    #Battery related methods

    def charge_battery(self, value):
        self.battery_level = min(self.battery_level + value, self.battery_capacity)  # Max capacity is 100%
        print(f"Charging {self.brand} {self.model}'s battery to {self.battery_level} kWh.")

    def check_battery(self):
        print(f"{self.brand} {self.model}'s battery level: {self.battery_level}%, capacity: {self.__battery_capacity} kWh.")


    
    #Implementing abstract methods

    def vehicle_range(self):
        range_km = self.battery_level * self.mileage
        return(f"{self.brand} {self.model} can travel approximately {range_km} km on current battery level.")
       
    

    
    def drive(self, distance):
        assert self.is_engine_on(), "Turn on the engine"
        battery_required = distance / self.mileage
        if battery_required > self.battery_level:
            print("Not enough battery. Please charge.")
            print(self.vehicle_range())
            raise ValueError("Not enough battery. Please charge.")

        self.battery_level -= battery_required
        self.km_ran+=distance
        print(f"Driving {distance} km. Remaining battery: {self.battery_level} / {self.battery_capacity}.")
        

    def operationalcost(self):
         return f"{self.brand}'s {self.model} Operational cost till date {self.cost_per_km * self.km_ran}"