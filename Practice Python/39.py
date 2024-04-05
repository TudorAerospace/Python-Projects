import datetime as dt

dt.datetime.now()

now = dt.datetime.now()

print(now.year)

age = int(input("How old are you? "))

print(f"From the current year, {now.year}, you will be 100 in {100-age} years.")