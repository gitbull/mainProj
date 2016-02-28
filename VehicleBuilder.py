import os
from Motorcycle import Motorcycle

class VehicleBuilder(object):

    def __init__(self):
        print "Vehicle Builder:"
        self.motorcycleList = []

    def buildVehicle(self):
        while True:
            user_input = raw_input("Enter class of vehicle (M or C). Enter 'q' to quit: ")
            if user_input.lower() == "m":
                self.buildMotorcycle()
            elif user_input.lower() == "c":
                self.buildCar()
            elif user_input.lower() == "q":
                break
            else:
                print "Invalid input. Try again."

    def buildMotorcycle(self):
        print "New Motorcycle."
        make = raw_input("Enter make:")
        model = raw_input("Enter model:")
        year = raw_input("Enter year:")
        category = raw_input("Enter category:")
        displacement = raw_input("Enter displacement:")
        newMC = Motorcycle(make, model, year, category, displacement)
        self.motorcycleList.append(newMC)

    def buildCar(self):
        print ("Under construction")

    def listVehicles(self):
        user_input = raw_input("Enter class of vehicle to list (M or C). Enter 'q' to quit: ")
        if user_input.lower() == "m":
            self.listMotorcycles()
        elif user_input.lower() == "c":
            self.listCars()
        elif user_input.lower() == "q":
            return
        else:
            print "Invalid input. Exiting."

    def listMotorcycles(self):
        print "Motorcycles:" + str(len(self.motorcycleList))
        for mc in self.motorcycleList:
            print "Make:"+str(mc._make) + ", Model:"+str(mc._model) + ", Year:"+str(mc._year) + ", Type:"+str(mc._catetory)
            print "Displacement:"+str(mc._displacement) + "cc"
            print "Vehicle Type:"+str(mc._veh_category) + ", Wheels:"+str(mc._num_wheels)




