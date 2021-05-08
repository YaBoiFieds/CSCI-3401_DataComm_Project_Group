def __init__(self, graph, source, destination):
    self.graph = graph
    self.source = source
    self.destination = destination


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

    with open('path_output.txt', 'w') as f:
        for i in track_path:
            f.write('%d\n' % i)
        f.close()

    with open('cost_output.txt', 'w') as f:
        f.write(str(shortest_distance[destination]))
        f.close()