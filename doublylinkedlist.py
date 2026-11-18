class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_end(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("NULL")

    def insert_after(self, target_data, new_data):
        temp = self.head
        while temp:
            if temp.data == target_data:
                new_node = Node(new_data)

        # Link new_node's next to current's next
                new_node.next = temp.next
                new_node.prev = temp
 
        # Adjust next node's prev pointer if it exists
            if temp.next:
                temp.next.prev = new_node

        # Link current node to new node
                temp.next = new_node
                return
            temp = temp.next
        print(f"Element {target_data} not found in the list.")

    def append(self,data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node        
        
    def printlist(self):
        current = self.head
        while current :
            print(end=f"[{current.data}]~>")
            current = current.next
        print("[None]")                    
        
    def insertafterposition(self,prev_data,new_data):
        temp = self.head
        while temp :
            if temp.data == prev_data:
                break
            temp = temp.next
            if temp is None:
                print(f"Node with data {prev_data} Not found")
                return
            new_node= Node(new_data)
            new_node.next = temp.next
            temp.next = new_node
        
    def delete_node(self, key):
        temp = self.head

         # Case 1: Head node itself is to be deleted
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return       

        # Case 2: Search for the key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next        

        # If key not found
        if temp is None:
            return

        # Unlink the node
        prev.next = temp.next
        temp = None
        
        

dll = DoublyLinkedList()
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
dll.printlist()
dll.prepend(10)
dll.printlist()
dll.insertafterposition(20,25)
dll.printlist()
dll.delete_node(20)
print("after deletion : ")
dll.printlist()            
dll.insert_at_end(50)
dll.printlist()            
dll.insert_after(30)
dll.printlist()            
dll.display_forward(20)
dll.printlist()            
