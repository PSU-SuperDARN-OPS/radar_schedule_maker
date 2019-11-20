#!/usr/bin/python3


class Entry:
    """
    This class stores all the information about a single scheduled event.

    Parameters
    ----------
    year : int
        Year of the schedule file
    month : int
        Month of the schedule file
    start_day : int
        Start day of the event
    start_hour : int
        Start hour of the event
    stop_day : int
        Stop day of the event
    stop_hour : int
        Stop hour of the event
    mode : string
        The operating category/mode of the radar for the event. Possible modes include 'Common' and 'Discretionary'
        Special modes also include the desired special mode.
        For example, a Themisscan entry would be: 'Special:THEMISSCAN'
    radar : list of strings
        Lists which radars the entry applies to. Most often this is 'ALL'.
    """
    def __init__(self, year=0, month=0, start_day=0, start_hour=0, stop_day=0, stop_hour=0, mode='', radar=['ALL']):
        self.year = year
        self.month = month
        self.start_day = start_day
        self.start_hour = start_hour
        self.stop_day = stop_day
        self.stop_hour = stop_hour
        self.mode = mode
        self.radar = radar

    def get_duration(self):
        """Calculates the duration based on the start and stop"""
        return (self.stop_day - self.start_day) * (24 * 60) \
               + (self.stop_hour - self.start_hour) * 60

    def get_time_string(self):
        """Returns the start time and duration of the entry in the Scheduler format"""
        return f"{self.year} {self.month:02} " \
            f"{self.start_day:02} {self.start_hour:02} 00 {self.get_duration():6}"

    def get_entry_string(self):
        """Returns the formatted time string, the mode, and the radars the entry applies to as a string"""
        return f"{self.get_time_string()} {self.mode} {self.radar}"

    def get_entry(self):
        """Returns the formatted time string, the mode, and the radars the entry applies to in a dictionary"""
        return {'Time String': self.get_time_string(),
                'Mode': self.mode,
                'Radars': self.radar}

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
