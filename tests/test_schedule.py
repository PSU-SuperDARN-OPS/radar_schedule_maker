import pytest

from schedule import Schedule


@pytest.fixture
def good_schedule():
    return Schedule(2019, 1)


def test_add_one_entry_to_schedule(good_schedule):
    good_schedule.add_entry(1, 0, 2, 4, 'Common')
    assert good_schedule.get_entries() == [
        {'Time String': '2019 01 01 00 00   1680', 'Mode': 'Common', 'Radars': ['ALL']}]


def test_add_two_entries_to_schedule(good_schedule):
    good_schedule.add_entry(1, 0, 2, 4, 'Common')
    good_schedule.add_entry(1, 0, 2, 4, 'Special')
    assert good_schedule.get_entries() == [
        {'Time String': '2019 01 01 00 00   1680', 'Mode': 'Common', 'Radars': ['ALL']},
        {'Time String': '2019 01 01 00 00   1680', 'Mode': 'Special', 'Radars': ['ALL']}]
