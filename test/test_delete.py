"""
Delete Function:

    - Given a user's desired e-invoice, this function will remove said invoice from the data base if it exists

Assumptions:
    - 
"""
import pytest
import string
import random
import psycopg2
from src.store import storeInvoice
from src.remove import removeInvoice
from src.extract import extract
from test.xmlString import xml_as_string
#import xml.etree.ElementTree as ET

#DATABASE_URL = "postgres://hugfbhqshfeuxo:bb21e74bd662eb54bbfb67841e33cb3994fee2526208ee3667c736777acd8658@ec2-44-195-191-252.compute-1.amazonaws.com:5432/drj7scqvv00fb"

def test_delete():
    # store a file 
    fileName = (''.join(random.choice(string.ascii_lowercase) for i in range(4)))
    storeInvoice(xml_as_string,fileName)

    # double check file has been stored
    output = extract(fileName)
    assert output[0] == fileName

    # delete the file
    removeInvoice(fileName)
    output = extract(fileName)
    assert output == None

def test_file_nonexistant():
    # store a file
    fileName = (''.join(random.choice(string.ascii_lowercase) for i in range(4)))
    storeInvoice(xml_as_string,fileName)

    # double check file has been stored
    output = extract(fileName)
    assert output[0] == fileName

    # try and delete a different file
    # the random file name generated is 4 characters
    fileName = 'abc'
    output = removeInvoice(fileName)
    assert output == "File name does not exist"

def test_filename_not_string():
    # store a file with filename as a string
    fileName = '1234'
    storeInvoice(xml_as_string,fileName)

    # double check file has been stored
    output = extract(fileName)
    assert output[0] == fileName

    # attempt to delete fileName as an int
    with pytest.raises(Exception):
        removeInvoice(1234)