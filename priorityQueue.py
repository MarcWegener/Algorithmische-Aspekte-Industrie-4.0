class PriorityQueue(object):
    
    def __init__(self):
        self.__queue = []

    def push(self, t):
        bool = True
        # Überprüfung ob ein Knoten bereits in der Queue vorhanden ist,
        # falls ja wird überprüft, ob das aktuelle Kantengewicht des Knotens 
        # unterboten werden kann
        for tup in self.__queue:
           
            if t[2] == tup[2] and t[0] < tup[0]:
                self.__queue.remove(tup)
            elif t[2] == tup[2] and t[0] >= tup[0]:
                bool = False
        
        if bool:
            self.__queue.append(t)   
            self.__sortQueue()
            self.printQueue()

    def popQueue(self):
        element = self.__queue.pop(0)
        self.__sortQueue()
        print(f"Element gepoppt: {element}")
        self.printQueue()
        return element

    def __sortQueue(self):
            self.__queue.sort()
            # self.printQueue()

    def printQueue(self):
        print(self.__queue)

    def queueLen(self):
        return len(self.__queue)