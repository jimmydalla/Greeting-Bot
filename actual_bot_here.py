from datetime import datetime
from pytz import timezone
from colorama import Fore,Back,Style 

Name = input(Fore.BLUE+"Mind telling me your name ?")
print(Name)

current_time = datetime.now(timezone("Asia/Kolkata"))
current_hr = current_time.hour
print(current_time)
print("\n\n\n\n")

if (current_hr < 12):
  print("Good Morning")
elif current_hr < 18:
  print("Good Afternoon")
else:
  print("Good night")