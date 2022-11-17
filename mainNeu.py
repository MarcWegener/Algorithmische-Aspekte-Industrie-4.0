from graph import *
from graph_csv import *
from priorityQueue import *


# Aufgabe 3
def solvePrim(g, currentNodeName):
    pq = PriorityQueue()
    usedNodes = []

    currentNodeIndex = g.nodes.index(currentNodeName)
    edgeWeight = 0

    nextNodeName = currentNodeName

    # Einfügen in PQ erfolgt immer als Tuple (Distanz bzw. Kantengewicht, Knotenname)
    # Einfügen des Startknotens in die PQ. Jeder Startknoten hat zu sich selber die Distanz von 0
    pq.push((0, currentNodeName, nextNodeName))

    # Untergraph von G: MST, also gleiche Knotenmenge und in diesem Fall ungerichtet
    mst = Graph(g.nodes, False)

#count < len(g.nodes) - 1

    # Abbruchbedingung: PQ ist leer
    while(pq.queueLen() != 0):

        # Entfernen des ersten Elements
        y = pq.popQueue()
        if y[2] not in usedNodes:
            usedNodes.append(y[1])
            mst.addConnection(currentNodeName, nextNodeName, y[0])
        print("Used Nodes:",usedNodes)

        # Von dem Startknoten aus wird jeder Knoten der Knotenmenge von G durchlaufen
        for i in range(len(g.nodes)):
        
            # Wenn Kantengewicht nicht Unendlich (None) oder 0 ist (selber Knoten)
            # wird der Knoten ausgehend von dem aktuell betrachteten Knoten in die PQ eingefügt
            edgeWeight = g.m[currentNodeIndex][i]
            if edgeWeight is not None and edgeWeight > 0:
                nextNodeName =  g.nodes[i]
                pq.push((edgeWeight, currentNodeName, nextNodeName))

            

        

        


    return mst

g = readCSV("Graph3.csv")
mst = solvePrim(g, 'A')
for i in mst.getWeightMatrix():
    print(i)

# nimmt Graphen und Startknoten als String an z.B. 'A'