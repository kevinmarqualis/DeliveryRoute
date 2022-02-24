
class Location:
    """
    Vertex class for the graph representation of the city
    Takes the location name as a parameter
    Can add neighbors(vertices) and their distances(edges)
    """

    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, neighbor, distance):
        self.neighbors[neighbor] = distance
