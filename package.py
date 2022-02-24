
class Package:
    """
    Package object that holds package data
    """
    delivered_status = ["at the hub", "en route", "delivered"]

    def __init__(self, package_id, address, deadline, city, zipcode, weight):
        self.package_id = package_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.status = self.delivered_status[0]
