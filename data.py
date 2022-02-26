import csv
from package import Package


def load_package_data(hashtable):
    with open('package_data.csv') as package_data:
        reader = csv.reader(package_data, delimiter=',')
        for row in reader:
            if row[1] == 'Address':
                continue
            package_id = row[0]
            address = row[1]
            city = row[2] + ', ' + row[3]
            zipcode = row[4]
            deadline = row[5]
            weight = row[6]
            current_package = Package(package_id, address, city, zipcode, deadline, weight)
            hashtable.insert_item(current_package.package_id, current_package)


def load_distance_data(distances):

    return distances
