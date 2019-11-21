#!/usr/bin/python3
# Minimum requirements are Python 3.6

import argparse
import schedule_generator
import schedule_parser

parser = argparse.ArgumentParser(description='SuperDARN Schedule Maker')
site_group = parser.add_mutually_exclusive_group(required=True)

site_group.add_argument("--site", default=None, type=str,
                        help='Station or site ID for a radar [Example: kod, mcm, sps, adw, ade]')
parser.add_argument("--channel", "-c", default='a', type=str, choices=['a', 'b', 'c', 'd'],
                    help='Channel of the radar [Example: a, b, c, d]')
site_group.add_argument("--sitelist", default=None, type=str, nargs='*',
                        help="List of station ID followed by a period and channel letter [Example: kod.c, kod.d]")
parser.add_argument("-m", "--month", type=int, choices=range(1, 13),
                    help="Enter the numeric value for the month of the schedule")
parser.add_argument("-y", "--year", type=int, help="Enter the year of the schedule")

args = parser.parse_args()

print(args.sitelist)

schedule_file = f"{args.year}{args.month:02}.swg"
schedule_path = f"external/schedules/{args.year}/"

schedule = schedule_parser.ScheduleParser(schedule_path + schedule_file)
schedule.run()

generator = schedule_generator.ScheduleGenerator('kod', 'd', schedule_path + schedule_file)
generator.run()
generator.print_schedule()
