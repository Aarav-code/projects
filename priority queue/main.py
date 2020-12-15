from priorityqueue import Priorityqueue as pq
import time
i = 0
messages = pq()

def main():
    number = int(input("Enter the number of messages(press enter for defualt value)"))
    priorities = number * (20/ 100)
    number_without_priorities = number - priorities
    for i in range(number):
        if messages.has_space:
            if not messages.has_space():
                print("No more space")
                return messages.stringify_list()
            input_value = input("Enter your message\n")
            yes_or_no = input("Is your message important?(yes/no)\n").strip().lower()
            if yes_or_no == "yes": 
                messages.insert_beginning(input_value)
            elif yes_or_no == "no": 
                messages.insert_end(input_value)
            else: print("Enter a valid response")
    print(messages.stringify_list())
    messages.update_messages_DB()
    for i in range(messages.value):    
        a = messages.pop()
        time.sleep(5)
        print(a)
    messages.update_messages_DB


main()