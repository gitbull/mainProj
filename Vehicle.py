import os

class Vehicle(object):

    _MCs = 0
    _Cs = 0
    _uncategorized = 0

    def __init__(self, veh_category, num_wheels):
        self._veh_category = veh_category
        self._num_wheels = num_wheels

        if self._veh_category.lower() == "m":
            Vehicle._MCs += 1
            print "Number of motorcycles: " + str(Vehicle._MCs)
        elif self._veh_category.lower() == "c":
            Vehicle._Cs += 1
            print "Number of cars: " + str(Vehicle._MCs)
        else:
            Vehicle._uncategorized += 1
            print "Number of uncategorized vehicles: " + str(Vehicle._MCs)
