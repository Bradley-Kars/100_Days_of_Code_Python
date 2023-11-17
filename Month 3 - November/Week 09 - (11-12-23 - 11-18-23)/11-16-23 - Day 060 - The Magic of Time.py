from datetime import datetime

print("Event Countdown")

todays_date = datetime.today().date()

event_date = input("When is the event, please eneter this in mm-dd-yyyy format: ")
event_date = datetime.strptime(event_date, "%m-%d-%Y").date()

time_difference = event_date - todays_date

if int(time_difference.days) > 0:
  print(f"Looks like your event is in {time_difference.days} days.")
elif int(time_difference.days) < 0:
  print(f"Looks like that happaned {abs(time_difference.days)} days ago.")
else:
  print("Thats today!!!")