#!/usr/bin/python3
# Minimum requirements are Python 3.6
from datetime import datetime


class ScheduleParser:
    """A class that parses the SuperDARN scheduling files and returns a generic schedule for the radars"""
    def __init__(self, filename):
        self.filename = filename
        self.year = 2000
        self.month = 1
        self.operations = []
        self.note_str = ''
        self.notes = {}
        self.notes_exist = False
        self.total_duration = 0
        self.schedule = []

    def read_schedule(self):
        with open(self.filename, 'r') as file:
            date_str = file.readline().rstrip()
            rest_of_file = file.read()

        operations = rest_of_file.split('#')[0].rstrip()
        self.operations = operations.split('\n')

        # Currently don't care about the following lines, discarding to get to the notes section
        common_time = rest_of_file.split('#')[1]
        discretionary_time = rest_of_file.split('#')[2]
        special_time = rest_of_file.split('#')[3]

        if len(rest_of_file.split('#')) > 4:
            self.note_str = rest_of_file.split('#')[4]
            self.notes_exist = True
        else:
            self.notes_exist = False

        date = datetime.strptime(date_str, "%B %Y")
        self.month = date.month
        self.year = date.year

    def __get_notes(self):
        note_sections = self.note_str.split('Note ')[1:]

        i = 0
        for note in note_sections:
            self.notes.update({f"Note {chr(ord('A') + i)})": note.split()[1]})
            i += 1

    def format_schedule(self):
        entry = {
            'Start Day': 0,
            'Start Hour': 0,
            'Stop Day': 0,
            'Stop Hour': 0,
            'Duration': 0,
            'Time String': '',
            'Mode': 'Common Time'
        }

        if self.notes_exist:
            self.__get_notes()

        for op in range(len(self.operations)):
            operation = self.operations[op].split("    ")

            entry['Start Day'] = int(operation[0].split(':')[0])
            entry['Start Hour'] = int(operation[0].split(':')[1])
            entry['Stop Day'] = int(operation[1].split(':')[0])
            entry['Stop Hour'] = int(operation[1].split(':')[1])

            entry['Duration'] = (entry['Stop Day'] - entry['Start Day']) * (24 * 60) \
                                + (entry['Stop Hour'] - entry['Start Hour']) * 60
            self.total_duration += entry['Duration']

            entry['Time String'] = f"{self.year} {self.month:02} " \
                f"{entry['Start Day']:02} {entry['Start Hour']:02} 00 {entry['Duration']:6}"

            entry['Mode'] = operation[2].split()[0]
            if entry['Mode'] == 'Special':
                entry['Mode'] += ":" + self.notes[operation[2].split("(see ")[1]]

            self.schedule.append(entry.copy())

    def get_schedule(self):
        return self.schedule

    def print_schedule(self):
        for line in self.schedule:
            print(f"{line['Time String']} {line['Mode']}")
        print(f"Monthly total: {self.total_duration}, "
              f"Should be {self.schedule[len(self.schedule)-1]['Stop Day']*24*60}")

    def run(self):
        self.read_schedule()
        self.format_schedule()


if __name__ == '__main__':
    parser = ScheduleParser('sample_notes.txt')
    parser.run()
    parser.print_schedule()

