#!/usr/bin/python3

import datetime

def get_last_wednesday(year, month):
    # Find the last day of the month
    if month == 12:
        last_day = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    
    # Calculate the difference between the last day and the desired Wednesday (2 represents Wednesday)
    diff = (last_day.weekday() - 2) % 7
    
    # Subtract the difference from the last day to get the last Wednesday
    last_wednesday = last_day - datetime.timedelta(days=diff)
    
    return last_wednesday

today = datetime.date.today()
latest_wednesdays = []

for _ in range(24):
    latest_wednesdays.append(get_last_wednesday(today.year, today.month).strftime('%Y-%m-%d'))
    # Move to the previous month
    if today.month == 1:
        today = today.replace(year=today.year - 1, month=12)
    else:
        today = today.replace(month=today.month - 1)

with open("chat-dates.txt", "w+") as fp:
    for latest_wednesday in latest_wednesdays:
        fp.write(latest_wednesday + "\n")