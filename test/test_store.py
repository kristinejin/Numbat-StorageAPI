import pytest
import string
import random
from src.store import store
from src.extract import extract
from test.xml_str import xml_as_string
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
    store(xml_as_string, file_name)
    elmt = extract(file_name)
    assert elmt[0] == file_name
    assert elmt[1] == xml_as_string


def test_duplicated_filename():
    # test for saving a file with a file name that already exist in the db
    # stores the first invoice
    file_name = (''.join(random.choice(string.ascii_lowercase)
                         for i in range(4)))
    store(xml_as_string, file_name)
    elmt = extract(file_name)
    assert elmt[0] == file_name
    assert elmt[1] == xml_as_string

    # try to save an invoice with the same filename
    with pytest.raises(Exception):
        store(xml_as_string, file_name)


def test_store_xml_not_string():
    # test for when the xml is not in string format
    with pytest.raises(Exception):
        store(9999, 'helloworld')
