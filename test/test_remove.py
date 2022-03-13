"""
Delete Function:

    - Given a user's desired e-invoice, this function will remove said invoice from the data base if it exists

Assumptions:
    - 
"""
import pytest
import string
import random
from src.store import store
from src.remove import remove
from src.extract import extract
from test.xml_str import xml_as_string


def test_remove_success():
    # store a file
    file_name = (''.join(random.choice(string.ascii_lowercase)
                         for i in range(4)))
    store(xml_as_string, file_name)

    # double check file has been stored
    output = extract(file_name)
    assert output[0] == file_name

    # delete the file
    remove(file_name)
    output = extract(file_name)
    assert output == None


def test_remove_file_nonexistant():
    # store a file
    file_name = (''.join(random.choice(string.ascii_lowercase)
                         for i in range(4)))
    store(xml_as_string, file_name)

    # double check file has been stored
    output = extract(file_name)
    assert output[0] == file_name

    # try and delete a different file
    # the random file name generated is 4 characters
    file_name = 'abc'
    output = remove(file_name)
    assert output == None


def test_remove_file_name_not_string():
    # store a file with file_name as a string
    integer = random.randint(1000, 9999)
    file_name = f'{integer}'
    store(xml_as_string, file_name)

    # double check file has been stored
    output = extract(file_name)
    assert output[0] == file_name

    # attempt to delete file_name as an int
    with pytest.raises(Exception):
        remove(integer)
