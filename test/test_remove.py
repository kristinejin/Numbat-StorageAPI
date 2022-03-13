"""
Delete Function:

    - Given a user's desired e-invoice, this function will remove said invoice from the data base if it exists

Assumptions:
    - 
"""
import pytest
import string
import random
from src.store import storeInvoice
from src.remove import removeInvoice
from src.extract import extract
from test.xmlString import xml_as_string


def test_remove_success():
    # store a file
    fileName = (''.join(random.choice(string.ascii_lowercase)
                for i in range(4)))
    storeInvoice(xml_as_string, fileName)

    # double check file has been stored
    output = extract(fileName)
    assert output[0] == fileName

    # delete the file
    removeInvoice(fileName)
    output = extract(fileName)
    assert output == None


def test_remove_file_nonexistant():
    # store a file
    fileName = (''.join(random.choice(string.ascii_lowercase)
                for i in range(4)))
    storeInvoice(xml_as_string, fileName)

    # double check file has been stored
    output = extract(fileName)
    assert output[0] == fileName

    # try and delete a different file
    # the random file name generated is 4 characters
    fileName = 'abc'
    output = removeInvoice(fileName)
    assert output == None


def test_remove_filename_not_string():
    # store a file with file_name as a string
    integer = random.randint(1000, 9999)
    file_name = f'{integer}'
    storeInvoice(xml_as_string, file_name)

    # double check file has been stored
    output = extract(file_name)
    assert output[0] == file_name

    # attempt to delete file_name as an int
    with pytest.raises(Exception):
        removeInvoice(integer)
