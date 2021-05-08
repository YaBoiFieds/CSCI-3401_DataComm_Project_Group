from SurvivableLeastCostPath import *
import random

Cost = []  # for calculating overage cost of all iterations
success = 0  # for calculating success rate
amnt = 1000
for b in range(amnt):
    G = {
        1: {2: 4, 11: 6},
        2: {1: 4, 3: 7, 12: 9},
        3: {2: 7, 4: 2},
        4: {3: 2, 5: 1},
        5: {4: 1, 6: 1},
        6: {5: 1, 7: 3},
        7: {6: 3, 8: 2},
        8: {7: 2, 9: 2, 10: 4},
        9: {8: 2, 14: 5},
        10: {4: 3, 8: 3, 13: 5},
        11: {1: 4, 19: 7},
        12: {2: 9, 4: 5, 13: 6, 18: 5},
        13: {10: 4, 12: 5, 14: 3, 17: 6},
        14: {9: 5, 13: 3, 15: 2},
        15: {14: 2, 16: 4},
        16: {15: 4, 17: 3, 27: 5, 28: 6},
        17: {13: 6, 16: 3, 18: 4, 26: 8},
        18: {12: 5, 17: 4, 19: 5, 22: 9},
        19: {18: 5, 11: 7, 20: 5},
        20: {19: 5, 21: 4},
        21: {20: 4, 22: 4, 40: 5},
        22: {18: 9, 21: 4, 23: 3},
        23: {22: 3, 24: 3, 37: 5},
        24: {23: 3, 25: 2},
        25: {24: 2, 26: 6},
        26: {17: 8, 25: 6, 27: 5, 30: 7, 36: 8},
        27: {16: 5, 26: 5},
        28: {16: 6, 29: 1},
        29: {28: 1, 30: 3},
        30: {26: 7, 29: 3, 31: 4},
        31: {30: 3, 32: 3},
        32: {31: 3, 33: 5, 48: 12},
        33: {32: 5, 34: 5, 47: 2},
        34: {33: 5, 35: 6, 46: 4},
        35: {34: 6, 36: 3},
        36: {26: 8, 35: 3},
        37: {23: 5, 38: 1, 46: 6},
        38: {37: 1, 39: 3},
        39: {38: 3, 40: 1, 41: 5},
        40: {21: 5, 39: 1},
        41: {39: 5, 42: 1},
        42: {41: 1, 43: 2},
        43: {42: 2, 44: 3, 74: 4},
        44: {43: 3, 45: 2, 68: 7},
        45: {44: 2, 46: 1, 70: 12},
        46: {34: 4, 37: 6, 45: 1, 72: 12},
        47: {33: 2, 53: 6, 73: 5},
        48: {32: 12, 49: 4},
        49: {48: 4, 50: 5},
        50: {49: 5, 51: 3},
        51: {50: 3, 52: 6},
        52: {51: 6, 53: 3},
        53: {47: 6, 52: 3, 54: 6},
        54: {53: 6, 55: 4},
        55: {54: 4, 56: 3, 72: 1},
        56: {55: 3, 57: 6},
        57: {56: 6, 58: 2, 69: 1},
        58: {57: 2, 66: 4, 59: 1},
        59: {58: 2, 60: 3},
        60: {59: 3, 61: 3, 67: 4},
        61: {60: 3, 62: 1},
        62: {61: 2, 63: 4},
        63: {62: 4, 64: 3},
        64: {63: 3, 65: 5},
        65: {64: 5, 66: 2, 75: 3},
        66: {58: 4, 65: 2, 67: 4, 68: 3},
        67: {60: 4, 66: 4},
        68: {44: 7, 66: 3, 69: 4, },
        69: {69: 4, 57: 1, 70: 1},
        70: {45: 12, 69: 1, 71: 3},
        71: {70: 3, 72: 5},
        72: {46: 12, 55: 1, 71: 5, 73: 1},
        73: {47: 5, 72: 1},
        74: {43: 4, 75: 1},
        75: {65: 3, 74: 1}
    }

    Gprime = {
        1: {2: 4, 11: 6},
        2: {1: 4, 3: 7, 12: 9},
        3: {2: 7, 4: 2},
        4: {3: 2, 5: 1},
        5: {4: 1, 6: 1},
        6: {5: 1, 7: 3},
        7: {6: 3, 8: 2},
        8: {7: 2, 9: 2, 10: 4},
        9: {8: 2, 14: 5},
        10: {4: 3, 8: 3, 13: 5},
        11: {1: 4, 19: 7},
        12: {2: 9, 4: 5, 13: 6, 18: 5},
        13: {10: 4, 12: 5, 14: 3, 17: 6},
        14: {9: 5, 13: 3, 15: 2},
        15: {14: 2, 16: 4},
        16: {15: 4, 17: 3, 27: 5, 28: 6},
        17: {13: 6, 16: 3, 18: 4, 26: 8},
        18: {12: 5, 17: 4, 19: 5, 22: 9},
        19: {18: 5, 11: 7, 20: 5},
        20: {19: 5, 21: 4},
        21: {20: 4, 22: 4, 40: 5},
        22: {18: 9, 21: 4, 23: 3},
        23: {22: 3, 24: 3, 37: 5},
        24: {23: 3, 25: 2},
        25: {24: 2, 26: 6},
        26: {17: 8, 25: 6, 27: 5, 30: 7, 36: 8},
        27: {16: 5, 26: 5},
        28: {16: 6, 29: 1},
        29: {28: 1, 30: 3},
        30: {26: 7, 29: 3, 31: 4},
        31: {30: 3, 32: 3},
        32: {31: 3, 33: 5, 48: 12},
        33: {32: 5, 34: 5, 47: 2},
        34: {33: 5, 35: 6, 46: 4},
        35: {34: 6, 36: 3},
        36: {26: 8, 35: 3},
        37: {23: 5, 38: 1, 46: 6},
        38: {37: 1, 39: 3},
        39: {38: 3, 40: 1, 41: 5},
        40: {21: 5, 39: 1},
        41: {39: 5, 42: 1},
        42: {41: 1, 43: 2},
        43: {42: 2, 44: 3, 74: 4},
        44: {43: 3, 45: 2, 68: 7},
        45: {44: 2, 46: 1, 70: 12},
        46: {34: 4, 37: 6, 45: 1, 72: 12},
        47: {33: 2, 53: 6, 73: 5},
        48: {32: 12, 49: 4},
        49: {48: 4, 50: 5},
        50: {49: 5, 51: 3},
        51: {50: 3, 52: 6},
        52: {51: 6, 53: 3},
        53: {47: 6, 52: 3, 54: 6},
        54: {53: 6, 55: 4},
        55: {54: 4, 56: 3, 72: 1},
        56: {55: 3, 57: 6},
        57: {56: 6, 58: 2, 69: 1},
        58: {57: 2, 66: 4, 59: 1},
        59: {58: 2, 60: 3},
        60: {59: 3, 61: 3, 67: 4},
        61: {60: 3, 62: 1},
        62: {61: 2, 63: 4},
        63: {62: 4, 64: 3},
        64: {63: 3, 65: 5},
        65: {64: 5, 66: 2, 75: 3},
        66: {58: 4, 65: 2, 67: 4, 68: 3},
        67: {60: 4, 66: 4},
        68: {44: 7, 66: 3, 69: 4, },
        69: {69: 4, 57: 1, 70: 1},
        70: {45: 12, 69: 1, 71: 3},
        71: {70: 3, 72: 5},
        72: {46: 12, 55: 1, 71: 5, 73: 1},
        73: {47: 5, 72: 1},
        74: {43: 4, 75: 1},
        75: {65: 3, 74: 1}
    }

    # create source and destination values
    s = random.randint(1, 75)  # randomised source
    d = random.randint(1, 75)  # randomised destination
    if d == s:  # randomises d again if same as source
        d = random.randint(1, 75)

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
                Gprime[node].pop(P1[nexInd])  # pops the given path option of out of the list for the given node in G
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