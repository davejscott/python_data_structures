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
    
    def insertNode(self, newNode):
        # data => Matt, next  => None
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode

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
LinkedList.insertEnd(Node1)
Node2 = Node(20)
LinkedList.insertEnd(Node2)
LinkedList.printList()
print(LinkedList.size)