import os
from Motorcycle import Motorcycle

class VehicleBuilder(object):

    def __init__(self):
        print "Vehicle Builder:"
        self.vehObj = None

    def buildVehicle(self, vehType):
        if vehType.lower() == "m":
            self.vehObj = self.buildMotorcycle()
        elif vehType.lower() == "c":
            self.vehObj = self.buildCar()
        else:
            print "Invalid input. Try again."
        return self.vehObj

    def buildMotorcycle(self):
        print "New Motorcycle."
        make = raw_input("Enter make:")
        model = raw_input("Enter model:")
        year = raw_input("Enter year:")
        category = raw_input("Enter category:")
        displacement = raw_input("Enter displacement:")
        newMC = Motorcycle(make, model, year, category, displacement)
        return newMC

    def buildCar(self):
        print ("Under construction")

    def listMotorcycles(self, mcList):
        print "Number of motorcycles:" + str(len(mcList))
        for mc in mcList:
            print "Make:"+str(mc._make) + ", Model:"+str(mc._model) + ", Year:"+str(mc._year) + ", Type:"+str(mc._catetory)
            print "Displacement:"+str(mc._displacement) + " cc"
            print "Vehicle Type:"+str(mc._veh_category) + ", Wheels:"+str(mc._num_wheels)




