import requests
import smtplib

def get_data():
    url = "https://api.sheety.co/e39415c83b3a3480fbbe68d63331cf7f/memonCoachingClassXiAnnualResults/results"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        results_list = data.get("results", [])
        return results_list
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []

def message_decider():
    if item["percentage"] >= 0.90:
        message = f"Dear {item['father\'sEmail']}\n\n{msg1}.{msg2}.\n{msg5}."
    elif item["percentage"] >= 0.80:
        message = f"Dear {item['father\'sEmail']}\n\n{msg1}.{msg3}.\n{msg5}."
    elif item["percentage"] >= 0.75:
        message = f"Dear {item['father\'sEmail']}\n\n{msg1}.{msg4}.\n{msg5}."
    else:
        message = f"Dear {item['father\'sEmail']}\n\n{msg1}.\n{msg5}."
    return message

def email_sender():
    from_address = "nehalmemon73@gmail.com"
    f_email = item["father'sEmail"]
    password = "prtp qiou xibo abup"
    subject = f"{item['name']}'s annual result"
    message = message_decider()
    full_message = f"Subject: {subject}\n\n{message}"
    
    print(f"Sending email to {f_email}")
   
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_address, password)
            server.sendmail(from_address, f_email, full_message)
            print(f"Email sent successfully to {f_email}")
    except Exception as e:
        print(f"Failed to send email to {f_email}: {e}")

if __name__ == "__main__":
    data = get_data()

    for item in data:
        if "father'sEmail" not in item:
            print("Father,s Email not found")
            continue

        with open('mail1.txt', 'r') as email1:
            template = email1.read()

        content1 = template.replace("x", item["name"])
        content1 = content1.replace("00", str(item["marks"]))  
        msg1 = content1.replace("Y", item["grade"])

        with open('mail2.txt', 'r') as email2:
            content2 = email2.read()
        msg2 = content2.replace("name", item["name"])

        with open('mail3.txt', 'r') as email3:
            content3 = email3.read()
        msg3 = content3.replace("name", item["name"])

        with open('mail4.txt', 'r') as email4:
            content4 = email4.read()
        msg4 = content4.replace("name", item["name"])
        
        with open('mail5.txt', 'r') as email5:
            content5 = email5.read()
        msg5=content5    

        email_sender()

    
    
        
    
    
