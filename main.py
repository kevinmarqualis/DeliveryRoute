# Kevin McBride ID: 010009106
from data import *
from truck import Truck
from hash_table import HashTable
from graph import *
import csv


# load package data from csv and store in HashTable
packages = HashTable()
load_package_data(packages)

# load distance data and create graph
city_map = Graph()
address_list = []
with open('distance_data.csv', encoding='utf-8-sig') as distance_data:
    reader = csv.DictReader(distance_data)
    for row in reader:
        curr_address = row['Address']
        address_list.append(curr_address)



# load packages from the packages HashTable into the trucks
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()


