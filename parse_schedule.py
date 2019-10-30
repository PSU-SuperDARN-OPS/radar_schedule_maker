
with open('sample.txt', 'r') as file:
    date = file.readline()

    rest_of_file = file.read()

operations = rest_of_file.split('#')[0]
common_time = rest_of_file.split('#')[1]
discretionary_time = rest_of_file.split('#')[2]
special_time = rest_of_file.split('#')[3]
if len(rest_of_file.split('#')) > 4:
    notes = rest_of_file.split('#')[4]
else:
    notes = "No notes"

print("Schedule date: " + date)
print("Scheduled operations")
print(operations)
print("Notes:")
print(notes)
