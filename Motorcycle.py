import os
from Vehicle import Vehicle

class Motorcycle(Vehicle):

    def __init__(self, make, model, year, category, displacement):
        Vehicle.__init__(self, "M", 2)
        self._make = make
        self._model = model
        self._year = year
        self._catetory = category
        self._displacement = displacement

    def getCategory(self):
        return self._catetory

