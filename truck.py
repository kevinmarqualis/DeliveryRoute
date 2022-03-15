from hash_table import HashTable
from package import Package

import datetime


class Truck:
    """
    Class that contains information about the truck and the loaded packages
    Parameters: truck_number, hours, minutes, seconds
    Hours, minutes, seconds initializes the truck's starting delivery time
    O(N) space complexity where N is the number of packages loaded
    """
    TRUCK_MPH = 18  # Constant value for truck's drive speed

    def __init__(self, truck_number, hours, minutes, seconds):
        self.truck_number = truck_number
        self.current_time = datetime.datetime(day=12, month=3, year=2022, hour=hours, minute=minutes, second=seconds)
        self.miles_driven = 0
        self.truck_storage = HashTable()
        self.delivery_locations = []
        self.location = '4001 South 700 East'
        self.truck_information = {'08:00 AM': []}
        self.return_time = ''

    def time_to_deliver(self, miles):
        """
        Function that takes miles as a parameter and returns the amount of time it takes
        to drive the distance based on TRUCK_MPH = 18
        :O(1) time complexity
        :param miles:
        :return datetime.timedelta() value:
        """
        hours = miles / self.TRUCK_MPH
        time_taken = datetime.timedelta(hours=float(hours))
        return time_taken

    def load_package(self, package: Package):
        """
        Function that takes a Package object as a parameter and loads it into self.truck_storage,
        adds the package delivery location to the delivery_locations list, and adds a timestamp
        for the package at 8:00 AM.
        :O(N) time complexity
        :param package:
        :return True:
        """
        package.truck_number = self.truck_number
        self.truck_storage.insert_item(package.package_id, package)
        self.delivery_locations.append((package.package_id, package.address))
        self.truck_information['08:00 AM'].append((package.get_current_status(), round(self.miles_driven, 2)))
        return True

    def deliver_packages(self, graph):
        """
        Function that takes a graph as a parameter to deliver packages along an optimized path on the graph.
        Will also update the miles driven by the truck, the current location of the truck, and the status
        of each package as it is delivered
        :O(N^2) time complexity
        :param graph:
        :return True:
        """
        optimized_path = self.find_optimized_route(graph)
        # Set each loaded package to "en route"
        for pack in optimized_path:
            package_id = pack[0]
            package = self.truck_storage.lookup_item(package_id)
            package.status = package.delivered_statuses[1]
        # Deliver each package based on the optimized delivery path
        for loc in optimized_path:
            package_id = loc[0]
            next_location = loc[1]

            time_taken = self.time_to_deliver(graph.edge_distances[(self.location, next_location)])
            self.miles_driven += graph.edge_distances[(self.location, next_location)]
            self.location = next_location
            self.current_time += time_taken

            current_package = self.truck_storage.lookup_item(package_id)
            current_package.status = current_package.delivered_statuses[2]
            current_package.delivered_time = self.current_time.strftime("%I:%M %p")
            self.upload_package_status(optimized_path)
        self.return_time = self.current_time.strftime("%I:%M %p")
        return True

    def upload_package_status(self, truck_package_list):
        """
        Function that takes the truck delivery list and adds the status of each package at each delivery.
        Keeps a record of package status at each delivery interval along the route
        :O(N) time complexity
        :param truck_package_list:
        :return True:
        """
        time = self.current_time.strftime("%I:%M %p")
        self.truck_information[time] = []
        for i in truck_package_list:
            current_package = self.truck_storage.lookup_item(i[0])
            current_package_status = current_package.get_current_status()
            self.truck_information[time].append((current_package_status, round(self.miles_driven, 2)))
        return True

    def find_optimized_route(self, graph):
        """
        Nearest Neighbor algorithm implementation. Takes a graph as a parameter and
        starts at the trucks starting location. It then selects the
        shortest distance(edge) at each stop for the next delivery location and adds
        it to the path list
        :O(N^2) time complexity
        :param graph:
        :return list containing an optimal path:
        """
        next_location = ''
        path = []
        while self.delivery_locations:
            min_distance = float('inf')
            for loc in self.delivery_locations:
                if graph.edge_distances[(self.location, loc[1])] < min_distance:
                    min_distance = graph.edge_distances[(self.location, loc[1])]
                    next_location = loc
            path.append(next_location)
            self.delivery_locations.remove(next_location)

        return path
