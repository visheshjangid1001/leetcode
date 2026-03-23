class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    ## append val in linked list
    def append(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            
    ## Traverse 
    def traverse(self):
        if self.head == None:
            print("sll is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val,end=" ")
                current = current.next
                
    def insert_at(self,val,position):
        new_node = Node(val)
        
                
                
sll = SinglyLinkedList()
sll.append(2)
sll.append(6)
sll.append(10)
sll.append(9)
sll.append(8)
sll.traverse()