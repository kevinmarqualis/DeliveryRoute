from hash_table import HashTable
from package import Package


class Truck:
    """
    Container(HashTable) for packages
    """

    def __init__(self):
        self.truck_storage = HashTable()

    # Object based implementation
    def load_package(self, package: Package):
        self.truck_storage.insert_item(package.package_id, package)
