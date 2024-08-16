from datetime import datetime

def find_day_of_week(date_str:str) -> str:
    date_formate="%Y-%m-%d"
    date = datetime.strptime(date_str, date_formate)
    day = date.strftime("%A, %B %d")
    return day

date_str = "2024-08-16"
print(find_day_of_week(date_str))