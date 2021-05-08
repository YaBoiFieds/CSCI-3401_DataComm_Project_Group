from SurvivableLeastCostPath import *
import random

Cost = []  # for calculating overage cost of all iterations
success = 0  # for calculating success rate
amnt = 1000
for b in range(amnt):
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

    Gprime = {
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

    # create source and destination values
    s = random.randint(1, 14)  # randomised source
    d = random.randint(1, 14)  # randomised destination
    if d == s:  # randomises d again if same as source
        d = random.randint(1, 14)

    print("Source node: " + str(s) + "\nDestination node: " + str(d))
    dijkstra(G, s, d)

    P1 = None  # variable P1 will hold the list of nodes on optimal path from dijkstra
    P1cost = None  # holds total cost of path

    # read from file created by dijkstras and add each value to P1
    with open("path_output.txt", "r", encoding="utf-8") as f:
        P1 = list(map(int, f.readlines()))
        f.close()

    # read from file created by dijkstras and add value to P1cost
    with open('cost_output.txt', "r", encoding="utf-8") as f:
        num = f.readlines()
        i = int(num[0])
        P1cost = i
        f.close()

    print("\nP1 is " + str(P1) + "\nWhen P1 is removed from G we get P2:\n")

    while True:  # iterates with path has values
        lpath = len(P1)
        lasInd = lpath - 1
        for node in P1:  # for every node in path
            curInd = P1.index(node)
            nexInd = curInd + 1
            if nexInd > lasInd:
                break
            else:
                Gprime[node].pop(
                    P1[nexInd])  # pops the given path option of out of the list for the given node in G
        break

    print("Source node: " + str(s) + "\nDestination node: " + str(d))
    dijkstra(Gprime, s, d)

    P2 = None  # variable p will hold the list of nodes on optimal path from dijkstra
    P2cost = None

    # read from file created by dijkstras and add each value to p
    with open("path_output.txt", "r", encoding="utf-8") as f:
        P2 = list(map(int, f.readlines()))
        f.close()

    # read from file created by dijkstras and add value to P2cost
    with open('cost_output.txt', "r", encoding="utf-8") as f:
        num = f.readlines()
        i = int(num[0])
        P2cost = i
        f.close()

    print("\nP2 is " + str(P2) + ".")

    totalCost = P1cost + P2cost

    print('\nTotal link-disjoint cost is ' + str(totalCost) + '.\n')

    Cost.append(totalCost)  # add total path cost of current iteration to Cost list before original for loop

    success += 1

print("Success rate of algorithm: ", str(int((success / amnt) * 100)), "%\nAverage cost after " + str(amnt) +
      " iterations is: ", str(sum(Cost) / len(Cost)))
# outputs the average path cost and success rate after all 1,000 iterations have completed