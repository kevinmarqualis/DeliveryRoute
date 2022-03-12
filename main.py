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
# start time is 8:00am
truck1 = Truck(8, 0, 0)
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
truck1.deliver_packages(city_map)

# start time is 8:00am
truck2 = Truck(8, 0, 0)
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
truck2.deliver_packages(city_map)

# start time is 10:20am waiting for updated address for package 9
truck3 = Truck(10, 20, 0)
package9 = packages.lookup_item('9')
package9.address = '410 S State St'
# load packages into truck 3
truck3.load_package(packages.lookup_item('9'))
truck3.load_package(packages.lookup_item('10'))
truck3.load_package(packages.lookup_item('11'))
truck3.load_package(packages.lookup_item('12'))
truck3.load_package(packages.lookup_item('17'))
truck3.load_package(packages.lookup_item('22'))
truck3.load_package(packages.lookup_item('23'))
truck3.load_package(packages.lookup_item('24'))
truck3.deliver_packages(city_map)

print(round(truck1.miles_driven + truck2.miles_driven + truck3.miles_driven, 2))
