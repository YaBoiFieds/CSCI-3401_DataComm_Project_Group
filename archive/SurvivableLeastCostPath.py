# Anastasia Altamirano & Nathan Fiedler
# CSCI3401AV Data Communications
# Final Project: Survivable Least Cost Path
# 5/7/2021
# Creates a 14 point node graph with various cities.

# graph class takes in vertices and edges
class MakeGraph:
    # initialize method to init variables for graph class
    def __init__(self, V, E):
        self.E = set(frozenset((u, v)) for u, v in E)  # initialize set of vertices, creates a frozenset of given
        # entries since you can't really make a set of sets so this does that
        self._neighbors = {}  # initialize neighbors set
        for v in V:  # for every vertex in the set of vertices
            self.addVertex(v)  # calls to addVertex() to add an empty set for v
        for u, v in self.E:  # for every edge in the edges set
            self.addEdge(u, v)  # calls to addEdge() to add an edge for u, v

    # method for adding a vertex to a graph
    def addVertex(self, v):
        if v not in self._neighbors:  # checks if v doesn't already exist
            self._neighbors[v] = set()  # creates neighbor set of v

    # method for adding an edge to a graph
    def addEdge(self, u, v):
        self.addVertex(u)  # calls addVertex() to add u
        self.addVertex(v)  # calls addVertex() to add v
        self.E.add(frozenset([u, v]))  # adds edge to E frozenset set
        self._neighbors[u].add(v)  # add the neighbors of u to the neighbors set
        self._neighbors[v].add(u)  # add the neighbors of v to the neighbors set

    # removes an edge u, v if it exists
    def removeEdge(self, u, v):
        edge = frozenset([u, v])  # stores the frozenset of u, v
        if edge in self.E:  # checks that the edge exists
            self.E.remove(edge)  # removes [u, v] from the edges list of a graph
            self._neighbors[u].remove(v)  # removes v from neighbors of u
            self._neighbors[v].remove(u)  # removes u from neighbors of v

    # removes a vertex u
    def removeVertex(self, u):
        delete = list(self.nbrs(u))
        for v in delete:  # for every vertex in the neighbors list
            self.removeEdge(u, v)  # removes edge u, v
        del self._neighbors[u]  # also deletes the set of stored neighbors for u

    # allows access to neighbors list without changing neighbors variables
    def nbrs(self, v):
        return iter(self._neighbors[v])

    # method that returns the degree or amount of neighbors a given node has
    def degree(self, v):  # takes in node v
        return len(self._neighbors[v])  # returns the length of the list of neighbors of v

    # method that returns the amount of edges in a graph
    def e_amnt(self):
        return len(self.E)  # returns the length of E

    # method that returns the amount of vertexes
    def v_amnt(self):
        return len(self._neighbors)


# create list of cities for 14 point node map
cities = ['Seattle, WA', 'Palo Alto, CA', 'San Diego, CA', 'Salt Lake City, UT', 'Boulder, CO', 'Houston, TX',
          'Lincoln, NE', 'Champagne, IL', 'Pittsburgh, PA', 'Atlanta, GA', 'Ann Arbor, MI', 'Ithaca, NY',
          'Princeton, NJ', 'College Pk, MD']

# create list of node names for 75 point node map
n75 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
       31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
       59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]

# pass in the list of cities and edges to Graph class for 14 point node map
G1 = MakeGraph(cities, {(cities[0], cities[1]), (cities[0], cities[2]), (cities[0], cities[7]), (cities[1], cities[2]),
                        (cities[1], cities[3]), (cities[2], cities[5]), (cities[3], cities[4]), (cities[3], cities[10]),
                        (cities[4], cities[5]), (cities[4], cities[6]), (cities[5], cities[9]), (cities[5], cities[13]),
                        (cities[6], cities[7]), (cities[7], cities[8]), (cities[8], cities[9]), (cities[8], cities[11]),
                        (cities[8], cities[12]), (cities[10], cities[11]), (cities[10], cities[12]),
                        (cities[11], cities[13]), (cities[12], cities[13])})

# 0,3,6,0,0,0,7,8,0,0,0,0,0,0
# 3,0,3,4,0,0,0,0,0,0,0,0,0,0
# 6,3,0,0,0,7,0,0,0,0,0,0,0,0
# 0,4,0,0,2,0,0,0,0,0,9,0,0,0
# 0,0,0,2,0,6,3,0,0,0,0,0,0,0
# 0,0,7,0,6,0,0,0,0,6,0,0,0,8
# 0,0,0,0,3,0,0,2,0,0,0,0,0,0
# 8,0,0,0,0,0,2,0,3,0,0,0,0,0
# 0,0,0,0,0,0,0,3,0,4,0,3,2,0
# 0,0,0,0,0,6,0,0,4,0,0,0,0,0
# 0,0,0,9,0,0,0,0,0,0,0,4,4,0
# 0,0,0,0,0,0,0,0,3,0,4,0,0,3
# 0,0,0,0,0,0,0,0,2,0,4,0,0,1
# 0,0,0,0,0,8,0,0,0,0,0,3,0,0
