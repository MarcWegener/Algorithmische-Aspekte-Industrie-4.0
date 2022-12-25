#   Beginn Aufgabe 2 - Algorithmische Geometrie

from xQueue import *
from avl import *
import copy

def checkSuccessor(delta, q, root, avl, value):
    print(f"root:{root.value}")
    # Knoten aus Baum mit Wert des Tuples wird im Baum gesucht und als Node zurückgegeben
    node = avl.searchNode(root, value)
    
    #Kopie des Knotens angelegt, da "Unendlichkeitsknoten" nicht in den Ursprungsbaum eingefuegt werden darf
    check = copy.deepcopy(node)
    #print(f"checkS: {check.value}")

    if check.rChild is None:
        check.rChild = Node((9999,9999))

    check = avl.getSuccessor(check.rChild)

    newDelta = q.calculateEuclidMetricDistance(node.value, check.value)
    if newDelta < delta:
            delta = newDelta
    print(check.value[1] - node.value[1])
    while check.value[1] - node.value[1] < delta:
        if check.rChild:
            check = avl.getSuccessor(check.rChild)
        else:
            check.rChild = Node((9999,9999))
            check = check.rChild
        newDelta = q.calculateEuclidMetricDistance(node.value, check.value)
        #check = avl.getSuccessor(check.rChild)
        print(f"check-Value:{check.value}")
        print(f"newDeltaS: {newDelta}")

        if newDelta < delta:
            delta = newDelta

    print(f"root nach Succ:{root.value}")
    return delta

def checkPredecessor(delta, q, root, avl, value):
    print(f"root:{root.value}")
    node = avl.searchNode(root, value)
    
    #Kopie des Knotens angelegt, da "Unendlichkeitsknoten" nicht in den Ursprungsbaum eingefuegt werden darf
    check = copy.deepcopy(node)

    if check.lChild is None:
        check.lChild = Node((-9999,-9999))
    check = avl.getPredecessor(check.lChild)

    newDelta = q.calculateEuclidMetricDistance(node.value, check.value)
    if newDelta < delta:
            delta = newDelta
    print(node.value[1] - check.value[1])
    while node.value[1] - check.value[1] < delta:
        if check.lChild:
            check = avl.getPredecessor(check.lChild)
        else:
            check.lChild = Node((-9999,-9999))
            check = check.lChild
        newDelta = q.calculateEuclidMetricDistance(node.value, check.value)
        print(f"check-Value:{check.value}")
        #check = avl.getPredecessor(check.lChild)
        print(f"newDeltaP: {newDelta}")

        if newDelta < delta:
            delta = newDelta

    print(f"root nach Pre:{root.value}")
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
   
    delta = q.calculateEuclidMetricDistance(xq[0], xq[1])
    print(xq[0],xq[1])
    print(f"first delta: {delta}")
    

    # Einfügen der ersten beiden y-Werte in den Baum
    root = avl.insertNode(root, xq[0])
    root = avl.insertNode(root, xq[1])

    tail = 1
    current = 1
    

    while (current < len(xq) - 1):

        current += 1
        print(f"current: {xq[current]}")

        while(xq[current][0] - xq[tail][0] >= delta) and (tail < current):
            root = avl.deleteNode(root, xq[tail])
            tail += 1
            print(f"tail: {xq[tail]}")

        root = avl.insertNode(root, xq[current])
        print("AVL Preorder:")
        avl.preOrder(root)
        print("\n")
        delta = checkSuccessor(delta, q, root, avl, xq[current])
        delta = checkPredecessor(delta, q, root, avl, xq[current])
        print(f"delta: in while:  {delta}")
    return delta

delta = closestPair()

print(f"delta: {delta}")


# q = XQueue()
# q.readData("Aufgabe2\datapoints.csv")

# xq = q.getData()

# min = 99999
# a = 0
# b = 0
# for i in range(len(xq)):
#     for j in range(len(xq)):
#         delta = q.calculateEuclidMetricDistance(xq[i],xq[j])
#         if delta > 0.0 and delta <= min:
#             min = delta
#             a = xq[i]
#             b = xq[j]
#         print(delta)


#print(min,a,b)

#Test Zone

#   Initialisieren der xQueue
    # Liste aus Tuplen
# q = XQueue()
# q.readData("Aufgabe2\datapoints.csv")

# xq = q.getData()

# Initialisieren der y-Werte als AVL-Baum
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