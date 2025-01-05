class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.prev = None 
    

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node
        self.length = 1 

    def print_DLL(self):

        tmp = self.head 
        while tmp.next is not None:
            print(tmp.value, "<-> ", end='')
            tmp = tmp.next 

        print(tmp.value)

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node 
            self.tail = new_node 
        else:
            new_node.prev = self.tail
            self.tail.next = new_node 
            self.tail = new_node 
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None 
        
        tmp = self.tail 

        if self.head is not None and self.head.next is None:
            self.head = None 
            self.tail = None 
        else:
            self.tail = self.tail.prev 
            self.tail.next = None 
            tmp.prev = None 
        self.length -= 1 
        return tmp 
    
    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node 
            self.tail = new_node 
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 
        self.length += 1 
        return True
    
    def pop_first(self):
        if self.head is None:
            return None 
        
        tmp = self.head 
        if self.head is not None and self.head is None:
            self.head = None 
            self.tail = None 
        else:
            self.head = self.head.next 
            self.head.prev = None 
            tmp.next = None 
        self.length -= 1 
        return tmp 
    
    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None 

        if index < self.length / 2:
            tmp = self.head 
            for _ in range(index):
                tmp = tmp.next 
        else:
            tmp = self.tail 
            for _ in range(self.length - 1, index, -1):
                tmp = tmp.prev 
        return tmp
    
    def set_value(self, index, value):
        tmp = self.get_value(index)

        if tmp:
            tmp.value = value 
            return True 
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False 
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)

        before = self.get_value(index - 1)
        after = before.next 


        new_node.prev = before
        before.next = new_node 

        new_node.next = after 
        after.prev = new_node
        
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None 

        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        

        before = self.get_value(index-1)
        tmp = before.next 
        after = tmp.next 

        before.next = after 
        after.prev = before 

        tmp.next = None 
        tmp.prev = None 
        self.length -= 1 
        return tmp
                  
    
# dll = DoublyLinkedList(2)

# dll.append(3)

# dll.append(4)

# print(dll.pop().value)

# dll.prepend(1)


# dll.insert(1, 15)

# dll.print_DLL()
