#!/usr/bin/python3

from entry import Entry


class Schedule:
    def __init__(self, year=0, month=0):
        self.year = year
        self.month = month
        self.entries = []

    def add_entry(self, start_day, start_hour, stop_day, stop_hour, mode):
        self.entries.append(Entry(self.year, self.month, start_day, start_hour, stop_day, stop_hour, mode))

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def get_entries(self):
        entries = []
        for entry in self.entries:
            entries.append(entry.get_entry())

        return entries

    def get_duration(self):
        duration = 0

        for entry in self.entries:
            duration += entry.get_duration()
        return duration

    def print_schedule(self):
        for entry in self.entries:
            print(entry.get_entry_string())

