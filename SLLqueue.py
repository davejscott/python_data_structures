class SLLqueue:
    class Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next
        
    def __init__(self):
        self.head = None
        self.tail = None 
        self.size = 0
    
    def len_stack(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, element):
        node = self.Node(element, None)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = new
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            pass
        data = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return data

    
    def first(self):
        if self.is_empty():
            print("stack is empty")
            pass
        return self.head.element

s = SLLqueue()
s.enqueue('One')
s.enqueue('Two')
print(s.dequeue())
print(s.first())
s.enqueue('Six')
print(s.first())
s.dequeue()
print(s.first())