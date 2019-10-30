#!/usr/bin/python3
# Minimum requirements are Python 3.6
from datetime import datetime

with open('sample.txt', 'r') as file:
    date_str = file.readline().rstrip()
    rest_of_file = file.read()

operations = rest_of_file.split('#')[0].rstrip()
common_time = rest_of_file.split('#')[1]
discretionary_time = rest_of_file.split('#')[2]
special_time = rest_of_file.split('#')[3]
if len(rest_of_file.split('#')) > 4:
    notes = rest_of_file.split('#')[4]
else:
    notes = "No notes"

date = datetime.strptime(date_str, "%B %Y")
month = date.month
year = date.year

print(f"Schedule date: {year} {month}")
print("Scheduled operations")
print(operations)
print("Notes:")
print(notes)

operations = operations.split('\n')

entry = {
    'Start Day' : 0,
    'Start Hour': 0,
    'Stop Day'  : 0,
    'Stop Hour' : 0,
    'Duration'  : 0,
    'Mode'  : 'Common Time'
}

schedule = []
for op in range(len(operations)):
    operation = operations[op].split("    ")

    entry['Start Day'] = int(operation[0].split(':')[0])
    entry['Start Hour'] = int(operation[0].split(':')[1])
    entry['Stop Day'] = int(operation[1].split(':')[0])
    entry['Stop Hour'] = int(operation[1].split(':')[1])

    entry['Duration'] = (entry['Stop Day'] - entry['Start Day']) * (24 * 60) \
                        + (entry['Stop Hour'] - entry['Start Hour']) * 60

    entry['Mode'] = operation[2]

    schedule.append(entry.copy())

for line in schedule:
    print(f"{year} {month:02} {line['Start Day']:02} {line['Start Hour']:02} 00 {line['Duration']:6} {line['Mode']}")
