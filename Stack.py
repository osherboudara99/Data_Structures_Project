class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node 
        self.height = 1 
    
    def print_stack(self):
        tmp = self.top 
        while tmp.next is not None:
            print(tmp.value)
            print(' |')
            print(' v')
            tmp = tmp.next
        print(tmp.value)

    def push(self, value):

        new_node = Node(value)

        if self.top is None:
            self.top = new_node 
        else:
            new_node.next = self.top
            self.top = new_node 
        self.height += 1 
        return True 

    def pop(self):

        if self.top is None:
            return None 
        
        tmp = self.top 

        if self.top is not None and self.top.next is None:
            self.top = None 
        else:
            self.top = self.top.next

        tmp.next = None 
        self.height -= 1 
        return tmp 
    

# stack = Stack(2)

# stack.print_stack()

# stack.push(25)
# stack.push(15)
# stack.push(100)

# stack.print_stack()

# stack.pop()
# stack.pop()

# stack.print_stack()