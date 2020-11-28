import json

class healthworker:
    def __init__(self, name, job_title, id):
        self.name = name
        self.job_title = job_title
        self.id = id

class hospital:
    worker_dict = {}
    current_largest_id = 10000

    def update_worker_DB(self):
        with open('healthcare/worker_db.json', 'w') as f:
            json.dump(self.worker_dict, f, indent=4)

    def read_worker_DB(self):
        with open('healthcare/worker_db.json') as f:
            self.worker_dict = json.load(f)
        self.current_largest_id = int(max(self.worker_dict.keys()))

    def generate_unique_worker_id(self):
        self.current_largest_id += 1
        return self.current_largest_id
    
    def add_healthworker(self):
        name = input("Health worker name: ")
        job_title = input("Health worker job title:")
        id = self.generate_unique_worker_id()
        self.worker_dict[id] = { "name" : name, "job_title" : job_title }
        self.update_worker_DB()
        
    def remove_healthworker(self):
        id = input("Enter Health worker ID: ")
        self.worker_dict.pop(id)
        self.update_worker_DB()

    def print_worker_dict(self):
        print(self.worker_dict)
    
hosp = hospital()
hosp.read_worker_DB()

while(True):
    
    try:
        user_input = int(input("""What would you like to do?
1 for adding a worker;
2 for removing a worker
3 for printing worker records
8 for read_worker_DB
9 for update_worker_DB
0 for exiting
"""))
    except ValueError:
        print("This is not a whole number.")
        continue
 
    if user_input == 0:
        break
    elif user_input == 1:
        hosp.add_healthworker()
    elif user_input == 2:
        hosp.remove_healthworker()
    elif user_input == 3:
        hosp.print_worker_dict()       
    elif user_input == 8:
        hosp.read_worker_DB()       
    elif user_input == 9:
        hosp.update_worker_DB()
    else:
        print("Enter a valid value.")   




