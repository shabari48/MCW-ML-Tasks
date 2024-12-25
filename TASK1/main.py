from gascar import GasCar
from ev import Ev
from car import Car

# GasCar => brand, model,mileage, tank_capacity
# Ev => brand, model,mileage, battery_capacity, battery_health=100

#Creating cars => car_type, brand, model,mileage, *args  (Ev->battery_cpacity)  (GasCar->tank_capacity)

Car.display_welcome_message()


ev1=Car.create_car("EV", "Tesla", "Model S", mileage=15,battery_capacity=100)
gc1=Car.create_car("GasCar", "Toyota", "Corolla", mileage=12, tank_capacity=50)

ev2=Ev("Nissan", "Leaf", 10, 50)

print(Car.get_cars()) 

# ev1.start_engine()
# ev1.drive(300)
# ev1.vehicle_range()
# ev1.check_battery()
# ev1.charge_battery(10)
# print(ev1.operationalcost())


gc1.start_engine()
gc1.drive(300)
print(gc1.vehicle_range())
gc1.drive(300)
gc1.check_fuel_level()
gc1.refuel(10)
print(gc1.operationalcost())



