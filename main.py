from graph import *
from graph_csv import *
from priorityQueue import *


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

# Aufgabe 2
# g = readCSV("Graph.csv")
# print(g.getWeightMatrix())
# writeCSV("graph-output.csv",g)


# Aufgabe 3
def solvePrim(g, n):
    pq = PriorityQueue()
    usedNodes = []

    count = 0
    weight = 0

    currentNodeIndex = g.nodes.index(n)
    lastNode = None
    nextNode = None
    x = None

    n1 = None
    n2 = 0

    # Einfügen in PQ erfolgt immer als Tuple (Distanz bzw. Kantengewicht, Knotenname)
    # Einfügen des Startknotens in die PQ. Jeder Startknoten hat zu sich selber die Distanz von 0
    pq.push((0, n))

    # Untergraph von G: MST, also gleiche Knotenmenge und in diesem Fall ungerichtet
    mst = Graph(g.nodes, False)

#count < len(g.nodes) - 1

    # Abbruchbedingung: PQ ist leer
    while(pq.queueLen() != 0):

        # Entfernen des ersten Elements
        y = pq.popQueue()
        if y[1] not in usedNodes:
            usedNodes.append(y[1])
        print("Used Nodes:",usedNodes)

        # minEdgeWeight auf hohen Wert setzten, damit dieses wieder von den Kantengewichten des Graphen unterboten werden kann
        minEdgeWeight = 10*9999
        


        # Von dem Startknoten aus wird jeder Knoten der Knotenmenge von G durchlaufen
        for i in range(len(g.nodes)):
        
            # Wenn Kantengewicht nicht Unendlich (None) oder 0 ist (selber Knoten)
            # wird der Knoten ausgehend von dem aktuell betrachteten Knoten in die PQ eingefügt
            x = g.m[currentNodeIndex][i]

            if x is not None and x > 0:
                
                # Push Tuple aus: (Kantengewicht, )
                # 2. Element Nodeliste an Stelle z.B. Index von Liste A an Stelle an der das min Kantengewicht liegt aus Liste A 

                if g.nodes[g.m[currentNodeIndex].index(x,i)] not in usedNodes:
                    # hier muss noch getestet werden, ob ein Knoten nicht schon im Ausgabegraphen mst enthalten ist
                    print("Betrachteter Knoten:", g.nodes[g.m[currentNodeIndex].index(x,i)], "von", y[1])
                    pq.push((x, g.nodes[g.m[currentNodeIndex].index(x,i)]))

            # Wenn Kantengewicht nicht Unendlich (None) oder 0 ist (selber Knoten) und Kantengewicht kleiner dem
            # bisher kleinsten, gefundenen Kantengewicht entspricht wird dieses aktualisiert
            
            if x is not None and x > 0 and x <= minEdgeWeight and g.nodes[g.m[currentNodeIndex].index(x)] != lastNode:
                minEdgeWeight = x
                lastNode = currentNodeIndex
                nextNode = i
                # print("lastNode:",lastNode)
                # print("nextNode:",nextNode)

        n1 = g.nodes[lastNode]
        n2 = g.nodes[nextNode]
        mst.addConnection(n1, n2, minEdgeWeight)
        currentNodeIndex = nextNode

        


    return mst

g = readCSV("Graph3.csv")
mst = solvePrim(g, 'A')
for i in mst.getWeightMatrix():
    print(i)

# nimmt Graphen und Startknoten als String an z.B. 'A'




