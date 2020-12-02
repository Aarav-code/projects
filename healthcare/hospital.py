import json
import os
import copy

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
        for i in self.worker_dict["doctor"]:
            for j in self.worker_dict["doctor"][i]["busy"]:
               if j == id:
                   del self.worker_dict["doctor"][i]["busy"][j]
                   break
            for h in self.worker_dict["doctor"][i]["free"]:
                if h == id:
                    del self.worker_dict["doctor"][i]["free"][h]
                    break
        self.update_worker_DB()

    def print_worker_dict(self):
        print(self.worker_dict)

    def book_doctor(self):
        doctor_type = input("Enter doctor type: ")
        if doctor_type in self.worker_dict["doctor"]:
            for i in self.worker_dict["doctor"][doctor_type]["free"]:
                self.worker_dict["doctor"][doctor_type]["busy"][i] = self.worker_dict["doctor"][doctor_type]["free"][i]
                del self.worker_dict["doctor"][doctor_type]["free"][i]
                break
        else:
            print("Enter a valid doctor type")
        self.update_worker_DB()
                 
    def set_doctor_free(self):
        id = input("enter the doctors id: ")
        for i in self.worker_dict["doctor"]:
            for j in self.worker_dict["doctor"][i]["busy"]:
                if j == id:
                    self.worker_dict["doctor"][i]["free"][j] = self.worker_dict["doctor"][i]["busy"][j]
                    del self.worker_dict["doctor"][i]["busy"][j]
                    break
        self.update_worker_DB()

            
    

            
            

