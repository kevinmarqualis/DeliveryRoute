
class Package:
    """
    !!!DELETE IF NOT USING!!!
    Package object to hold package data
    """

    def __init__(self, package_id, address, deadline, city, zipcode, weight, status):
        self.package_id = package_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.status = status
