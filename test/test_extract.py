import string
import random
from src.store import storeInvoice
from src.extract import extract
from test.xmlString import xml_as_string


# test simple extraction
def test_store_and_extract():
    fileName = (''.join(random.choice(string.ascii_lowercase) for i in range(4)) )
    storeInvoice(xml_as_string,fileName)
       
    
    #Insert File Name and XML into 
    return_values = extract(fileName)
    assert return_values[0] == fileName
    assert return_values[1] == xml_as_string

# extract non-existant file
def test_extract_file_not_found():
    fileName = (''.join(random.choice(string.ascii_lowercase) for i in range(4)) )
    storeInvoice(xml_as_string,fileName)
    
    
    # check that no file is returned
    return_values = extract(fileName + "Not in existance")
    assert return_values == None


"""
need additional testing for authorisation
    - attempting to extract an invoice that user does not have access to
"""
