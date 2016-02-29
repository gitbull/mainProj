import os
import sys
from VehicleBuilder import VehicleBuilder

def main(argv):
    print ("In main class")

    mcList = []
    vehObj = None

    builder = VehicleBuilder()
    while True:
        user_input = raw_input("Enter class of vehicle (M or C). Enter 'q' to quit: ")
        if user_input.lower() == "m":
            vehObj = builder.buildVehicle(user_input)
            mcList.append(vehObj)
        elif user_input.lower() == "q":
            break
        else:
            print "Invalid input. Try again."

    builder.listMotorcycles(mcList)

if __name__ == "__main__":
    main(sys.argv)
