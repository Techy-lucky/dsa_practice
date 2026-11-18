# 1. This is just the basic box for data
class Node:
    def __init__(self, process_id, process_name, priority):
        self.process_id = process_id
        self.process_name = process_name
        self.priority = priority
        self.next = None

# 2. This is the simple Priority Queue
class CPUScheduler:
    def __init__(self):
        self.front = None

    def add_process(self, process_id, process_name, priority):
        new_node = Node(process_id, process_name, priority)
        
        # Case 1: If queue is empty OR new process has higher priority (smaller number)
        if self.front == None or self.front.priority > priority:
            new_node.next = self.front
            self.front = new_node
            print(f"Added: {process_name}")
            return
            
        # Case 2: Traverse to find the correct spot
        temp = self.front
        while temp.next != None and temp.next.priority <= priority:
            temp = temp.next
            
        new_node.next = temp.next
        temp.next = new_node
        print(f"Added: {process_name}")

    def execute_process(self):
        if self.front == None:
            print("No processes to execute.")
            return
            
        # Simply remove the first node
        print(f"Executed: {self.front.process_name}")
        self.front = self.front.next

    def view_next_process(self):
        if self.front == None:
            print("No pending processes.")
            return
            
        print(f"Next Process: {self.front.process_name} (Priority {self.front.priority})")

    def display_processes(self):
        if self.front == None:
            print("No pending processes.")
            return
            
        print("\nPending Processes:")
        temp = self.front
        while temp != None:
            print(f"[{temp.priority}] {temp.process_id} - {temp.process_name}")
            temp = temp.next
        print()

    def count(self):
        total = 0
        temp = self.front
        while temp != None:
            total += 1
            temp = temp.next
        print(f"Total Count: {total}")


# --- Simple Testing ---
scheduler = CPUScheduler()

# Add processes according to assignment priorities
scheduler.add_process("P1", "Background Job", 3)
scheduler.add_process("P2", "System Job", 1) 
scheduler.add_process("P3", "Low Priority Job", 4)
scheduler.add_process("P4", "Interactive Job", 2)

scheduler.count()
scheduler.view_next_process()
scheduler.display_processes()

scheduler.execute_process()
scheduler.execute_process()

scheduler.count()
scheduler.display_processes()