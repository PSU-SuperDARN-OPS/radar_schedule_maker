import pytest

import schedule_parser
import schedule_generator


@pytest.fixture
def good_schedule_legacy():
    """Returns a ScheduleParser instance with a good schedule"""
    parser = schedule_parser.ScheduleParser('tests/test_schedules/good_schedule_no_notes_legacy.txt')
    parser.run()
    return parser


@pytest.fixture
def good_schedule(monkeypatch):
    """Returns a ScheduleParser instance with a good schedule"""
    # Override the Python built-in input method
    monkeypatch.setattr('builtins.input', lambda x: 'y')
    parser = schedule_parser.ScheduleParser('tests/test_schedules/good_schedule_notes.txt')
    parser.run()
    return parser


def test_generate_header(good_schedule):
    gen = schedule_generator.ScheduleGenerator('kod', 'c', good_schedule.get_schedule())
    gen.generate_header()

    assert gen.header == 'path /home/radar/rst/usr/bin\n' \
                         'default uafscan --stid kod --xcf 1 --fast --df 10400 --nf 10400 -c 3\n' \
                         'stationid kod\n' \
                         'sitelib ros\n' \
                         'channel c\n' \
                         'priority 1\n' \
                         'duration a\n\n'

def test_generate_schedule(good_schedule):
    gen = schedule_generator.ScheduleGenerator('kod', 'c', good_schedule.get_schedule())
    gen.run()
    assert gen.schedule[0] == "2019 12 01 00 00   3240   5 uafscan --stid kod  --xcf 1 --fast --df 10400 --nf 10400 -c 3"
    assert gen.schedule[2] == "2019 12 03 12 00   4320   5 uafscan --stid kod --di --xcf 1 --fast --df 10400 --nf 10400 -c 3"
    assert gen.schedule[9] == "# >>> Schedule Note <<< The following entry is operating in the mode Special:THEMISSCAN"
    assert gen.schedule[10] == "2019 12 19 06 00    720   5 uafscan --stid kod  --xcf 1 --fast --df 10400 --nf 10400 -c 3"
