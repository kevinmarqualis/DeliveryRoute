# Kevin McBride ID: 010009106
from data import *
from truck import Truck
from hash_table import HashTable
from map import *


# load package data from csv and store in HashTable
packages = HashTable()
load_package_data(packages)

# load distance data and create graph
city_map = Graph()
load_distance_data(city_map)

# load packages from the packages HashTable into the trucks
truck1 = Truck()
# load packages into truck 1
truck1.load_package(packages.lookup_item('1'))
truck1.load_package(packages.lookup_item('4'))
truck1.load_package(packages.lookup_item('7'))
truck1.load_package(packages.lookup_item('8'))
truck1.load_package(packages.lookup_item('13'))
truck1.load_package(packages.lookup_item('14'))
truck1.load_package(packages.lookup_item('15'))
truck1.load_package(packages.lookup_item('16'))
truck1.load_package(packages.lookup_item('19'))
truck1.load_package(packages.lookup_item('20'))
truck1.load_package(packages.lookup_item('21'))
truck1.load_package(packages.lookup_item('29'))
truck1.load_package(packages.lookup_item('30'))
truck1.load_package(packages.lookup_item('34'))
truck1.load_package(packages.lookup_item('39'))
truck1.load_package(packages.lookup_item('40'))

truck2 = Truck()
# load packages into truck 2
truck2.load_package(packages.lookup_item('2'))
truck2.load_package(packages.lookup_item('3'))
truck2.load_package(packages.lookup_item('5'))
truck2.load_package(packages.lookup_item('6'))
truck2.load_package(packages.lookup_item('18'))
truck2.load_package(packages.lookup_item('25'))
truck2.load_package(packages.lookup_item('26'))
truck2.load_package(packages.lookup_item('27'))
truck2.load_package(packages.lookup_item('28'))
truck2.load_package(packages.lookup_item('31'))
truck2.load_package(packages.lookup_item('32'))
truck2.load_package(packages.lookup_item('33'))
truck2.load_package(packages.lookup_item('35'))
truck2.load_package(packages.lookup_item('36'))
truck2.load_package(packages.lookup_item('37'))
truck2.load_package(packages.lookup_item('38'))

truck3 = Truck()
# load packages into truck 3
truck3.load_package(packages.lookup_item('9'))
truck2.load_package(packages.lookup_item('10'))
truck2.load_package(packages.lookup_item('11'))
truck2.load_package(packages.lookup_item('12'))
truck2.load_package(packages.lookup_item('17'))
truck2.load_package(packages.lookup_item('22'))
truck2.load_package(packages.lookup_item('23'))
truck2.load_package(packages.lookup_item('24'))
