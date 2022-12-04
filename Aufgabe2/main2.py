#   Beginn Aufgabe 2 - Algorithmische Geometrie

from xQueue import *
from avl import *


# Liste aus Tuplen
# data = XQueue()

# data.readData("Aufgabe2\datapoints.csv")

# print(data.getData())

# print("Distanz:", data.calculateEuclidMetric(data.getData()[0], data.getData()[1]))


avl = AVL()
root = None

root = avl.insertNode(root, 17)
root = avl.insertNode(root, 10)
root = avl.insertNode(root, 25)
root = avl.insertNode(root, 12)
root = avl.insertNode(root, 22)
root = avl.insertNode(root, 28)
root = avl.insertNode(root, 22)
root = avl.insertNode(root, 23)
root = avl.insertNode(root, 26)
root = avl.insertNode(root, 29)
root = avl.insertNode(root,14)

avl.preOrder(root)