from pydantic import BaseModel 
from typing import Union

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

    def return_LL(self):

        tmp = self.head 
        returned = ""
        while tmp.next is not None:
            returned += str(tmp.value) + ' -> '
            tmp = tmp.next 
        returned += str(tmp.value) 
        return returned 


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
        return tmp
    
    def set_value(self, index, value):

        if index < 0 or index >= self.length:
            return False 

        tmp = self.head 

        for _ in range(index):
            tmp = tmp.next 

        tmp.value = value
        return True
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Index is out of bounds!")
            return False 
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)


        new_node = Node(value)
        
        tmp = self.get_value(index - 1)
        
        new_node.next = tmp.next 
        tmp.next = new_node 
        self.length += 1
        return True 
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            print("Index is out of bounds!")
            return None 
        if index == 0:
            return self.pop_first() 
        if index == self.length - 1:
            return self.pop() 
        
        prev = self.get_value(index - 1)
        tmp = prev.next 

        prev.next = tmp.next 
        tmp.next = None 

        self.length -= 1
        return tmp 
    
    def reverse(self):

        tmp = self.head 
        self.head = self.tail 
        self.tail = tmp 

        before = None 

        for _ in range(self.length):
            after = tmp.next 
            tmp.next = before 
            before = tmp 
            tmp = after 


        

     


               


class LLValue(BaseModel):
    value: Union[str, int, float]





# ll = LinkedList(2)

# ll.append(35)
# ll.append(3)

# ll.insert(1, 6)

# ll.print_LL()

# print(ll.get_value(1).value)

# ll.remove(1)

# ll.print_LL()