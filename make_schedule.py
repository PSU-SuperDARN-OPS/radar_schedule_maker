#!/usr/bin/python3
# Minimum requirements are Python 3.6

import parse_schedule as ps
from radar_modes import radar

parser = ps.parse_schedule('nov.txt')
parser.read_schedule()
parser.generate_schedule()

check = False

schedule = parser.get_schedule()

site = "kod"
site_channel = 'd'
default_priority = 5

header = (f"path {radar[site]['Control Program Path']}\n"
          f"default {radar[site]['Control Program']} --stid {site} {radar[site]['Control Program Arguments']} "
          f"--df {radar[site]['Day Frequency']} --nf {radar[site]['Night Frequency']} "
          f"-c {ord(site_channel) - 96}\n"
          f"stationid {site}\n"
          f"sitelib ros\n"
          f"channel {site_channel}\n"
          f"priority 1\n"
          f"duration a\n\n")

print(header)
new_schedule = []

for line in schedule:
    new_schedule.append(f"{line['Time String']:6} "
                        f"{default_priority:>3} "
                        f"{radar[site]['Control Program']} "
                        f"--stid {site} "
                        f"{radar[site]['Mode'][line['Mode']]} "
                        f"{radar[site]['Control Program Arguments']} "
                        f"--df {radar[site]['Day Frequency']} "
                        f"--nf {radar[site]['Night Frequency']} "
                        f"-c {ord(site_channel) - 96}")

for line in range(len(new_schedule)):
    print(f"{new_schedule[line]:100} {schedule[line]['Mode'] if check else ''}")
