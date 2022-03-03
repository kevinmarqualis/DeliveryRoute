# Kevin McBride ID: 010009106
from data import *
from truck import Truck
from hash_table import HashTable
from graph import *


# load package data from csv and store in HashTable
packages = HashTable()
load_package_data(packages)

# load distance data and create graph
city_map = Graph()
load_distance_data(city_map)

# load packages from the packages HashTable into the trucks
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()


