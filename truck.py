from map import Graph
from package import Package


class Truck:
    """
    Container(HashTable) for packages
    """

    def __init__(self):
        self.miles_driven = 0
        self.truck_storage = []
        self.delivery_locations = []
        self.location = '4001 South 700 East'

    def load_package(self, package: Package):
        package.status = package.delivered_statuses[1]
        self.truck_storage.append(package)
        self.delivery_locations.append(package.address)

    def deliver_packages(self, graph):
        optimized_path = self.find_optimized_route(graph)
        """
        Psuedocode:
        loop through addresses in optimized path
            add each distance to miles driven update current Time
            deliver package and update status/delivery time
            remove address from list
        """

    def find_optimized_route(self, graph):  # O(n^2)
        next_location = ''
        path = []
        while self.delivery_locations:
            min_distance = float('inf')
            for loc in self.delivery_locations:
                if graph.edge_distances[(self.location, loc)] < min_distance:
                    min_distance = graph.edge_distances[(self.location, loc)]
                    next_location = loc
            path.append(next_location)
            self.delivery_locations.remove(next_location)

        return path


