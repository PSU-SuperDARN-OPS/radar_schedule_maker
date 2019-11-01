#!/usr/bin/python3

from entry import Entry


class Schedule:
    def __init__(self, year=0, month=0):
        self.year = year
        self.month = month
        self.entries = []
