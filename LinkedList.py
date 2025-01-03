from pydantic import BaseModel 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node
        self.length = 1

    def print_LL(self):
        tmp = self.head 

        while tmp.next is not None:
            print(tmp.value, '->', end = ' ')
            tmp = tmp.next 
        print(tmp.value)

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node 
            self.tail = new_node 
        else:
            self.tail.next = new_node 
            self.tail = new_node 
        self.length += 1
        return True 
    
    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node 
            self.tail = new_node 
        else:
            new_node.next = self.head 
            self.head = new_node 
        self.length += 1
        return True

    def pop(self):

        if self.head is None:
            print('Nothing to pop! LinkedList is empty!')
            return None
        
        tmp = self.head

        if self.head is not None and self.head.next is None:
            self.head = None 
            self.tail = None 
        else:
            while tmp.next is not None:
                prev = tmp 
                tmp = tmp.next
            self.tail = prev 
            self.tail.next = None 
        self.length -= 1
        return tmp
    
    def pop_first(self):
        
        if self.head is None: 
            return None 

        tmp = self.head 
        if self.head is not None and self.head.next is None:
            self.head = None 
            self.tail = None 
        else:
            self.head = self.head.next 
            tmp.next = None 
        self.length -= 1
        return tmp
             
    def get_value(self, index):
        
        if index < 0 or index >= self.length:
            return None

        tmp = self.head

        for _ in range(index):
            tmp = tmp.next
        return tmp.value
    
    def set_value(self, index, value):

        if index < 0 or index >= self.length:
            return False 

        tmp = self.head 

        for _ in range(index):
            tmp = tmp.next 

        tmp.value = value
        return True
    

ll = LinkedList(3)

ll.append(2)
ll.append(5) 

ll.prepend(4)
ll.prepend(14)

ll.pop()

ll.pop_first()

ll.print_LL()

print(ll.get_value(2))