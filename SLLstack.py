class SLLstack:
    class Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next
        
    def __init__(self):
        self.head = None
        self.size = 0
    
    def len_stack(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    
    def push(self, element):
        self.head = self.Node(element, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("stack is empty")
            pass
        result = self.head.element
        self.head = self.head.next
        return result
    
    def peek(self):
        if self.is_empty():
            print("stack is empty")
            pass
        return self.head.element

s = SLLstack()
s.push('One')
s.push('Two')
print(s.pop())
print(s.peek()