from hash_table import HashTable
from package import Package


class Truck:

    def __init__(self):
        self.truck_storage = HashTable()

    def load_package(self, package: Package):
        self.truck_storage.insert_item(package.package_id, package.address, package.deadline, package.city,
                                       package.zipcode, package.weight, package.status)

