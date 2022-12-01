from graph import *
from graph_csv import *
from priorityQueue import *


# # g = Graph(l,False)
# # g.addConnection("A","B", 3)
# # g.addConnection("A","C", 4)
# # g.addConnection("A","D", 1)
# # g.addConnection("B","D", 2)

# # # print(g.getWeightMatrix())


# # g2 = Graph(l, True)
# # g2.addConnection("A","B", 2)
# # g2.addConnection("B","D", 1)
# # g2.addConnection("D","C", 3)
# # g2.addConnection("A","C", 4)

# # print(g2.getWeightMatrix())

# # Aufgabe 2
# # g = readCSV("Graph.csv")
# # print(g.getWeightMatrix())
# # writeCSV("graph-output.csv",g)


# Aufgabe 3

def solvePrim(g, currentNodeName):

    mstWeight = 0
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

# count < len(g.nodes) - 1

    # Abbruchbedingung: PQ ist leer
    while(pq.queueLen() != 0):

        # Entfernen des ersten Elements
        y = pq.popQueue()
        if y[2] not in usedNodes:
            usedNodes.append(y[2])
            mst.addConnection(y[1], y[2], y[0])
        print("Used Nodes:", usedNodes)
        currentNodeName = y[2]
        currentNodeIndex = g.nodes.index(y[2])
        mstWeight += y[0]

        # Von dem Startknoten aus wird jeder Knoten der Knotenmenge von G durchlaufen
        for i in range(len(g.nodes)):

            # Wenn Kantengewicht nicht Unendlich (None) oder 0 ist (selber Knoten)
            # wird der Knoten ausgehend von dem aktuell betrachteten Knoten in die PQ eingefügt
            nextNodeName = g.nodes[i]
            edgeWeight = g.m[currentNodeIndex][i]

            if edgeWeight is not None and edgeWeight > 0 and nextNodeName not in usedNodes:
                pq.push((edgeWeight, currentNodeName, nextNodeName))

    return mst, mstWeight


# Aufgabe 4:

def solveHierholzer(mst, currentNode):

    usedNodes = []
    tour = []

    nextNodes = [currentNode]

    while(len(nextNodes) != 0):
        currentNode = nextNodes.pop(0)
        currentNodeIndex = mst.nodes.index(currentNode)
        row = mst.m[currentNodeIndex]

        count = 0
        for i in row:

            nextNode = mst.nodes[count]
         # iterativer Ansatz
            if i is not None and i > 0 and nextNode not in usedNodes:

                if currentNode in tour:
                        x = tour.index(currentNode)
                        l1 = tour[:x]
                        l2 = tour[x+1:]
                        l1.extend([currentNode, nextNode, currentNode])
                        l1.extend(l2)
                        tour = l1
                else:
                    tour.append(currentNode)
                    tour.append(nextNode)
                    tour.append(currentNode)

                nextNodes.append(nextNode)
                # print(nextNodes)

            count+=1
            # print(tour)
        
        usedNodes.append(currentNode)   
        
        
    # Tour (Liste) wird in eine dict übersetzt (darf keine Dopplung enthalten), 
    # um doppelte Werte zu entfernen, dann erfolgt die Rückübersetzung in eine Liste
    # zuletzt wird noch der Startknoten wieder an das Ende angefügt
    cleanedTour = list(dict.fromkeys(tour))
    cleanedTour.append(tour[0])


    print(cleanedTour)   

        # Pseudo rekursiv:
        # def solveTSP(mst,currentNode,lastNode):

        #
        # currentNodeIndex = mst.nodes.index(currentNode)
        # row = mst.m[currentNodeIndex]
        # count = 0
        # for i in row:
        # if i is not None and i > 0 and:
        #   lastNode = mst.nodes[count]
        #  solveTSP(mst,lastNode,currentNode)
        # count+=1
        # return tour+=lastNode
     


    




def main():

    # Aufgabe 3:

    # g = readCSV("Graph3.csv")
    # mst, mstWeight = solvePrim(g, 'A')
    # print("MST: Gewicht: ", mstWeight)
    # for i in mst.getWeightMatrix():
    #     print(i)


    # Aufgabe 4:

    g = readCSV("Aufgabe1\Graph4.csv")
    mst, mstWeight = solvePrim(g, 'A')
    
    print("MST: Gewicht: ", mstWeight)
    print("MST: ")
    for i in mst.getWeightMatrix():
        print(i)

    tour = solveHierholzer(mst, 'A')


    

# nimmt Graphen und Startknoten als String an z.B. 'A'





if __name__ == "__main__":
    main()





