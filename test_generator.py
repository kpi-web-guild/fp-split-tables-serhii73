"""Tests for generator."""

from pysize import get_size

from generator import create_random_data_list, create_random_job_list


def test_equal_size_data():
    """Generate a data and calculate right size."""

    # Generate a lists of dicts and calculate right size.
    data_list = create_random_data_list()
    assert get_size(data_list) > 133000000

    # Generate a lists of dicts and calculate right size.
    data_job = create_random_job_list(data_list)
    assert get_size(data_job) > 49800000
