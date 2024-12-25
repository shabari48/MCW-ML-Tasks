from abc import ABC, abstractmethod


class Car(ABC):

    cars=[]  #List of all cars

    @staticmethod
    def display_welcome_message():
        print("Welcome to our car dashboard system!\n")


    #Constructor

    def __init__(self, brand, model,mileage):
        self.brand = brand
        self.model = model
        self.__mileage=mileage   #distance covered by car in 1 litre of fuel or 1 kwh of battery
        self.__engine_on = False
        self.__km_ran=0

        Car.cars.append(self)


    #Properties


    @property
    def km_ran(self):
        return self.__km_ran
    
    @km_ran.setter
    def km_ran(self, value):
        self.__km_ran = value

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, value):
        assert value > 0, "Mileage must be a positive number."
        self.__mileage = value


    #Engine methods

    def start_engine(self):
        self.__engine_on = True
        if self.__class__.__name__ == "Ev":
            print(f"{self.brand} {self.model} electric motor started.")
        else:
            print(f"{self.brand} {self.model} engine started.")


    def stop_engine(self):
        self.__engine_on = False
        if self.__class__.__name__ == "Ev":
            print(f"{self.brand} {self.model} electric motor started.")
        else:
            print(f"{self.brand} {self.model} engine started.")


    def is_engine_on(self):
        return self.__engine_on

    
    #Class methods

    @classmethod
    def create_car(cls, car_type, brand, model,mileage, **kwargs):
        if car_type == "EV":
            from ev import Ev
            return Ev(brand, model, mileage, **kwargs)
        elif car_type == "GasCar":
            from gascar import GasCar
            return GasCar(brand, model,mileage, **kwargs)
        

    @classmethod
    def get_cars(cls):
        print("Cars in the system:")
        return f"{Car.cars}\n"
        
        

    #Abstract methods and properties

    @property
    @abstractmethod
    def cost_per_km(self):
        pass

    @abstractmethod
    def vehicle_range(self):
        pass
    

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def operationalcost(self):
        pass


    #magic methods

    def __repr__(self):
        return f"{self.brand} {self.model}"
    
    
    
   