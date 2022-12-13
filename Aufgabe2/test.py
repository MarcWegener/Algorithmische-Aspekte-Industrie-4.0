from avl import *

# Test Zone

# #   Initialisieren der xQueue
#     # Liste aus Tuplen
# q = XQueue()
# q.readData("Aufgabe2\datapoints.csv")

# xq = q.getData()

# # Initialisieren der y-Werte als AVL-Baum
avl = AVL()
root = None

root = avl.insertNode(root, (1,17))
root = avl.insertNode(root, (1,10))
root = avl.insertNode(root, (1,25))
root = avl.insertNode(root, (1,12))
root = avl.insertNode(root, (1,22))
root = avl.insertNode(root, (1,28))
root = avl.insertNode(root, (1,20))
root = avl.insertNode(root, (1,23))
root = avl.insertNode(root, (1,26))
root = avl.insertNode(root, (1,29))

root = avl.deleteNode(root,(1,12))
avl.preOrder(root)
# temp = root
# temp = avl.searchNode(temp, (1,22))

# print(root.value)
# print(temp.rChild.value)

