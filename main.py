from graph import *
from graph_csv import *


# g = Graph(l,False)
# g.addConnection("A","B", 3)
# g.addConnection("A","C", 4)
# g.addConnection("A","D", 1)
# g.addConnection("B","D", 2)

# # print(g.getWeightMatrix())


# g2 = Graph(l, True)
# g2.addConnection("A","B", 2)
# g2.addConnection("B","D", 1)
# g2.addConnection("D","C", 3)
# g2.addConnection("A","C", 4)

# print(g2.getWeightMatrix())

g = readCSV("Graph.csv")
print(g.getWeightMatrix())
writeCSV("graph-output.csv",g)



