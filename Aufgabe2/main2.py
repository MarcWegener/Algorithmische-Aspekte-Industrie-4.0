#   Beginn Aufgabe 2 - Algorithmische Geometrie

from xQueue import *
from avl import *

def checkSuccessor(delta, q, root, avl, value):
    
    # Knoten aus Baum mit Wert des Tuples wird im Baum gesucht und als Node zurückgegeben
    node = avl.searchNode(root, value)
    
    # print(f"Successor Node: {node.value}")

    check = node
    print(f"checkS: {check.value}")

    if check.rChild:
        check = avl.getSuccessor(check.rChild)
    else:
        return delta

    print(f"checkS2: {check.value}")
    print(f"nodeS2: {node.value}")
    newDelta = q.calculateEuclidMetricDistance(node.value, check.value)

    if newDelta < delta:
        delta = newDelta

    while check.value[1] - node.value[1] >= delta:
        check = avl.getSuccessor(check.rChild)
        newDelta = q.calculateEuclidMetricDistance(node.value, check.value)

        if newDelta < delta:
            delta = newDelta

    return delta

def checkPredecessor(delta, q, root, avl, value):
    
    node = avl.searchNode(root, value)
    
    # print(f"Predecessor Node: {node.value}")
    check = node
    print(f"checkP: {check.value}")

    if check.lChild:
        check = avl.getPredecessor(check.lChild)
    else:
        return delta

    newDelta = q.calculateEuclidMetricDistance(node.value, check.value)

    if newDelta < delta:
        delta = newDelta

    while check.value[1] - node.value[1] >= delta:
        check = avl.getPredecessor(check.lChild)
        newDelta = q.calculateEuclidMetricDistance(node.value, check.value)

        if newDelta < delta:
            delta = newDelta

    return delta


def closestPair():

    #   Initialisieren der xQueue
    # Liste aus Tuplen
    q = XQueue()
    q.readData("Aufgabe2\datapoints.csv")

    xq = q.getData()

    # Initialisieren der y-Werte als AVL-Baum
    avl = AVL()
    root = None

    # Initialisiere delta
    global delta
    delta = q.calculateEuclidMetricDistance(xq[0], xq[1])
    

    # Einfügen der ersten beiden y-Werte in den Baum
    root = avl.insertNode(root, xq[0])
    root = avl.insertNode(root, xq[1])

    tail = 0
    current = 1
    

    while (current < len(xq) - 1):

        current += 1
        # print(f"current: {current}")

        while(xq[current][0] - xq[tail][0] >= delta) and (tail < current):
            root = avl.deleteNode(root, xq[tail])
            tail += 1
            # print(f"tail: {tail}")

        root = avl.insertNode(root, xq[current])
        delta = checkSuccessor(delta, q, root, avl, xq[current])
        delta = checkPredecessor(delta, q, root, avl, xq[current])

    return delta

delta = closestPair()

print(f"delta: {delta}")



# Test Zone

# #   Initialisieren der xQueue
#     # Liste aus Tuplen
# q = XQueue()
# q.readData("Aufgabe2\datapoints.csv")

# xq = q.getData()

# # Initialisieren der y-Werte als AVL-Baum
# avl = AVL()
# root = None

# root = avl.insertNode(root, (1,17))
# root = avl.insertNode(root, (1,10))
# root = avl.insertNode(root, (1,25))
# root = avl.insertNode(root, (1,12))
# root = avl.insertNode(root, (1,22))
# root = avl.insertNode(root, (1,28))
# root = avl.insertNode(root, (1,20))
# root = avl.insertNode(root, (1,23))
# root = avl.insertNode(root, (1,26))
# root = avl.insertNode(root, (1,29))

# # avl.preOrder(root)

# root = avl.searchNode(root, (1,23))
# print(root.value)