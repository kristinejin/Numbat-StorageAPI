import string
import random
from src.store import store
from src.extract import extract
from test.xml_str import xml_as_string


def test_store_and_extract():
    # test simple extraction
    fileName = (''.join(random.choice(string.ascii_lowercase)
                for i in range(4)))
    store(xml_as_string, fileName)

    # Insert File Name and XML into
    return_values = extract(fileName)
    assert return_values[0] == fileName
    assert return_values[1] == xml_as_string


def test_extract_file_not_found():
    # extract non-existant file
    fileName = (''.join(random.choice(string.ascii_lowercase)
                for i in range(4)))
    store(xml_as_string, fileName)

    # check that no file is returned
    return_values = extract(fileName + "Not in existance")
    assert return_values == None
