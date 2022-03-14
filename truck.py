from hash_table import HashTable
from package import Package

import datetime


class Truck:
    """
    Container(HashTable) for packages
    """
    TRUCK_MPH = 18

    def __init__(self, truck_number, hours, minutes, seconds):
        self.truck_number = truck_number
        self.current_time = datetime.datetime(day=12, month=3, year=2022, hour=hours, minute=minutes, second=seconds)
        self.miles_driven = 0
        self.truck_storage = HashTable()
        self.delivery_locations = []
        self.location = '4001 South 700 East'
        self.truck_information = {'08:00 AM': []}
        self.return_time = ''

    def time_to_deliver(self, miles):  # O(1) time complexity
        hours = miles / self.TRUCK_MPH
        time_taken = datetime.timedelta(hours=float(hours))
        return time_taken

    def load_package(self, package: Package):  # O(n) time complexity
        # package.status = package.delivered_statuses[1]
        package.truck_number = self.truck_number
        self.truck_storage.insert_item(package.package_id, package)
        self.delivery_locations.append((package.package_id, package.address))
        self.truck_information['08:00 AM'].append((package.get_current_status(), round(self.miles_driven, 2)))

    def deliver_packages(self, graph):  # O(n^2) time complexity
        optimized_path = self.find_optimized_route(graph)
        for pack in optimized_path:
            package_id = pack[0]
            package = self.truck_storage.lookup_item(package_id)
            package.status = package.delivered_statuses[1]

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

    def upload_package_status(self, truck_package_list):  # O(n) time complexity
        time = self.current_time.strftime("%I:%M %p")
        self.truck_information[time] = []
        for i in truck_package_list:
            current_package = self.truck_storage.lookup_item(i[0])
            current_package_status = current_package.get_current_status()
            self.truck_information[time].append((current_package_status, round(self.miles_driven, 2)))

    def find_optimized_route(self, graph):  # O(n^2) time complexity
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
