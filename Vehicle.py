import os

class Vehicle(object):

    _num_MCs = 0
    _num_Cs = 0
    _uncategorized = 0

    def __init__(self, veh_category, num_wheels):
        self._veh_category = veh_category
        self._num_wheels = num_wheels

        if self._veh_category.lower() == "m":
            Vehicle._num_MCs += 1
            print "Number of motorcycles added: " + str(Vehicle._num_MCs)
        elif self._veh_category.lower() == "c":
            Vehicle._num_Cs += 1
            print "Number of cars added: " + str(Vehicle._num_Cs)
        else:
            Vehicle._uncategorized += 1
            print "Number of uncategorized vehicles added: " + str(Vehicle._MCs)
سالب نقل طاقه ستة الآف و تسع ميه لمكاين ديزيل يدعم إشاره ضوئيه
