#!/usr/bin/python3
# Minimum requirements are Python 3.6

import parse_schedule as ps

parser = ps.parse_schedule('nov.txt')
parser.read_schedule()
parser.generate_schedule()
# parser.print_schedule()

schedule = parser.get_schedule()

site = "kod"
site_channel = 'd'
site_day_frequency = 10400
site_night_frequency = 10400
control_program_path = "/home/radar/rst/usr/bin"
control_program = "uafscan"
priority = 5

header = (f"path {control_program_path}\n"
          f"default {control_program} --stid {site} --xcf 1 --fast "
          f"--df {site_day_frequency} --nf {site_night_frequency} "
          f"-c {ord(site_channel) - 96}\n"
          f"stationid {site}\n"
          f"sitelib ros\n"
          f"channel {site_channel}\n"
          f"priority 1\n"
          f"duration a\n\n")

print(header)
new_schedule = []

for line in schedule:
    if line['Mode'] == 'Common':
        mode = f""
    elif line['Mode'] == 'Discretionary':
        mode = f"--di"
    else:
        mode = ""

    new_schedule.append(f"{line['Time String']:6} {priority:>3} {control_program} --stid {site} {mode} --xcf 1 --fast "
                        f"--df {site_day_frequency} --nf {site_night_frequency} -c {ord(site_channel) - 96}")

for line in new_schedule:
    print(line)
