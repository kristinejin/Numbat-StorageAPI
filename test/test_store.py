import pytest
import string
import random
from src.store import storeInvoice
from src.extract import extract
from test.xmlString import xml_as_string
'''
# Store Function 
    
    - Given an XML file, parses the data and stores important information in DB.
    - Invoice id is unique

Assumptions:

    - Function is called, storeInvoice(String,String)
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
    file_name = (''.join(random.choice(string.ascii_lowercase)
                         for i in range(4)))
    storeInvoice(xml_as_string, file_name)
    elmt = extract(file_name)
    assert elmt[0] == file_name
    assert elmt[1] == xml_as_string


def test_duplicated_filename():
    # stores the first invoice
    file_name = (''.join(random.choice(string.ascii_lowercase)
                         for i in range(4)))
    storeInvoice(xml_as_string, file_name)
    elmt = extract(file_name)
    assert elmt[0] == file_name
    assert elmt[1] == xml_as_string

    # try to save an invoice with the same filename
    with pytest.raises(Exception):
        storeInvoice(xml_as_string, file_name)


def test_store_xml_not_string():
    with pytest.raises(Exception):
        storeInvoice(9999, 'helloworld')
