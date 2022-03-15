
class HashTable:
    """
    Implementation of a hash table that contains an insert, lookup, and remove function.
    Allows the user to specify the size by providing a size parameter upon instantiation
    """

    def __init__(self, table_size=10):
        """
        Initializes a chaining Hash Table using a list of lists to be used with the other functions.
        :param table_size:
        """
        self.table_size = table_size
        self.table = []
        for i in range(self.table_size):
            self.table.append([])

    def insert_item(self, package_id, new_package):
        """
        Takes an ID and a Package object as parameters and inserts the package into the table using the
        provided ID and the Hash function to find the correct index
        :O(N) time complexity
        :param package_id:
        :param new_package:
        :return True:
        """
        index = self.hash(package_id)
        for package in self.table[index]:
            if package.package_id == package_id:
                print('Package already exists.\n')
                return False
        self.table[index].append(new_package)
        return True

    def lookup_item(self, package_id):
        """
        Takes an ID(key) as a parameter and returns the Package object corresponding to the given ID by
        using the Hash function to find the index and then looping through each item at that index checking
        for the ID
        :O(N) time complexity
        :param package_id:
        :return Package object or False if package is not found:
        """
        index = self.hash(package_id)
        for package in self.table[index]:
            if package.package_id == package_id:
                return package
        print("That package does not exist.")
        return False

    def remove_item(self, package_id):
        """
        Takes an ID(key) as a parameter and removes the Package object corresponding to the given ID by
        using the Hash function to find the index and then looping through each item at that index checking
        for the ID
        :O(N) time complexity
        :param package_id:
        :return:
        """
        index = self.hash(package_id)
        for package in self.table[index]:
            if package.package_id == package_id:
                self.table[index].remove(package)
                return True

        return False

    def hash(self, key):
        """
        Hash function that takes a key as a parameter to determine the index that an item lives in
        inside the Hash Table
        :O(1) time complexity
        :param key:
        :return:
        """
        return int(key) % self.table_size
