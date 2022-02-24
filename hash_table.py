
class HashTable:
    """
    Implementation of a hash table
    Hash Function takes sum of the values in the id mod table size
    """

    def __init__(self):
        self.table_size = 10
        self.table = []
        for i in range(self.table_size):
            self.table.append([])

    def insert_item(self, package_id, package):
        index = self.hash(package_id)
        if not self.table[index]:
            self.table[index].append(package)
            return True
        for package in self.table[index]:
            if package.package_id == package_id:
                return False

    def lookup_item(self, package_id):
        index = self.hash(package_id)
        for package in self.table[index]:
            if package.package_id == package_id:
                return package
        return False

    def hash(self, key):
        hash_sum = 0
        for c in key:
            hash_sum += int(c)
        return hash_sum % self.table_size
