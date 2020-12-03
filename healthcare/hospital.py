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
        doctor_prof = None
        doctor_status = None
        id = input("Enter Health worker ID: ")
        doctor_dict = self.worker_dict["doctor"]
        for prof in doctor_dict:
            if id in self.worker_dict["doctor"][prof]["free"]:
                doctor_prof = prof
                doctor_status = "free"
                break
            elif id in self.worker_dict["doctor"][prof]["free"]:
                doctor_prof = prof
                doctor_status = "busy"
                break
        del self.worker_dict["doctor"][doctor_prof][doctor_status][id]
        self.update_worker_DB()

    def print_worker_dict(self):
        print(self.worker_dict)

    def book_doctor(self):
        doctor_type = input("Enter doctor type: ").strip().lower()
        doctor_dict = self.worker_dict["doctor"]
        if doctor_type not in doctor_dict:
            print("{} not found".format(doctor_type))
            return
        
        free_list = doctor_dict[doctor_type]["free"]
        if len(free_list) == 0:
            print("No free doctors found")
            return
        
        for id in free_list:
            doctor_id = id
            break

        free_doc = free_list[doctor_id]
        del free_list[doctor_id]

        busy_list = doctor_dict[doctor_type]["busy"]
        busy_list[doctor_id] = free_doc
        self.update_worker_DB()
        return doctor_id


    def set_doctor_free(self):
        doctor_found = False
        id = input("enter the doctors id: ")
        doctor_dict = self.worker_dict["doctor"]
        for prof in doctor_dict:
            if id in doctor_dict[prof]["busy"]:
               doctor_found = True
               doctor_prof = prof
               break
        if not doctor_found :
            print("Doctor not found")
            return

        doctor_dict[doctor_prof]["free"][id] = doctor_dict[doctor_prof]["busy"][id]
        del doctor_dict[doctor_prof]["busy"][id]
        self.update_worker_DB()

            
    

            
            

