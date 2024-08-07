import json
import requests
import smtplib
from datetime import datetime, timedelta
from functools import reduce

def get_data():
    url = "https://api.sheety.co/5219cc60317c4cff6cc2ae9d5607c724/budget/budget"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results_list = data.get("budget", [])
        return results_list
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []

data = get_data()

def income():
    income_list = []
    for item in data:
        if item.get("type") == "income":
            income_list.append(item["rupees"])
    return income_list

income_ = income()
total_income = reduce(lambda x, y: x + y, income_a) if income_ else 0

def expense():
    expense_list = []
    for item in data:
        if item.get("type") == "expense":
            expense_list.append(item["rupees"])
    return expense_list

expense_ = expense()
total_expense = reduce(lambda x, y: x + y, expense_) if expense_ else 0


def saving_over_expense():
    total_savings = 0
    over_expense = 0
    if total_income > total_expense:
        total_savings = total_income - total_expense
    else:
        over_expense = total_expense - total_income
    return total_savings, over_expense

savings, over_expense = saving_over_expense()
  
    
    
    
def msg_decider(msg1, msg2, msg3):
    if savings > 0:
        msg = f"{msg1}.\n{msg3}"
    else:
        msg = f"{msg1}.\n{msg2}"
    return msg

def email_sender():
    from_address = "nehalmemon73@gmail.com"
    to_email = "nehalmemon73@gmail.com"
    password = "passwordaaaaa aa"  
    subject = f"Monthly budget of {l_month}"
    
    with open('msg.txt', 'r') as file:
        msg1 = file.read().replace("jan", l_month).replace("00", str(total_income)).replace("11", str(total_expense))

    with open('msg2.txt', 'r') as file:
        msg2 = file.read().replace("00", str(total_expense))

    with open('msg3.txt', 'r') as file:
        msg3 = file.read().replace("00", str(savings))
    
    message = msg_decider(msg1, msg2, msg3)
    full_message = f"Subject: {subject}\n\nDear User\n{message}"
    
    print(f"Sending email to {to_email}")
    
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_address, password)
            server.sendmail(from_address, to_email, full_message)
            print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
        

today=datetime.now()
f_d_c_m=today.replace(day=1)
l_d_l_m=f_d_c_m-timedelta(days=1)
l_month=l_d_l_m.strftime("%B")
year=l_d_l_m.year
        
def add_data():
    
    data={ "budgetTracker2":{
        "MONTH":l_month,
        "YEAR":year ,
        "TOTAL INCOME":total_income,
        "TOTAL EXPENSE":total_expense,
        "SAVINGS":savings if savings > 0 else 0,
        "OVER EXPENSE": over_expense if over_expense >0 else 0      
    }}
    url="https://api.sheety.co/5219cc60317c4cff6cc2ae9d5607c724/budgetTracker2/budgetTracker2"
    data_json = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=data_json, headers=headers)
    print("Add data response status code:", response.status_code)
    
    if response.status_code == 200:
        print("Data added successfully")
    else:
        print(f"Failed to add data. Status code: {response.status_code}, Response: {response.text}")
        
        
def delete_data():
    url = "https://api.sheety.co/5219cc60317c4cff6cc2ae9d5607c724/budget/budget"
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json().get("budget", []) 
            if not data:
                print("All data deleted successfully.")
                break
            for item in data:
                item_id = item["id"]
                delete_url = f"https://api.sheety.co/5219cc60317c4cff6cc2ae9d5607c724/budget/budget/{item_id}"
                delete= requests.delete(delete_url)
                if delete.status_code == 204:
                    print(f"Entry with ID {item_id} deleted successfully")
                else:
                    print(f"Failed to delete data with ID {item_id}. Status code: {delete.status_code}")
        else:
            print(f"Failed to retrieve data for deletion. Status code: {response.status_code}")
            break
if __name__=="__main__":
      if today.strftime("%d")== "07" :
         email_sender()
         add_data() 
         delete_data()         
            
    


            
        
