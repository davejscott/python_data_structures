class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedList:
    def __init__(self, head=None):
        self.head = None

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

def mergedLists(firstList, secondList, mergedList):
    # 1->3 -> 4 | 2-> 7 -> 9 | 1->2->3->4-> None
    currentFirst = firstList.head
    currentSecond = secondList.head
    while True:
        if currentFirst is None:
            mergedList.insertEnd(currentSecond)
            break
        if currentSecond is None:
            mergedList.insertEnd(currentFirst)
        if currentFirst.data < currentSecond.data:
            currentFirstNext = currentFirst.next
            currentFirst.next = None
            mergedList.insertEnd(currentFirst)
            currentFirst = currentFirstNext
        else:
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mergedList.insertEnd(currentSecond)
            currentSecond = currentSecondNext

# First List
nodeOne = Node(1)
nodeTwo = Node(3)
nodeThree = Node(4)
firstList = LinkedList()
firstList.insertEnd(nodeOne)
firstList.insertEnd(nodeTwo)
firstList.insertEnd(nodeThree)

# Second List
nodeFour = Node(2)
nodeFive = Node(7)
nodeSix = Node(9)
secondList = LinkedList()
secondList.insertEnd(nodeFour)
secondList.insertEnd(nodeFive)
secondList.insertEnd(nodeSix)

print("First List")
firstList.printList()
print("Second List")
secondList.printList()

mergedList = LinkedList()

mergedLists(firstList, secondList, mergedList)
del firstList
del secondList
print("merged List")
mergedList.printList()