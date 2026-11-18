class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, data):
        self.items.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        print("Queue is empty")
        return None
        
    def is_empty(self):
        return len(self.items) == 0
        
    def display(self):
        print("Queue:", self.items)

def reverse_queue(q):
    s = [] # Using a simple list as a stack
    
    # Dequeue all elements and push to stack
    while not q.is_empty():
        s.append(q.dequeue())
        
    # Pop all elements from stack and enqueue back to queue
    while len(s) > 0:
        q.enqueue(s.pop())

def merge_queues(q1, q2):
    merged = Queue()
    for item in q1.items:
        merged.enqueue(item)
    for item in q2.items:
        merged.enqueue(item)
    return merged

def are_identical(q1, q2):
    if len(q1.items) != len(q2.items):
        return False
    for i in range(len(q1.items)):
        if q1.items[i] != q2.items[i]:
            return False
    return True

# --- Testing Q2 ---
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    print("After Enqueue:")
    q.display()
    print("Dequeued item:", q.dequeue())
    q.display()

    print("\nBefore reversing:")
    q.display()
    reverse_queue(q)
    print("After reversing using stack:")
    q.display()

    q1 = Queue()
    q1.enqueue(1)
    q1.enqueue(2)

    q2 = Queue()
    q2.enqueue(3)
    q2.enqueue(4)

    print("\nMerging two queues:")
    m_queue = merge_queues(q1, q2)
    m_queue.display()

    print("\nChecking if identical:")
    q3 = Queue()
    q3.enqueue(1)
    q3.enqueue(2)
    
    print("Are q1 and q2 identical?", are_identical(q1, q2))
    print("Are q1 and q3 identical?", are_identical(q1, q3))