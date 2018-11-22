from random import choice

from faker import Faker


def create_random_data_list():
    """Create  a list of 200000 dicts with random data."""
    fake = Faker()
    keys = (
        "first_name",
        "last_name",
        "address",
        "email",
        "sex",
        "state",
        "city",
        "country",
        "phone_number",
    )
    count_of_fake_data = range(200000)
    data_list = [
        {i: choose_data(i, fake) for i in keys} for i in count_of_fake_data
    ]
    return data_list


def choose_data(data_line, fake):
    """Generate random data."""
    if data_line == "sex":
        data = choice(["man", "woman"])
    else:
        data = getattr(fake, data_line)()
    return data


def choose_job(fake, data_dict, data_dict_value):
    """Create random job position for list of dicts with random job position."""
    if data_dict_value == "job_position":
        return fake.job()
    else:
        return data_dict.get(data_dict_value)


def create_random_job_list(data_list):
    """Create a list of dicts with random job position."""
    fake = Faker()
    keys = ["first_name", "last_name", "job_position"]
    list_dicts_name_job = [
        {y: choose_job(fake, i, y) for y in keys} for i in data_list
    ]
    return list_dicts_name_job
