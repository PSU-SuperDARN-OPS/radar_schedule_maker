#!/usr/bin/python3
# Minimum requirements are Python 3.6

import schedule_parser as ps
from radar_modes import radar


class ScheduleGenerator(object):
    """
    Takes a schedule object that has been parsed and generates the file the scheduler on a radar needs
    """
    def __init__(self, site, channel, schedule_object):
        self.site = site
        self.site_channel = channel
        self.check = False
        self.default_priority = 5
        self.generic_schedule = schedule_object.get_entries()
        self.header = ''
        self.schedule = []

    def generate_header(self):
        self.header = (f"path {radar[self.site]['Control Program Path']}\n"
                       f"default {radar[self.site]['Control Program']} "
                       f"--stid {self.site} "
                       f"{radar[self.site]['Control Program Arguments']} "
                       f"--df {radar[self.site]['Day Frequency']} --nf {radar[self.site]['Night Frequency']} "
                       f"-c {ord(self.site_channel) - 96}\n"
                       f"stationid {self.site}\n"
                       f"sitelib ros\n"
                       f"channel {self.site_channel}\n"
                       f"priority 1\n"
                       f"duration a\n\n")

    def print_header(self):
        print(self.header)

    def generate_schedule(self):
        for scheduled in self.generic_schedule:
            if scheduled['Mode'] != 'Common' and scheduled['Mode'] != 'Discretionary':
                self.schedule.append(f"# >>> Schedule Note <<< "
                                     f"The following entry is operating in the mode {scheduled['Mode']}")

            self.schedule.append(f"{scheduled['Time String']:6} "
                                 f"{self.default_priority:>3} "
                                 f"{radar[self.site]['Control Program']} "
                                 f"--stid {self.site} "
                                 f"{radar[self.site]['Mode'][scheduled['Mode']]} "
                                 f"{radar[self.site]['Control Program Arguments']} "
                                 f"--df {radar[self.site]['Day Frequency']} "
                                 f"--nf {radar[self.site]['Night Frequency']} "
                                 f"-c {ord(self.site_channel) - 96}")

    def print_schedule(self):
        for line in range(len(self.schedule)):
            print(f"{self.schedule[line]:100} {self.generic_schedule[line]['Mode'] if self.check else ''}")

    def get_schedule(self):
        schedule_output = ''
        for line in range(len(self.schedule)):
            schedule_output += f"{self.schedule[line]:100} {self.generic_schedule[line]['Mode'] if self.check else ''}\n"

        return schedule_output

    def run(self):
        self.generate_schedule()


if __name__ == '__main__':
    schedule = ps.ScheduleParser('tests/test_schedules/good_schedule_notes.txt')
    schedule.run()
    generator = ScheduleGenerator('kod', 'd', schedule.get_schedule())
    generator.generate_schedule()
    generator.print_schedule()
