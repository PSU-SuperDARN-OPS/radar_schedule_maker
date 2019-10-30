#!/usr/bin/python3
# Minimum requirements are Python 3.6
from datetime import datetime

class Schedule_Parser:
    """A class that parses the SuperDARN scheduling files and returns a generic schedule for the radars"""
    def __init__(self, filename):
        self.filename = filename
        self.year = 2000
        self.month = 1
        self.operations = []
        self.notes = ''
        self.total_duration = 0
        self.schedule = []

    def read_schedule(self):
        with open(self.filename, 'r') as file:
            date_str = file.readline().rstrip()
            rest_of_file = file.read()

        operations = rest_of_file.split('#')[0].rstrip()
        self.operations = operations.split('\n')
        common_time = rest_of_file.split('#')[1]
        discretionary_time = rest_of_file.split('#')[2]
        special_time = rest_of_file.split('#')[3]
        if len(rest_of_file.split('#')) > 4:
            self.notes = rest_of_file.split('#')[4]
        else:
            self.notes = "No notes"

        date = datetime.strptime(date_str, "%B %Y")
        self.month = date.month
        self.year = date.year

    def generate_schedule(self):
        entry = {
            'Start Day' : 0,
            'Start Hour': 0,
            'Stop Day'  : 0,
            'Stop Hour' : 0,
            'Duration'  : 0,
            'Mode'  : 'Common Time'
        }

        for op in range(len(self.operations)):
            operation = self.operations[op].split("    ")

            entry['Start Day'] = int(operation[0].split(':')[0])
            entry['Start Hour'] = int(operation[0].split(':')[1])
            entry['Stop Day'] = int(operation[1].split(':')[0])
            entry['Stop Hour'] = int(operation[1].split(':')[1])

            entry['Duration'] = (entry['Stop Day'] - entry['Start Day']) * (24 * 60) \
                                + (entry['Stop Hour'] - entry['Start Hour']) * 60
            self.total_duration += entry['Duration']

            entry['Mode'] = operation[2]

            self.schedule.append(entry.copy())

    def print_schedule(self):
        for line in self.schedule:
            print(f"{self.year} {self.month:02} {line['Start Day']:02} {line['Start Hour']:02} 00 {line['Duration']:6} {line['Mode']}")
        print(f"Monthly total: {self.total_duration}, Should be {self.schedule[len(self.schedule)-1]['Stop Day']*24*60}")


if __name__ == '__main__':
    parser = Schedule_Parser('sample_notes.txt')
    parser.read_schedule()
    parser.generate_schedule()
    parser.print_schedule()
