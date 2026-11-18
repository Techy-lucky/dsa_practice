# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class stack:
#     def __init__(self):
#         self.top = None

#     def push(self,data):
#         new_node = Node(data)
#         new_node.next = self.top
#         self.top = new_node
#         print(f"pushed {data} onto stack")

#     def pop(self):
#         if self.is_empty():
#             print("stack underflow! No element to pop.")
#             return
#         popped = self.top.data
#         self.top = self.top.next
#         print(f"popped {popped} from stack")
#         return popped

#     def display(self):
#         if self.is_empty():
#             print("stack is empty.")
#             return
#         temp = self.top
#         print("stack elements (top to bottom ) : ",end ="")
#         while temp:
#             print(temp.data,end ="_>")
#             temp = temp.next
#         print("None")

# st =stack()
# st.push(10)
# st.push(20)
# st.push(30)
# st.push(40)
# st.push(50)

# st.display()

# print("Top element is :",st.peek())

# st.pop()
# st.display()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    # Added missing is_empty method
    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"pushed {data} onto stack")

    def pop(self):
        if self.is_empty():
            print("stack underflow! No element to pop.")
            return
        popped = self.top.data
        self.top = self.top.next
        print(f"popped {popped} from stack")
        return popped

    # Added missing peek method
    def peek(self):
        if self.is_empty():
            print("stack is empty.")
            return None
        return self.top.data

    def display(self):
        if self.is_empty():
            print("stack is empty.")
            return
        temp = self.top
        print("stack elements (top to bottom ) : ", end="")
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

st = stack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)

st.display()

print("Top element is :", st.peek())

st.pop()
st.display()