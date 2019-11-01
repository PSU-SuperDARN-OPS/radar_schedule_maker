import pytest

import entry


@pytest.fixture
def default_entry():
    return entry.Entry()


@pytest.fixture
def good_entry():
    return entry.Entry(2019, 1, 1, 0, 2, 4, 'Common')


def test_default_entry_year(default_entry):
    assert default_entry.get_year() == 0


def test_default_entry_month(default_entry):
    assert default_entry.get_month() == 0


def test_good_entry_year(good_entry):
    assert good_entry.get_year() == 2019


def test_good_entry_month(good_entry):
    assert good_entry.get_month() == 1


def test_good_entry_duration(good_entry):
    assert good_entry.get_duration() == 1680


def test_good_entry_time_string(good_entry):
    assert good_entry.get_time_string() == '2019 01 01 00 00   1680'


def test_good_entry_string(good_entry):
    assert good_entry.get_entry_string() == '2019 01 01 00 00   1680 Common'
