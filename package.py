
class Package:
    """
    Package object that holds package data
    """
    delivered_statuses = ["at the hub", "en route", "delivered"]

    def __init__(self, package_id, address, city, zipcode, deadline, weight):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = self.delivered_statuses[0]
        self.delivered_time = '00:00:00'

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.zipcode,
                                                   self.deadline, self.weight, self.status, self.delivered_time)
