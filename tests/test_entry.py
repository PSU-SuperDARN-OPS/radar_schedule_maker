import pytest

import entry


@pytest.fixture
def default_entry():
    return entry.Entry()


@pytest.fixture
def good_entry():
    return entry.Entry(2019, 1, 1, 0, 10, 24, 'Common')


def test_default_entry_year(default_entry):
    assert default_entry.get_year() == 0


def test_default_entry_month(default_entry):
    assert default_entry.get_month() == 0
