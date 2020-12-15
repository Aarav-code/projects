from nodes import Node as nd
import json
import os

class Priorityqueue:
    def __init__(self, number_of_priorities = 10, total_messages = 40, value = None):
        self.number_of_priorities = number_of_priorities
        self.total_messages = total_messages
        self.head_node = nd(value)
        self.value = 0
        self.messages_dict = {}
        self.string = ""

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value):
        new_node = nd(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        self.value += 1
        print(self.value)
    
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        i = 0
        while current_node:
            if current_node.get_value() != None:
                string_list = str(current_node.get_value()) #+ "\n"
                self.messages_dict[i] = string_list
                if i in self.messages_dict:
                    i +=1
            current_node = current_node.get_next_node()
        return self.messages_dict
    
    def insert_end(self, new_value):
        new_node = nd(new_value)
        if self.head_node is None:
            self.head_node = new_node
        
        last = self.head_node
        while(last.next_node != None):
            last = last.get_next_node

        last.next_node = new_node
        self.value += 1
        print(self.value)

    def has_space(self):
        return self.value < self.number_of_priorities + self.total_messages
    
    def is_empty(self):
        return self.value == 0
    
    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        self.head_node.next_node = self.head_node.next_node.next_node
        self.value -= 1
        string = str(self.head_node.next_node)
        return string + " was sent"
    
    def read_messages_db(self):
        if os.stat("messages.json").st_size == 0:
            return
        with open('messages.json') as f:
            self.worker_dict = json.load(f)
        self.current_largest_id = self.worker_dict["largest_id"]

    def update_messages_DB(self):
        with open('messages.json', 'w') as f:
            json.dump(self.messages_dict, f, indent=4)
