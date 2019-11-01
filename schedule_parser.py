#!/usr/bin/python3
# Minimum requirements are Python 3.6
from datetime import datetime
from schedule import Schedule


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
        self.schedule = Schedule()

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

        self.set_date(date_str)

    def set_date(self, date_str):
        date = datetime.strptime(date_str, "%B %Y")
        self.month = date.month
        self.year = date.year
        self.schedule.set_month(self.month)
        self.schedule.set_year(self.year)

    def __get_notes(self):
        note_sections = self.note_str.split('Note ')[1:]

        i = 0
        for note in note_sections:
            correct_mode = input(f"If '{note.split()[1]}' is the correct mode for Note {chr(ord('A') + i)}, "
                                 f"enter 'y'. Else enter the correct mode: ")
            if correct_mode == 'y':
                self.notes.update({f"Note {chr(ord('A') + i)})": note.split()[1]})
            else:
                self.notes.update({f"Note {chr(ord('A') + i)})": correct_mode})
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
            start_time = operation[0]
            stop_time = operation[1]
            mode_and_note = operation[2]

            start_day = int(start_time.split(':')[0])
            start_hour = int(start_time.split(':')[1])
            stop_day = int(stop_time.split(':')[0])
            stop_hour = int(stop_time.split(':')[1])

            mode = mode_and_note.split()[0]
            if mode == 'Special':
                mode += ":" + self.notes[mode_and_note.split("(see ")[1]]

            self.schedule.add_entry(start_day, start_hour, stop_day, stop_hour, mode)

        self.total_duration = self.schedule.get_duration()

    def get_schedule(self):
        return self.schedule

    def print_schedule(self):
        self.schedule.print_schedule()

    def run(self):
        self.read_schedule()
        self.format_schedule()


if __name__ == '__main__':
    parser = ScheduleParser('sample_notes.txt')
    parser.run()
    parser.print_schedule()

