class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node 
        self.last = new_node 
        self.length = 1
        
    def print_queue(self):
        tmp = self.first

        print("Front")
        print("|")
        print("v")
        string = ''
        while tmp.next is not None:
            string += str(tmp.value) + ' -> '
            tmp = tmp.next 
        string += str(tmp.value)
        
        print(string)
        back_pos = len(string) - len(str(tmp.value)) - 1
        print(back_pos * ' ', '^')
        print(back_pos * ' ', '|')
        print((back_pos - 3) * ' ', 'Back')
        
        
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node 
            self.last = new_node 
        else:
            self.last.next = new_node 
            self.last = new_node 
            
        self.length += 1
        return True 
    
    def dequeue(self):
        
        if self.first is None:
            return None 

        tmp = self.first
        
        if self.first is not None and self.first.next is None:
            self.first = None 
            self.last = None 
        else:
            self.first = self.first.next 
            tmp.next = None 
        self.length -= 1 
        return tmp 
    


queue = Queue(3)

queue.enqueue(52)
queue.enqueue(7)

queue.print_queue()
            
queue.enqueue(434)
queue.enqueue(3)

queue.print_queue()

queue.dequeue()

queue.print_queue()