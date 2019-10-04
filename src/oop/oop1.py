# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle(object): #No Base Class / Object
    pass

class FlightVehicle(Vehicle): #Base Class Vehicle
    pass

class Starship(FlightVehicle): #Base Class Vehicle via FlightVehicle
    pass

class Airplane(FlightVehicle): #Base Class Vehicle via FlightVehicle
    pass

class GroundVehicle(Vehicle): #Base Class Vehicle
    pass

class Car(GroundVehicle): #Base Class Vehicle via GroundVehicle
    pass

class Motorcycle(GroundVehicle): #Base Class Vehicle via GroundVehicle
    pass