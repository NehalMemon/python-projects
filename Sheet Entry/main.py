import json
import requests

class Student:
    def __init__(self):
        self.student_name=None
        self.father_name=None
        self.cla_ss=None
        self.register_no=None
        self.batch=None
        self.fees=None
    
lst=[]

while True:
    student=Student()
    student.student_name=input("Enter student name...")
    student.father_name=input("Enter father name...")
    student.cla_ss=(input("Enter class..."))
    student.register_no=int(input("Enter registeration number..."))
    student.batch=input("Enter batch type...")
    student.fees = input("Enter monthly fees: ")
    
    
    data={
         'studentsDatum': {
        'Student Name':student.student_name,
        'Father Name':student.father_name,
        'Registration no':student.register_no,
        'Class':student.cla_ss,
        'Batch Type': student.batch,
        'Monthly Fees':student.fees
    }}
            
    lst.append(data) 
    add_another=input("Do you want to add another student (answer in \'yes\' or \'no\')\n")
    if add_another=="no":
        break

def add_data(lst):
    # Use the correct URL based on the project and sheet in Sheety
    url = "https://api.sheety.co/50067000f71c86b690d38fecf8d34c17/studentsData/studentsData"
    headers = {'Content-Type': 'application/json'}

    for data in lst:
        json_data = json.dumps(data)
        response = requests.post(url, data=json_data, headers=headers)
        
        print("Add data response status code:", response.status_code)
        
        if response.status_code == 201:
            print("Data added successfully")
        else:
            print(f"Failed to add data. Status code: {response.status_code}, Response: {response.text}")


if __name__=="__main__":
    add_data(lst)        
        