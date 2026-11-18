class Node:
    def __init__(self, process_id, process_name, priority):
        self.process_id = process_id
        self.process_name = process_name
        self.priority = priority
        self.next = None

class CPUScheduler:
    def __init__(self):
        self.front = None

    def add_process(self, process_id, process_name, priority):
        new_node = Node(process_id, process_name, priority)
        
        if self.front == None or self.front.priority > priority:
            new_node.next = self.front
            self.front = new_node
            print(f"Added: {process_name}")
            return
            
        temp = self.front
        