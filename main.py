# Kevin McBride ID: 010009106

from data import *
from truck import Truck
from hash_table import HashTable
from map import *
from time import time
from datetime import datetime


# Load package data from csv and store in HashTable
packages = HashTable()
load_package_data(packages)

# Load distance data and create graph
city_map = Graph()
load_distance_data(city_map)

# Load packages from the packages HashTable into the trucks
# Start time is 8:00am
truck1 = Truck('1', 8, 0, 0)
# Load packages into truck 1
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

# Start time is 8:00am
truck2 = Truck('2', 8, 0, 0)
# Load packages into truck 2
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

# Start time is 10:20am waiting for updated address for package 9
truck3 = Truck('3', 10, 20, 0)
package9 = packages.lookup_item('9')
package9.address = '410 S State St'
# Load packages into truck 3
truck3.load_package(packages.lookup_item('9'))
truck3.load_package(packages.lookup_item('10'))
truck3.load_package(packages.lookup_item('11'))
truck3.load_package(packages.lookup_item('12'))
truck3.load_package(packages.lookup_item('17'))
truck3.load_package(packages.lookup_item('22'))
truck3.load_package(packages.lookup_item('23'))
truck3.load_package(packages.lookup_item('24'))
truck3.deliver_packages(city_map)

# Implement the command line UI
total_distance = round(truck1.miles_driven + truck2.miles_driven + truck3.miles_driven, 2)
user_input = ''

while user_input != 'q':
    print('\n-------WELCOME TO THE WGUPS PROGRAM!-------')
    print('\nt -> "List status of packages at a specified time"\n')
    print('id -> "List package information by id"\n')
    print('d -> "Get distance and time traveled by each truck"\n')
    print('q -> "Quit"\n')

    user_input = input('What do you want to do?\n')

    # handle package display by specified time
    if user_input == 't':
        chosen_time = input('Please give a time in {hh:mm AM/PM} format.\n')
        try:
            chosen_time = datetime.strptime(chosen_time, '%I:%M %p')
        except ValueError:
            print('Invalid time entered.')
            continue
        if chosen_time < datetime.strptime('08:00 AM', '%I:%M %p'):
            print('Please enter a time after 07:59 AM')
            continue
        # Print Truck 1 Package Statuses
        closest_time = datetime.strptime('08:00 AM', '%I:%M %p')
        log_time = ''
        for k in truck1.truck_information:
            time_key = datetime.strptime(k, '%I:%M %p')
            if closest_time <= time_key <= chosen_time:
                closest_time = time_key
                log_time = k
        print('\n---TRUCK 1 PACKAGES---\n')
        # print(truck1.truck_information[log_time])
        for pack in truck1.truck_information[log_time]:
            print(pack[0], '\n')
        truck1_miles = truck1.truck_information[log_time][0][1]
        print('Miles Driven -- ' + str(truck1_miles))

        # Print Truck 2 Package Statuses
        closest_time = datetime.strptime('08:00 AM', '%I:%M %p')
        log_time = ''
        for k in truck2.truck_information:
            time_key = datetime.strptime(k, '%I:%M %p')
            if closest_time <= time_key <= chosen_time:
                closest_time = time_key
                log_time = k
        print('\n---TRUCK 2 PACKAGES---\n')
        # print(truck2.truck_information[log_time])
        for pack in truck2.truck_information[log_time]:
            print(pack[0], '\n')
        truck2_miles = truck2.truck_information[log_time][0][1]
        print('Miles Driven -- ' + str(truck2_miles))

        # Print Truck 3 Package Statuses
        closest_time = datetime.strptime('08:00 AM', '%I:%M %p')
        log_time = ''
        for k in truck3.truck_information:
            time_key = datetime.strptime(k, '%I:%M %p')
            if closest_time <= time_key <= chosen_time:
                closest_time = time_key
                log_time = k
        print('\n---TRUCK 3 PACKAGES---\n')
        for pack in truck3.truck_information[log_time]:
            print(pack[0], '\n')
        truck3_miles = truck3.truck_information[log_time][0][1]
        print('Miles Driven -- ' + str(truck3_miles))
        print('------------------------------------------------------------------------')
        print('Total miles driven at ' + chosen_time.strftime('%I:%M %p') + ' is ' +
              str(round(truck1_miles + truck2_miles + truck3_miles, 2)) + ' miles.')

    # handle package display by id
    elif user_input == 'id':
        package_id = input('Enter a package id: ')
        if 1 < int(package_id) < 41:
            package = packages.lookup_item(package_id)
            print(package.get_current_status())
        else:
            print('Invalid ID entered. Please try again.')

    # handle truck travel distance
    elif user_input == 'd':
        print('\nTruck 1 - ' + str(round(truck1.miles_driven, 2)) + ' miles')
        print('Time on delivery route -- 08:00 AM - ' + truck1.return_time)
        print('\nTruck 2 - ' + str(round(truck2.miles_driven, 2)) + ' miles')
        print('Time on delivery route -- 08:00 AM - ' + truck2.return_time)
        print('\nTruck 3 - ' + str(round(truck3.miles_driven, 2)) + ' miles')
        print('Time on delivery route -- 10:20 AM - ' + truck3.return_time)
        print('\nTotal distance driven is ' + str(total_distance) + '\n\n')

    elif user_input == 'q':
        break

    else:
        print('Invalid option selected. Please try again.\n')
