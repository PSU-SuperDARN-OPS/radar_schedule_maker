#!/usr/bin/python3
# Minimum requirements are Python 3.6
from datetime import datetime
from schedule import Schedule


class ScheduleParser:
    """
    A class that parses the SuperDARN scheduling files and returns a generic schedule for the radars.


    """
    def __init__(self, filename):
        self.filename = filename

        self.raw_date = ""
        self.raw_operations = []
        self.raw_notes = []

        self.year = 2000
        self.month = 1
        # self.operations = []
        # self.note_str = ""
        self.notes = {}
        self.notes_exist = False
        self.total_duration = 0
        self.schedule = Schedule()

    def read_schedule(self):
        with open(self.filename, 'r') as file:
            self.raw_date = file.readline().rstrip()

            for line in file:
                if line[0] == '#':
                    pass  # Ignore comment
                elif line[0] == '0' or line[0] == '1' or line[0] == '2' or line[0] == '3':
                    self.raw_operations.append(line.rstrip())
                elif "Note" in line:
                    self.raw_notes.append(line.rstrip())
                    self.notes_exist = True
                else:
                    # Ignore line
                    pass

    def set_date(self):
        date = datetime.strptime(self.raw_date, "%B %Y")
        self.month = date.month
        self.year = date.year
        self.schedule.set_month(self.month)
        self.schedule.set_year(self.year)

    def get_notes(self):
        i = 0
        for note in self.raw_notes:
            correct_mode = input(f"If '{note.split()[2]}' is the correct mode for Note {chr(ord('A') + i)}, "
                                 f"enter 'y'. Else enter the correct mode: ")

            if correct_mode == 'y':
                self.notes.update({f"Note {chr(ord('A') + i)}": note.split()[2]})
            else:
                self.notes.update({f"Note {chr(ord('A') + i)}": correct_mode})
            i += 1

    def get_operation(self):
        for op in range(len(self.raw_operations)):
            operation = self.raw_operations[op].split("    ")
            start_time = operation[0]
            stop_time = operation[1]
            mode_and_note = operation[2]

            start_day = int(start_time.split(':')[0])
            start_hour = int(start_time.split(':')[1])
            stop_day = int(stop_time.split(':')[0])
            stop_hour = int(stop_time.split(':')[1])

            mode = mode_and_note.split()[0]
            if mode == 'Special':
                mode += ":" + self.notes[mode_and_note.split("(see ")[1][:-1]]

            self.schedule.add_entry(start_day, start_hour, stop_day, stop_hour, mode)

    def format_schedule(self):
        self.set_date()

        if self.notes_exist:
            self.get_notes()

        self.get_operation()

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

