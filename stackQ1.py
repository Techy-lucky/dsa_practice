class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, data):
        self.items.append(data)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        print("Stack is empty")
        return None
        
    def is_empty(self):
        return len(self.items) == 0
        
    def display(self):
        print("Stack:", self.items)

def reverse_string(text):
    s = Stack()
    for char in text:
        s.push(char)
    
    reversed_text = ""
    while not s.is_empty():
        reversed_text += s.pop()
        
    return reversed_text

def reverse_stack(original_stack):
    temp_stack = Stack()
    # Pop all elements from original and push to temp (reverses the order)
    while not original_stack.is_empty():
        temp_stack.push(original_stack.pop())
    return temp_stack

# --- Testing Q1 ---
if __name__ == "__main__":
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    
    print("After Pushing:")
    st.display()
    
    print("Popped item:", st.pop())
    st.display()

    word = "LAKSHIT VARMA"
    print(f"Original String: {word} | Reversed: {reverse_string(word)}")

    st2 = Stack()
    st2.push(1)
    st2.push(2)
    st2.push(3)
    print("\nOriginal Stack 2:")
    st2.display()
    
    reversed_st2 = reverse_stack(st2)
    print("Reversed Stack 2:")
    reversed_st2.display()