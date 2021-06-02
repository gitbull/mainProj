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
        self._cost = self.getCost()

    def getCost(self):
        if self._catetory.lower() == "cruiser":
            self._cost = 10000
        elif self._catetory.lower() == "sport":
            self._cost = 15000
        else:
            self._cost = 20000
        return self._cost

https://www.shjpolice.gov.ae/ (مية اشارة ضويئه مدينة جده ثمانية الالاف شحنه موجبه فقط للون الاشارهاثنا السير (اخضر
