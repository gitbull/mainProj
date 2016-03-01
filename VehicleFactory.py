import os
from Motorcycle import Motorcycle

class MotorcycleFactory(object):

    _numVehiclesProduced = 0

    def __init__(self, make, model, year, category, displacement):
        print "New Motorcycle."
        MotorcycleFactory._numVehiclesProduced += 1
        self._make = make
        self._model = model
        self._year = year
        self._category = category
        self._displacement = displacement

    def makeMotorcycle(self):
        mcObj = Motorcycle(self._make, self._model, self._year, self._category, self._displacement)
        return mcObj
