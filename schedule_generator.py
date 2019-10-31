#!/usr/bin/python3
# Minimum requirements are Python 3.6

import schedule_parser as ps
from radar_modes import radar


class ScheduleGenerator(object):
    def __init__(self, site, channel, schedule_file):
        self.site = site
        self.site_channel = channel
        self.schedule_file = schedule_file
        self.check = False
        self.default_priority = 5
        self.generic_schedule = []
        self.header = ''
        self.schedule = []

    def get_schedule(self):
        parser = ps.ScheduleParser(self.schedule_file)
        parser.run()
        self.generic_schedule = parser.get_schedule()

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

        for line in self.generic_schedule:
            if line['Mode'] != 'Common' and line['Mode'] != 'Discretionary':
                self.schedule.append(f"# >>> Schedule Note <<< "
                                     f"The following entry is operating in the mode {line['Mode']}")

            self.schedule.append(f"{line['Time String']:6} "
                                 f"{self.default_priority:>3} "
                                 f"{radar[self.site]['Control Program']} "
                                 f"--stid {self.site} "
                                 f"{radar[self.site]['Mode'][line['Mode']]} "
                                 f"{radar[self.site]['Control Program Arguments']} "
                                 f"--df {radar[self.site]['Day Frequency']} "
                                 f"--nf {radar[self.site]['Night Frequency']} "
                                 f"-c {ord(self.site_channel) - 96}")

    def print_schedule(self):
        for line in range(len(self.schedule)):
            print(f"{self.schedule[line]:100} {self.generic_schedule[line]['Mode'] if self.check else ''}")


if __name__ == '__main__':
    generator = ScheduleGenerator('kod', 'd', 'dec.txt')
    generator.get_schedule()
    generator.generate_schedule()
    generator.print_schedule()
