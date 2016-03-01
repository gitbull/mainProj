import os
from VehicleFactory import MotorcycleFactory

class VehicleBuilder(object):

    def __init__(self):
        print "Vehicle Builder:"
        self.mcObj = None
        self.carObj = None

    def buildVehicle(self, vehType):
        if vehType.lower() == "m":
            vehObj = self.buildMotorcycle()
        elif vehType.lower() == "c":
            vehObj = self.buildCar()
        else:
            print "Invalid input. Try again."
        return vehObj

    def buildMotorcycle(self):
        make = raw_input("Enter make:")
        model = raw_input("Enter model:")
        year = raw_input("Enter year:")
        category = raw_input("Enter category:")
        displacement = raw_input("Enter displacement:")
        self.mcObj = MotorcycleFactory(make, model, year, category, displacement)
        return self.mcObj.makeMotorcycle()

    def buildCar(self):
        print ("Under construction")
        return None

    def listMotorcycles(self, mcList):
        print "Number of motorcycles:" + str(len(mcList))
        for mc in mcList:
            print "Make:"+str(mc._make) + ", Model:"+str(mc._model) + ", Year:"+str(mc._year) + ", Type:"+str(mc._catetory)
            print "Displacement:"+str(mc._displacement) + " cc"
            print "Vehicle Type:"+str(mc._veh_category) + ", Wheels:"+str(mc._num_wheels)
            print "Cost:$"+str(mc._cost)






