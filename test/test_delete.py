"""
Delete Function:

    - Given a user's desired e-invoice, this function will remove said invoice from the data base if it exists

Assumptions:
    - 
"""
import pytest

from src.store import storeInvoice
from src.remove_invoice import removeInvoice
from src.extract import extract
from sample_xml import xml_as_string, not_xml_as_string

# Test deleting an exising xml with no errors
def test_delete_normal():

    # Populate the db with an invoice
    fileName = "file1"
    output = storeInvoice("xml_as_string", fileName)
    assert output == "file saved"

    # Attempt to delete the saved invoice
    output = delete_invoice('EBWASP1002')  # ---> check with surya is this is the ID and same for the test below
    assert output == "Invoice deleted"

    # Check invoice is no longer in db
    with pytest.raises(Exception):
        retriveInvoice(filename)

# Test deleting a non existant file
def test_delete_nonexistant():

    # Populate db with a invoices
    fileName = "file1"
    wrongFilename = "file2"
    output = storeInvoice("xml_as_string", fileName)
    assert output == "file saved"

    # attempt to delete 'wrongFilename'
    with pytest.raises(Exception):
        delete_invoice('EBWASP1002' + 'SENG2021')


