import pytest

import schedule_parser


@pytest.fixture
def good_schedule_legacy():
    """Returns a ScheduleParser instance with a good schedule"""
    parser = schedule_parser.ScheduleParser('tests/test_schedules/good_schedule_no_notes_legacy.txt')
    parser.read_schedule()
    return parser


@pytest.fixture
def good_schedule():
    """Returns a ScheduleParser instance with a good schedule"""

    parser = schedule_parser.ScheduleParser('tests/test_schedules/good_schedule_notes.txt')
    parser.read_schedule()
    return parser


def test_notes_dont_exist_legacy(good_schedule_legacy):
    assert good_schedule_legacy.notes_exist is False


# Test for set_date
def test_month(good_schedule_legacy):
    good_schedule_legacy.set_date()
    assert good_schedule_legacy.month == 9

# Test for set_date
def test_year(good_schedule_legacy):
    good_schedule_legacy.set_date()
    assert good_schedule_legacy.year == 2019


def test_read_schedule(good_schedule):
    assert good_schedule.raw_date == "December 2019"
    assert good_schedule.raw_operations[0] == "01:00    03:06    Common Time (1-min)"
    assert good_schedule.raw_notes[0] == "Note A: NORMALSCAN - This is a spacecraft working group request to support"


def test_notes(good_schedule, monkeypatch):
    # Override the Python built-in input method
    monkeypatch.setattr('builtins.input', lambda x: 'y')

    good_schedule.get_notes()
    assert good_schedule.notes['Note A'] == "NORMALSCAN"
    assert good_schedule.notes['Note C'] == "RBSPSCAN"


def test_operation(good_schedule, monkeypatch):
    # Override the Python built-in input method
    monkeypatch.setattr('builtins.input', lambda x: 'y')

    good_schedule.get_notes()
    good_schedule.get_operation()
    assert good_schedule.print_schedule() == ""
