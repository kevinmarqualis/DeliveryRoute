class Graph:
    """
    Undirected graph implementation for locations in the delivery area.
    O(N*M) space complexity where N is the number of locations and M is the number of edges
    """
    def __init__(self):
        self.adjacency_list = {}
        self.edge_distances = {}

    def add_location(self, new_location):
        """
        Takes a location(node) as a parameter and adds it to the adjacency list
        :O(1) time complexity
        :param new_location:
        :return True:
        """
        self.adjacency_list[new_location] = []
        return True

    def add_edge(self, start_location, end_location, distance):
        """
        Adds an undirected edge between "start_location" and "end_location" with a weight of "distance"
        :O(1) time complexity
        :param start_location:
        :param end_location:
        :param distance:
        :return:
        """
        self.edge_distances[(start_location, end_location)] = float(distance)
        self.edge_distances[(end_location, start_location)] = float(distance)
        self.adjacency_list[start_location].append(end_location)
        self.adjacency_list[end_location].append(start_location)
        return True
