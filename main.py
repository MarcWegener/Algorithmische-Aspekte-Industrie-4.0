from graph import *
import csv


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


def readCSV(direction=False):
    with open("Graph.csv") as csvdatei:
        csv_reader_object = csv.DictReader(csvdatei)

        rows = []

        for row in csv_reader_object:
            rows.append(row)

    nodes = []
    for k, v in rows[0].items():
        nodes.append(k)

    print(nodes)

    g = Graph(nodes, direction)
    counter = 0
    for row in rows:
        for k, v in row.items():
            g.addConnection(nodes[counter], k, v)

        counter += 1
    return g


g = readCSV()
print(g.getWeightMatrix())


def writeCSV():
    pass