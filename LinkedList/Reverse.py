class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    ## Reverse function
    def reverseList(self):
        temp = self.head
        prev = None
        
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        
        self.head = prev  

ll = LinkedList()

n = int(input("Enter number of elements: "))

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    ll.insert(val)

print("\nOriginal Linked List:")
ll.display()

ll.reverseList()

print("Reversed Linked List:")
ll.display()