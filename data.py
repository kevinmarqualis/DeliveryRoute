import csv
from package import Package


def load_package_data(hashtable):
    """
    Function that parses a csv file, creates a Package object and inserts the object into the Hash Table
    :O(N) time complexity
    :param hashtable:
    :return:
    """
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


def load_distance_data(graph):
    """
    Function that parses a distance data csv file, adds the address to a list, and then creates a graph
    based on the location and distance information parsed
    :O(N^2) time complexity
    :param graph:
    :return:
    """
    address_list = []
    distance_list = []
    with open('distance_data.csv', encoding='utf-8-sig') as distance_data:
        reader = csv.DictReader(distance_data)
        for row in reader:
            curr_address = row['Address'].split('(')[0].strip()
            address_list.append(curr_address)
            distance_list.append(row)

    for i in range(len(address_list)):
        graph.add_location(address_list[i])
        for k, v in distance_list[i].items():
            if k == 'Address':
                continue
            if v == '':
                break
            graph.add_edge(address_list[i], k, v)
