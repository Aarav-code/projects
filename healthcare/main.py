# git push -u origin master


import json
from hospital import hospital

class healthworker:
    def __init__(self, name, job_title, id):
        self.name = name
        self.job_title = job_title
        self.id = id
   
hosp = hospital()
hosp.read_worker_DB()

while(True):
    
    try:
        user_input = int(input("""========================
What would you like to do?
1 for adding a worker;
2 for removing a worker
3 for printing worker records
4 to book doctor
5 to free the doctor
8 for read_worker_DB         
0 for exiting
========================
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
    elif user_input == 4:
        hosp.book_doctor()
    elif user_input == 5:
        hosp.set_doctor_free()           
    elif user_input == 8:
        hosp.read_worker_DB()       

    else:
        print("Enter a valid value.")   




