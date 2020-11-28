import json

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
        self.worker_dict[id] = { "name" : name, "job_title" : job_title , "busy" : False}
        self.update_worker_DB()
        
    def remove_healthworker(self):
        id = input("Enter Health worker ID: ")
        self.worker_dict.pop(id)
        self.update_worker_DB()

    def print_worker_dict(self):
        print(self.worker_dict)

    def get_doctor(self):
        bFound = False
        doctor_type = input("Enter doctor type ").strip()
        for i in self.worker_dict:
            a = self.worker_dict[i]["job_title"]
            if a == doctor_type:
                print("Doctor name:" + self.worker_dict[i]["name"] + " doctor busy: " 
                + str(self.worker_dict[i]["busy"]))
                bFound = True   
                break
        if bFound == False:
            print("Enter a valid doctor type")
        
    def set_busy_status(self):
        doctor_id = input("Enter a doctors id: ")
        busy_status = input("Enter doctor status (busy or free) : ").lower().strip()   
        if busy_status == "busy":
            self.worker_dict[doctor_id]["busy"] = True
        elif busy_status == "free":
            self.worker_dict[doctor_id]["busy"] = False
        else:
            print("Enter valid status")
        self.update_worker_DB()
    

            
            

