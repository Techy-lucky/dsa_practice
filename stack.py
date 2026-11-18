class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node 

    def pop(self):
        if self.isempty():
            print("stack is empty")
            return None
        else:
            temp = self.top
            self.top = self.top.next
            data = temp.data
            temp = None
            return data

    def print(self):
        temp = self.top
        print("stack elements:")
        while temp:
            print(temp.data)
            temp = temp.next
        print("---")
        
    def reverse(self, aux_stack):
        # Transfer all elements to the auxiliary stack
        while not self.isempty():
            val = self.pop()
            aux_stack.push(Node(val))
            
        # Point the original stack's top to the reversed stack's top
        self.top = aux_stack.top


# Testing the code
st = stack()
st1 = stack() # Auxiliary stack

st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(75))
st.push(Node(90))

print("Original Stack")
st.print()

# Reverse the stack using st1
st.reverse(st1)

print("Reversed Stack")
st.print()