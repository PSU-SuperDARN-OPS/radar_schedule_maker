import pytest

import schedule_parser


@pytest.fixture
def good_schedule_legacy():
    '''Returns a ScheduleParser instance with a good schedule'''
    parser = schedule_parser.ScheduleParser('tests/test_schedules/good_schedule_no_notes_legacy.txt')
    parser.read_schedule()
    return parser


def test_notes_dont_exist(good_schedule_legacy):
    assert good_schedule_legacy.notes_exist is False


def test_month(good_schedule_legacy):
    assert good_schedule_legacy.month == 9


def test_year(good_schedule_legacy):
    assert good_schedule_legacy.year == 2019
