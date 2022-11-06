from graph import *
import csv

def readCSV(filename,direction=False):
    with open(filename) as csvdatei:
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


def writeCSV(filename,graph):
   with open(filename,"w",encoding="UTF8",newline='') as f:
    writer = csv.writer(f)
    writer.writerow(graph.nodes)
    for i in graph.getWeightMatrix():
        writer.writerow(i)
        

          