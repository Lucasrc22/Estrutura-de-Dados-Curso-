class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty_list(self):
        return self.head is None


    def insere_head(self,value):
        new_node = Node()

        if self.empty_list():
            self.head = self.tail = new_node
        
        else:
            new_node.next = self.head

            self.head = new_node
    
    def insere_tail(self, value):
        new_node = Node()
    
        if self.empty_list():
            self.head = self.tail = Node()
        
        else:
            self.tail.next = new_node
            self.tail = new_node