import time

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node
    
class Queue:
    def __init__(self, a):
        self.head = None
        self.tail = None
        self.max_size = 3
        self.total_prioirity_messages = a
        self.current_prioirity_messages = 0
        self.current_size = 0
    
    def prioirity_has_space(self):
        return self.total_prioirity_messages > self.current_prioirity_messages

    def has_space(self):
        return self.max_size > self.current_size

    def add(self, value):
        if self.has_space():
            if self.tail is None:
                self.head = Node(value)
                self.tail = self.head
                self.current_size += 1
            else:
                self.tail.next_node = Node(value)
                self.tail = self.tail.next_node
                self.current_size += 1

    def remove(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.value
            self.head = self.head.next_node
            return to_return + " was sent."
            self.current_size -= 1

prioirity = []
not_prioirity = []

number = int(input("Enter number of prioirity messages: "))
a = Queue(number)

def message_input():
    while a.has_space():
        message = input("Enter your message: ")
        yes_or_no = input("Is the message important(y/n): ").lower().strip()
        if yes_or_no == "y":
            if a.prioirity_has_space():
                prioirity.append(message)
                a.current_prioirity_messages += 1
                a.current_size += 1
            else:
                print("No more space in priority message")
        elif yes_or_no == "n":
            not_prioirity.append(message)
            a.current_size += 1
        else:
            message_input()
    a.current_size = 0

message_input()      
final_list = prioirity + not_prioirity

for message in final_list:
    a.add(message)

for i in range(a.current_size):
    time.sleep(3)
    print(a.remove())