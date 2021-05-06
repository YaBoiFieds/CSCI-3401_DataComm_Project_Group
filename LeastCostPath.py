import networkx as nx
import matplotlib.pyplot as plt

# create a empty graph object
G = nx.Graph()

# list hold city names from 13 point node map
cities = ['Seattle, WA',
          'Palo Alto, CA',
          'San Diego, CA',
          'Salt Lake City, UT',
          'Boulder, CO',
          'Houston, TX',
          'Lincoln, NE',
          'Champagne, IL',
          'Pittsburgh, PA',
          'Atlanta, GA',
          'Ann Arbor, MI',
          'Ithaca, NY',
          'Princeton, NJ',
          'College Pk, MD']

# create all edges, cities as nodes, based on 13 point node map
G.add_edge(cities[0], cities[1])
G.add_edge(cities[0], cities[2])
G.add_edge(cities[0], cities[7])
G.add_edge(cities[1], cities[2])
G.add_edge(cities[1], cities[3])
G.add_edge(cities[2], cities[5])
G.add_edge(cities[3], cities[4])
G.add_edge(cities[3], cities[10])
G.add_edge(cities[4], cities[5])
G.add_edge(cities[4], cities[6])
G.add_edge(cities[5], cities[9])
G.add_edge(cities[5], cities[13])
G.add_edge(cities[6], cities[4])
G.add_edge(cities[6], cities[7])
G.add_edge(cities[7], cities[8])
G.add_edge(cities[8], cities[9])
G.add_edge(cities[8], cities[11])
G.add_edge(cities[8], cities[12])
G.add_edge(cities[10], cities[11])
G.add_edge(cities[10], cities[12])
G.add_edge(cities[11], cities[13])
G.add_edge(cities[12], cities[13])

nx.draw(G)
plt.show()

s = 'source'
d = 'destination'
t = 'time'
