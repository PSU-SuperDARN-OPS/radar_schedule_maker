#!/usr/bin/python3

from entry import Entry


class Schedule:
    def __init__(self, year=0, month=0):
        self.year = year
        self.month = month
        self.entries = []

    def add_entry(self, start_day, start_hour, stop_day, stop_hour, mode):
        self.entries.append(Entry(self.year, self.month, start_day, start_hour, stop_day, stop_hour, mode).get_entry())
