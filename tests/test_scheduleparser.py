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


def test_month(good_schedule_legacy):
    good_schedule_legacy.set_date()
    assert good_schedule_legacy.month == 9


def test_year(good_schedule_legacy):
    good_schedule_legacy.set_date()
    assert good_schedule_legacy.year == 2019


def test_notes(good_schedule, monkeypatch):
    # Override the Python built-in input method
    monkeypatch.setattr('builtins.input', lambda x: 'y')
    good_schedule.get_notes()
    assert good_schedule.notes['Note A'] == "NORMALSCAN"

