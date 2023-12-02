year = int(input("What year is it?: "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      days = 366
    else:
      days = 365
  else:
    days = 366
else:
  days = 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"In the year {year}, there are {days:,} days, or {hours:,} hours, or {minutes:,} minutes, or {seconds:,} seconds.")