import pytest
from src.search import search
from src.store import store
from test.xml_str_for_search import generate_random_date, generate_random_name, generate_unique_xml
PASSWORD = "searchtest"
"""
Summary: function test for invoice_seach
    - invoice_search takes in at least one non keyword argument and perform a seach in the database to extract the most relevant e-invoice to the key searched by the user
    
    
Assumptions:
    - 
    
Exceptions occurs when:
    - the user is not authorised (HTTP status code: 403)
    - there is no argument passed in (status code: 400)
    
Success Output:
    {
        "invoice": ["an xml file as a string"]
    }

No match output:
    {
        "invoice": []
    }
    
"""

# testing the multiple search function


def store_helper():
    date = generate_random_date()
    sender_name = generate_random_name(60)
    xml = generate_unique_xml(date, sender_name)
    xml_name = generate_random_name(10)
    store(xml, xml_name, PASSWORD)
    return {
        'issue_date': date,
        'sender_name': sender_name,
        'xml': xml,
        'xml_name': xml_name
    }


'''
def test_search_issue_date_only():
    invoice_info = store_helper()
    second_xml_name = generate_random_name(10)
    store(invoice_info['xml'], second_xml_name)
    assert search([invoice_info['issue_date']], ['']) == (
        [invoice_info['xml_name'], second_xml_name])
'''


def test_search_sender_name_only():
    invoice_info = store_helper()
    second_xml_name = generate_random_name(10)
    store(invoice_info['xml'], second_xml_name, PASSWORD)
    assert search([''], [invoice_info['sender_name']], PASSWORD) == (
        [invoice_info['xml_name'], second_xml_name])


def test_search_multiple_arg():
    invoice_info = store_helper()
    assert search([invoice_info['issue_date']], [invoice_info['sender_name']], PASSWORD) == [
        invoice_info['xml_name']]


def test_search_multiple_no_match():
    store_helper()
    with pytest.raises(Exception):
        search(["Ebusiness Software Services Pty Ltd"],
               ["1930-02-20"], PASSWORD)


def test_search_multiple_no_args():
    with pytest.raises(Exception):
        search([''], [''], PASSWORD)
