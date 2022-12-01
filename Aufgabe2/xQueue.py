# Liste aus Tuplen

import csv, math

class XQueue(object):

    def __init__(self):
        self.__data = []

    def readData(self, filename):
        with open(filename) as csvdatei:
            csv_reader_object = csv.DictReader(csvdatei)
            for row in csv_reader_object:
                self.__data.append((float(row["x"]), float(row["y"])))

        self.__data.sort(key=lambda tup:tup[0])

    def getData(self):
        return self.__data

    def calculateEuclidMetric(self,p,q):
        dist = math.sqrt(math.pow((p[0] - q[0]),2) + math.pow((p[1] - q[1]),2))
        return dist