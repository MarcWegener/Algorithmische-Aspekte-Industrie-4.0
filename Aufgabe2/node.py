class Node(object):

    def __init__(self, value) -> None:
        self.__value = value
        self.__lChild = None
        self.__rChild = None
        self.__height = 1

    def getValue(self):
        return self.__value

    def setValue(self,value):
        self.__value = value
    
    value = property(getValue,setValue)


    def getLChild(self):
        return self.__lChild

    def setLChild(self,lChild):
        self.__lChild = lChild
    
    lChild = property(getLChild,setLChild)


    def getRChild(self):
        return self.__rChild

    def setRChild(self,rChild):
        self.__rChild = rChild
    
    rChild = property(getRChild,setRChild)


    def getHeight(self):
        return self.__height

    def setHeight(self,height):
        self.__height = height
    
    height = property(getHeight,setHeight)