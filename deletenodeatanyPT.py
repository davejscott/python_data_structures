class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedList:
    def __init__(self, head=None):
        self.head = None
        self.size = 0

    def insertHead(self, newNode):
        # data => Matt, next  => None
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode
    
    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length
    
    def insertAt(self, newNode, position):
        # head => 10 => 20 => None 
        if position < 0 or position > self.listLength():
            print("Invalid Position")
            return
        if position is 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode =  currentNode.next
            currentPosition += 1

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
        # head =>John->Ben->None
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def deleteEnd(self):
        if self.head is None:
            print("Empty Linked List")
            return
        else:
            lastNode = self.head
            while True:
                if lastNode.next.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = None

    def deleteHead(self):
        if self.head is None:
            print("Empty Linked List")
            return
        else:
            firstNode = self.head
            self.head = firstNode.next

    def deleteAt(self, position):
        if position < 0 or position > self.listLength():
            print("Invalid Position")
            return
        if position is 0:
            self.deleteHead()
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1


    def deleteEnd2(self):
        if self.head is None:
            print("Empty Linked List")
            return
        else:
            lastNode = self.head
            while lastNode.next is not None:
                previousNode = lastNode
                lastNode = lastNode.next
            previousNode.next = None

    def printList(self):
    #  head=> John -> Ben -> Matthew-> None
        if self.head is None:
            print("Linked List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
            self.size += 1


# Node => data, next
Node1 = Node(10)
LinkedList =  LinkedList()
LinkedList.insertEnd(Node1)
Node2 = Node(20)
LinkedList.insertEnd(Node2)
Node3 = Node(15)
LinkedList.insertAt(Node3, 1)
LinkedList.deleteAt(1)
LinkedList.printList()
print(LinkedList.size)