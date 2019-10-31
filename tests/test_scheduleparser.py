import pytest

import schedule_parser


@pytest.fixture
def good_schedule():
    '''Returns a ScheduleParser instance with a good schedule'''
    parser = schedule_parser.ScheduleParser('tests/test_schedules/good_schedule.txt')
    parser.read_schedule()
    return parser


def test_notes_dont_exist(good_schedule):
    assert good_schedule.notes_exist is False


def test_month(good_schedule):
    assert good_schedule.month == 9


def test_year(good_schedule):
    assert good_schedule.year == 2019
