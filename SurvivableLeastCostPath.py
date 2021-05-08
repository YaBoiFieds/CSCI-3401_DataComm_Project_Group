import random

G = {
    1: {2: 3, 3: 6, 7: 7, 8: 8},
    2: {1: 3, 3: 3, 4: 4},
    3: {1: 6, 2: 3, 6: 7},
    4: {2: 4, 5: 2, 11: 9},
    5: {4: 2, 6: 6, 7: 3},
    6: {3: 7, 5: 6, 10: 6, 14: 8},
    7: {1: 7, 5: 3, 8: 2},
    8: {1: 8, 7: 2, 9: 3},
    9: {8: 3, 10: 4, 12: 3, 13: 2},
    10: {6: 6, 9: 4},
    11: {4: 9, 12: 4, 13: 4},
    12: {9: 3, 11: 4, 14: 3},
    13: {9: 2, 11: 4, 14: 1},
    14: {6: 8, 12: 3, 13: 1}
}


def dijkstra(graph, source, destination):
    shortest_distance = {}  # records the cost of travel to node, updates as shorter cost discovered
    track_predecessor = {}  # records previous node for path tracking
    unseenNodes = graph  # allows iteration through all nodes
    infinity = float('inf')  # used for comparing paths to find the lowest cost path
    track_path = []  # path order for lowest cost path

    for node in unseenNodes:  # for every node in the graph
        shortest_distance[node] = infinity  # assigns cost of infinity
    shortest_distance[source] = 0  # except for source node as this is our starting point

    while unseenNodes:  # version of 'while True' to continue iteration of while loop until all node have been covered
        min_dist_node = None  # min distance starts empty

        for node in unseenNodes:  # iterates through each node
            if min_dist_node == None:  # checks that min_dist_node equals None
                min_dist_node = node  # sets min_dist_node as starting node
            elif shortest_distance[node] < shortest_distance[min_dist_node]:
                min_dist_node = node
                # swaps min_dist_node with node if shortest_distance at the node is less than the shortest distance at
                # the min_dist_node

        path_options = graph[min_dist_node].items()  # stores paths listed in graph for min_dist_node

        # for loop refines route and tracks via track_predecessor
        for child_node, weight in path_options:
            if weight + shortest_distance[min_dist_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_dist_node]
                track_predecessor[child_node] = min_dist_node

        # helps to stop while loop
        unseenNodes.pop(min_dist_node)

    currentNode = destination

    # for all nodes except source since source doesn't have a predecessor
    while currentNode != source:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]  # help move back along the path
        except KeyError:
            print("There is no path that is reachable.")
            break

    # for source node
    track_path.insert(0, source)

    if shortest_distance[destination] != infinity:
        print("Shortest path is " + str(shortest_distance[destination]))
        print("Optimum path is " + str(track_path))

s = random.randint(1, 14)  # randomised source
d = random.randint(1, 14)  # randomised destination
if d == s:  # randomises d again if same as source
    d = random.randint(0, 13)

print("Source node: " + str(s) + "\nDestination node: " + str(d))
dijkstra(G, s, d)