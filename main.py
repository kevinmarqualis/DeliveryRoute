# Kevin McBride ID: 010009106
from data import *
from truck import Truck
from hash_table import HashTable
from location import Location


# load package data from csv and store in HashTable
packages = HashTable()
load_package_data(packages)

# load distance data


# load packages from the packages HashTable into the trucks
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

# create the graph data structure for the delivery locations
city_map = []


# Test Print Statements
print(packages.lookup_item('28'))
