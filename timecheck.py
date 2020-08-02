from datetime import datetime 
from emailalert import sendmail

new_day = True
now = datetime.now()
current_date = now.strftime("%d/%m/%Y")
current_day = current_date[0:2]
past_day = current_day
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_hour = current_time[0:2]
    current_date = now.strftime("%d/%m/%Y")
    past_day = current_date[0:2]

    if current_day != past_day:
        new_day = True
    
    if current_hour == 21 and new_day:
        sendmail()
        new_day == False
    print(current_date, current_time)
