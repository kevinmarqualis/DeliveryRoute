class Graph:
    """
    Graph builder implementation for locations in the delivery area
    """
    def __init__(self):
        self.adjacency_list = {}
        self.edge_distances = {}

    def add_location(self, new_location):
        """
        Adds a location to the adjacency list for an instance
        :param new_location:
        :return:
        """
        self.adjacency_list[new_location] = []

    def add_edge(self, start_location, end_location, distance):
        """
        Adds an undirected edge between "start_location" to "end_location" with a weight of "distance"
        :param start_location:
        :param end_location:
        :param distance:
        :return:
        """
        self.edge_distances[(start_location, end_location)] = float(distance)
        self.edge_distances[(end_location, start_location)] = float(distance)
        self.adjacency_list[start_location].append(end_location)
        self.adjacency_list[end_location].append(start_location)
