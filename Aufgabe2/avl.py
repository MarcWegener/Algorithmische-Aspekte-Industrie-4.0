from node import *

class AVL(object):

    def insertNode(self, root, value):
        if not root:
            return Node(value)
        elif value[1] < root.value[1]:
            root.lChild = self.insertNode(root.lChild, value)
        else:
            root.rChild = self.insertNode(root.rChild, value)

        # Gewicht der "aktuellen" Wurzel wird um 1 erhöht
        root.height = 1 + max(self.getHeight(root.lChild), self.getHeight(root.rChild))

        # Balance Faktor wird ermittelt
        balance = self.getBalance(root)

        # Wenn kleiner als -1, also unbalanciert nach links
        if balance < -1:
            # Wenn Wert des eingefügten Knotens kleiner ist als der der aktuellen root
            # also im linken Teilbaum der root eingefügt wurde
            if value[1] > root.rChild.value[1]:
                # Dann muss nach rechts ausgeglichen werden
                return self.leftRotation(root)
                # Sonst wurde der neue Knoten im rechten Teilbaum eingefügt und 
                # es erfolgt eine doppel Rotation
            else:
                # rechts-links Rotation
                root.rChild = self.rightRotation(root.rChild)
                return self.leftRotation(root)
        # Wenn größer als 1, also unbalanciert nach rechts 
        if balance > 1:
            # Wenn Wert des eingefügten Knotens größer ist als der Wert der aktuellen root
            # also im rechten Teilbaum der root eingefügt wurde
            if value[1] < root.lChild.value[1]:
                return self.rightRotation(root)
            else:
                # links-rechts Rotation
                root.lChild = self.leftRotation(root.lChild)
                return self.rightRotation(root)

        return root

    def deleteNode(self, root, value):

        if not root:
            return root
        elif value[1] < root.value[1]:
            root.lChild = self.deleteNode(root.lChild, value)
        elif value[1] > root.value[1]:
            root.rChild = self.deleteNode(root.rChild, value)
        else:
            # Rekursionsanker der deleteNode Methode

            # Es ist nicht möglich noch weiter nach links zu gehen
            if root.lChild is None:
                # rechter Knoten der übergebenen Node wird als Nachfolger festgelegt
                temp = root.rChild
                # root wird auf None gesetzt und somit ist die Node aus dem Baum entfernt
                root = None
                # Nachfolger wird zurückgegeben
                return temp

            elif root.rChild is None:
                temp = root.lChild
                root = None
                return temp

            temp = self.getSuccessor(root.rChild)
            root.value = temp.value
            root.rChild = self.deleteNode(root.rChild, temp.value)

        if root is None:
            return root

        # Gewicht der "aktuellen" Wurzel wird um 1 erhöht
        root.height = 1 + max(self.getHeight(root.lChild), self.getHeight(root.rChild))

        # Balance Faktor wird ermittelt
        balance = self.getBalance(root)

         # Wenn kleiner als -1, also unbalanciert nach links
        if balance < -1:
            # Wenn Wert des eingefügten Knotens kleiner ist als der der aktuellen root
            # also im linken Teilbaum der root eingefügt wurde
            if self.getBalance(root.rChild) <= 0:
                # Dann muss nach rechts ausgeglichen werden
                return self.leftRotation(root)
                # Sonst wurde der neue Knoten im rechten Teilbaum eingefügt und 
                # es erfolgt eine doppel Rotation
            else:
                # rechts-links Rotation
                root.rChild = self.rightRotation(root.rChild)
                return self.leftRotation(root)
        # Wenn größer als 1, also unbalanciert nach rechts 
        if balance > 1:
            # Wenn Wert des eingefügten Knotens größer ist als der Wert der aktuellen root
            # also im rechten Teilbaum der root eingefügt wurde
            if self.getBalance(root.lChild) >= 0:
                return self.rightRotation(root)
            else:
                # links-rechts Rotation
                root.lChild = self.leftRotation(root.lChild)
                return self.rightRotation(root)

        return root

        
    def searchNode(self, root, value):
        if root is None or root.value == value:
            return root
        elif value[1] < root.value[1]:
            # print(root.value)
            return self.searchNode(root.lChild, value)
        elif value[1] > root.value[1]:
            # print(root.value)
            return self.searchNode(root.rChild, value)
        


    # Methode zur Ermittlung des Nachfolgers
    def getSuccessor(self,root):
        # Wenn None übergeben oder lChild von der übergebenen Node None ist wird
        # der aktuelle Knoten zurückgegeben
        # der übergebene Knoten ist root.rChild
        # wenn lChild dann None ist ist der Nachfolger der ursprünglichen Node
        # also die Node direkt rechts davon der Nachfolger
        if root is None or root.lChild is None:
            return root
        # Alternativ wird nachdem einmal nach rechts gegangen wurde (Übergabe ist root.rChild)
        # wird soweit wie möglich nach links gegangen um den Nachfolger der ursprünglichen
        # Node zu finden
        return self.getSuccessor(root.lChild)


    def getPredecessor(self,root):
        if root is None or root.rChild is None:
            return root
        return self.getPredecessor(root.rChild)


    def getHeight(self, root):
        if not root:
            return 0
        
        return root.height

    # Methode zur Ermittlung des Balance Faktors
    def getBalance(self, root):

        # Also wenn Blattknoten:
        if not root:
            return 0
        
        # rechts - links wie aus Vorlesung AD:
        # Tiefe des rechten Teilbaums minus die Höhe des linken Teilbaums
        return self.getHeight(root.lChild) - self.getHeight(root.rChild)

    #  Rechtsrotation nimmt Knoten an
    def rightRotation(self, node):

        #  linker Knoten des übergebenen Knotens wird in einer Hilfsvar gespeichert
        help = node.lChild
        # rechter Teilbaum wird in einer Hilfsvar gespeichert
        rightTree = help.rChild
        # übergebener Knoten wird rechts von dem Hilfsknoten eingefügt
        help.rChild = node
        # ursprünglicher rechter Teil des Hilfsknotens wird links an den übergebenen
        # (nun rechts von dem Hilfsknoten stehenden) übergebenen Knoten angehangen
        node.lChild = rightTree

        # Höhen werden angepasst:
        node.height = 1 + max(self.getHeight(node.lChild), self.getHeight(node.rChild))
        help.height = 1 + max(self.getHeight(help.lChild), self.getHeight(help.rChild))

        # Hilfsknoten wird zurückgegeben und nimmt so die Position des übergebenen Knotens ein
        return help


    #  Linksrotation nimmt Knoten an
    def leftRotation(self, node):

        #  rechter Knoten des übergebenen Knotens wird in einer Hilfsvar gespeichert
        help = node.rChild
        # linker Teilbaum wird in einer Hilfsvar gespeichert
        leftTree = help.lChild
        # übergebener Knoten wird links von dem Hilfsknoten eingefügt
        help.lChild = node
        # ursprünglicher linker Teil des Hilfsknotens wird rechts an den übergebenen
        # (nun links von dem Hilfsknoten stehenden) übergebenen Knoten angehangen
        node.rChild = leftTree

        # Höhen werden angepasst:
        node.height = 1 + max(self.getHeight(node.lChild), self.getHeight(node.rChild))
        help.height = 1 + max(self.getHeight(help.lChild), self.getHeight(help.rChild))

        # Hilfsknoten wird zurückgegeben und nimmt so die Position des übergebenen Knotens ein
        return help

    
    def preOrder(self, root):
    
        if not root: 
            return
        
        print(root.value, end=", ")
        self.preOrder(root.lChild)
        self.preOrder(root.rChild)