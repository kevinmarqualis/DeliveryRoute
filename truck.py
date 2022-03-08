from hash_table import HashTable
from package import Package


class Truck:
    """
    Container(HashTable) for packages
    """

    def __init__(self):
        self.miles_driven = 0
        self.truck_storage = HashTable()
        self.delivery_locations = []
        self.location = '4001 South 700 East'

    def load_package(self, package: Package):
        package.status = package.delivered_statuses[1]
        self.truck_storage.insert_item(package.package_id, package)
        self.delivery_locations.append((package.package_id, package.address))

    def deliver_packages(self, graph):
        optimized_path = self.find_optimized_route(graph)
        for loc in optimized_path:
            package_id = loc[0]
            next_location = loc[1]
            self.miles_driven += graph.edge_distances[(self.location, next_location)]
            self.location = next_location
            current_package = self.truck_storage.lookup_item(package_id)
            current_package.status = current_package.delivered_statuses[2]

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


