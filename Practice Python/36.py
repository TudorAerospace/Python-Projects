from bokeh.plotting import figure, show, output_file
from collections import Counter
import json
file_path = r'C:\Users\Tudor\Desktop\Python\Practice Python\birthdays.json'

month_dict = { '01': 'January', '02': 'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}

birthdays = []
final = []

with open(file_path, 'r') as file:
        data = json.load(file)
        for item in data:
           birthdays.append(item['date'])
        months = [date.split('/')[1] for date in birthdays]

lght = len(months)
for j in range(lght):
    month_lookup = months[j]
    final.append(month_dict[month_lookup])

c = Counter(final)

for month, count in c.items():
    print(f"{month}: {count}")


output_file("plot.html")
y=[]
x =[]
x_categories = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for month, count in c.items():
    x.append(month)
    print(y)
for month, count in c.items():
    y.append(count)
    print(y)

p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)

show(p)