#   Beginn Aufgabe 2 - Algorithmische Geometrie

from xQueue import *

# Liste aus Tuplen
data = XQueue()

data.readData("Aufgabe2\datapoints.csv")

print(data.getData())

print("Distanz:", data.calculateEuclidMetric(data.getData()[0], data.getData()[1]))