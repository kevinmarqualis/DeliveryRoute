
class HashTable:
    """
    Implementation of a hash table
    Hash Function takes sum of the values in the id mod 3
    """

    def __init__(self):
        self.table = []

    def insert_item(self, id, address, deadline, city, zipcode, weight, status):
        delivered_time = "0:00"
        hash_value = self.hashify(id)
        self.table[hash_value] = [id, address, deadline, city, zipcode, weight, status, delivered_time]

    def lookup_item(self, id):
        hash_value = self.hashify(id)
        return self.table[hash_value]

    @staticmethod
    def hashify(id):
        id_sum = 0
        for i in id:
            id_sum += int(i)
        return id_sum % 3
