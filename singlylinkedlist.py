class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

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

ll = linkedlist()
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.printlist()
ll.prepend(10)
ll.printlist()
ll.insertafterposition(20,25)
ll.printlist()
ll.delete_node(20)
print("after deletion : ")
ll.printlist()
