class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def insert(self, newNode):
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


# Node => data, next
firstNode = Node("John")
LinkedList = LinkedList()
#LinkedList.insert(firstNode)
secondNode = Node("Ben")
#LinkedList.insert(s1econdNode)
thirdNode = Node("Matthew")
#LinkedList.insert(thirdNode)
Node1 = Node("Dave")
LinkedList.insert(Node1)
LinkedList.printList()