#!/usr/bin/python3


class Entry:
    def __init__(self, year=0, month=0, start_day=0, start_hour=0, stop_day=0, stop_hour=0, mode=''):
        self.year = year
        self.month = month
        self.start_day = start_day
        self.start_hour = start_hour
        self.stop_day = stop_day
        self.stop_hour = stop_hour
        self.mode = mode

    def get_duration(self):
        return (self.stop_day - self.start_day) * (24 * 60) \
               + (self.stop_hour - self.start_hour) * 60

    def get_time_string(self):
        return f"{self.year} {self.month:02} " \
               f"{self.start_day:02} {self.start_hour:02} 00 {self.get_duration():6}"

    def get_entry_string(self):
        return f"{self.get_time_string()} {self.mode}"

    def get_entry(self):
        return {'Time String': self.get_time_string(),
                'Mode': self.mode}

# Everything below this may be unneeded
    def get_start_day(self):
        return self.start_day

    def get_start_hour(self):
        return self.start_hour

    def get_stop_day(self):
        return self.stop_day

    def get_stop_hour(self):
        return self.stop_hour

    def get_mode(self):
        return self.mode

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def set_start_day(self, start_day):
        self.start_day = start_day

    def set_start_hour(self, start_hour):
        self.start_hour = start_hour

    def set_stop_day(self, stop_day):
        self.stop_day = stop_day

    def set_stop_hour(self, stop_hour):
        self.stop_hour = stop_hour

    def set_mode(self, mode):
        self.mode = mode

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month
