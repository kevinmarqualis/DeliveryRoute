from hash_table import HashTable
from package import Package

import datetime


class Truck:
    """
    Container(HashTable) for packages
    """
    TRUCK_MPH = 18
    # time_obj = datetime.timedelta(hours=int(h))

    def __init__(self, hours, minutes, seconds):
        self.current_time = datetime.datetime(day=12, month=3, year=2022, hour=hours, minute=minutes, second=seconds)
        self.miles_driven = 0
        self.truck_storage = HashTable()
        self.delivery_locations = []
        self.location = '4001 South 700 East'

    def time_to_deliver(self, miles):
        hours = miles / self.TRUCK_MPH
        time_taken = datetime.timedelta(hours=float(hours))
        return time_taken

    def load_package(self, package: Package):
        package.status = package.delivered_statuses[1]
        self.truck_storage.insert_item(package.package_id, package)
        self.delivery_locations.append((package.package_id, package.address))

    def deliver_packages(self, graph):
        optimized_path = self.find_optimized_route(graph)
        for loc in optimized_path:
            package_id = loc[0]
            next_location = loc[1]

            time_taken = self.time_to_deliver(graph.edge_distances[(self.location, next_location)])
            self.miles_driven += graph.edge_distances[(self.location, next_location)]
            self.location = next_location
            self.current_time += time_taken

            current_package = self.truck_storage.lookup_item(package_id)
            current_package.status = current_package.delivered_statuses[2]
            current_package.delivered_time = self.current_time
        return True

    def find_optimized_route(self, graph):  # O(n^2)
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


