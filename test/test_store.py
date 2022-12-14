import pytest
import string
import random
from src.store import store
from src.extract import extract
from test.xml_str import xml_as_string
PASSWORD = "password"
PASSWORD_ALTER = "password2"
'''
Store Function 
    
    - Given an XML file, parses the data and stores important information in DB.
    - Invoice id is unique

Assumptions:

    - Function is called, store(String,String)
        - Param1: xml, as string
        - Param2: filename, as string
            Filename Rules:
                - Min 1 char :: Max 50 char
                - valid Regex = valid_email = '^[a-zA-Z0-9]+[\\._]?[a-zA-Z0-9]+[@]\\w+[.]\\w{2,3}$'

        - returns "file saved" on success
        - returns "error" on error

    - Function is called, retrieveInvoice(String)
        - Param1: filename, as string
        - Returns xml, as string
    
List of possible errors:
    
    - Wrong file format. Not xml
    - Do not have permission to retrieve file
    - Wrong file name to retrive

'''


def test_store_success():
    # test for successfully save a file
    file_name = (''.join(random.choice(string.ascii_lowercase)
                         for i in range(4)))
    store(xml_as_string, file_name, PASSWORD)
    assert xml_as_string == extract(file_name, PASSWORD)[0]


def test_duplicated_fname_diff_pass():
    # test for saving a file with a file name that already exist in the db
    # stores the first invoice
    file_name = (''.join(random.choice(string.ascii_lowercase)
                         for i in range(4)))
    store(xml_as_string, file_name, PASSWORD)
    assert extract(file_name, PASSWORD)[0] == xml_as_string

    # try to save an invoice with the same filename but different password
    store(xml_as_string, file_name, PASSWORD_ALTER)
    assert extract(file_name, PASSWORD_ALTER)[0] == xml_as_string


def test_duplicated_fname_and_password():
    # test for saving a file with a file name that already exist in the db
    # stores the first invoice
    file_name = (''.join(random.choice(string.ascii_lowercase)
                         for i in range(4)))
    store(xml_as_string, file_name, PASSWORD)
    assert xml_as_string == extract(file_name, PASSWORD)[0]

    # try to save an invoice with the same filename
    with pytest.raises(Exception):
        store(xml_as_string, file_name, PASSWORD)


def test_store_xml_not_string():
    file_name = (''.join(random.choice(string.ascii_lowercase)
                         for i in range(4)))
    # test for when the xml is not in string format
    with pytest.raises(Exception):
        store(9999, file_name, PASSWORD)


def test_store_invalid_xml():
    file_name = (''.join(random.choice(string.ascii_lowercase)
                         for i in range(4)))
    with pytest.raises(Exception):
        store('invalid xml', file_name, PASSWORD)
