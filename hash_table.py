
class HashTable:
    """
    Implementation of a hash table
    Hash Function takes sum of the values in the id mod table size
    """

    def __init__(self, table_size=10):
        self.table_size = table_size
        self.table = []
        for i in range(self.table_size):
            self.table.append([])

    def insert_item(self, package_id, new_package):
        index = self.hash(package_id)
        for package in self.table[index]:
            if package.package_id == package_id:
                print('Package already exists.\n')
                return False
        self.table[index].append(new_package)
        return True

    def lookup_item(self, package_id):
        index = self.hash(package_id)
        for package in self.table[index]:
            if package.package_id == package_id:
                return package
        print("That package does not exist.")
        return False

    def remove_item(self, package_id):
        index = self.hash(package_id)
        for package in self.table[index]:
            if package.package_id == package_id:
                self.table[index].remove(package)
                return True

        return False

    def hash(self, key):
        return int(key) % self.table_size
