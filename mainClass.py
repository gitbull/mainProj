import os
import sys
from VehicleBuilder import VehicleBuilder

def main(argv):
    print ("In main class")

    builder = VehicleBuilder()
    builder.buildVehicle()
    builder.listVehicles()

if __name__ == "__main__":
    main(sys.argv)
