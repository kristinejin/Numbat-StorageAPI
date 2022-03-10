#import pytest
import string
import random
#import psycopg2
from src.store import storeInvoice
from src.extract import extract
from test.xmlString import xml_as_string
#import xml.etree.ElementTree as ET

DATABASE_URL = "postgres://hugfbhqshfeuxo:bb21e74bd662eb54bbfb67841e33cb3994fee2526208ee3667c736777acd8658@ec2-44-195-191-252.compute-1.amazonaws.com:5432/drj7scqvv00fb"

# test simple extraction
def test_store_and_extract():
    fileName = (''.join(random.choice(string.ascii_lowercase) for i in range(4)) )
    storeInvoice(xml_as_string,fileName)
    #conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    #Open a cursor for db operations
    #cur = conn.cursor()
    
    
    #Insert File Name and XML into 
    returnedvalues = extract(fileName)
    assert returnedvalues[0] == fileName
    #assert returnedvalues[1] == xml_as_string

# # extract non-existant file
# def test_extract_file_not_found():
#     fileName = (''.join(random.choice(string.ascii_lowercase) for i in range(4)) )
#     storeInvoice(xml_as_string,fileName)
#     #conn = psycopg2.connect(DATABASE_URL, sslmode='require')

#     with pytest.raises(Exception):
#         extract(fileName + 'Not in existance')

"""
need additional testing for authorisation
    - attempting to extract an invoice that user does not have access to
"""
