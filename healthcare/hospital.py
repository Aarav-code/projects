import json
import os

class hospital:
    current_largest_id = 10000

    def __init__(self):
        self.worker_dict = {
            "doctor" :{"cardiologist" : {"busy" : {}, "free" : {}},
            "audiologist" : {"busy" : {}, "free" : {}},
            "paediatrician" : {"busy" : {}, "free" : {}}, 
            "veterinarian" : {"busy" : {}, "free" : {}},
            "radiologist" : {"busy" : {}, "free" : {}}},
            "nurse" : {"busy" : {}, "free" : {}},
            "other-health-worker-type" : {"busy" : {}, "free" : {}},
            "largest_id" : "\"\"" 
            }

    def generate_unique_worker_id(self):
        self.current_largest_id += 1
        self.worker_dict["largest_id"] = self.current_largest_id
        return self.current_largest_id

    def update_worker_DB(self):
        with open('healthcare/worker_db.json', 'w') as f:
            json.dump(self.worker_dict, f, indent=4)

    def read_worker_DB(self):
        if os.stat("healthcare/worker_db.json").st_size == 0:
            return
        with open('healthcare/worker_db.json') as f:
            self.worker_dict = json.load(f)
        self.current_largest_id = self.worker_dict["largest_id"]
            
         
    def add_healthworker(self):
        name = input("Health worker name: ")
        job_title = input("Health worker job title: ")
        worker_type = input("Enter worker type: ").lower().strip()
        id = self.generate_unique_worker_id()
        if job_title in self.worker_dict["doctor"]:
            if worker_type == "doctor":
                self.worker_dict["doctor"][job_title]["free"][id] = { "name" : name}
        elif worker_type == "nurse": 
            self.worker_dict["nurse"]["free"][id] = { "name" : name, "job_title" : job_title} 
        else:
            self.worker_dict["other-health-worker-type"]["free"][id] = { "name" : name, "job_title" : job_title} 
        self.update_worker_DB()

    def remove_healthworker(self):
        id = input("Enter Health worker ID: ")
        self.worker_dict.pop(id)
        self.update_worker_DB()

    def print_worker_dict(self):
        print(self.worker_dict)

    def book_doctor(self):
        doctor_type = input("Enter doctor type ").strip().lower()
        if doctor_type in self.worker_dict["doctor"]:
            a = self.worker_dict["doctor"][doctor_type]["free"]
            self.worker_dict["doctor"][doctor_type]["busy"] = a
            for i in (self.worker_dict["doctor"][doctor_type]["free"]):
                del self.worker_dict["doctor"][doctor_type]["free"][i]
                break
        self.update_worker_DB()
                 

        
    def set_doctor_free(self):
        doctor_id = int(input("Enter a doctors id: "))
        print(self.worker_dict)
        # radiologist
    

            
            

