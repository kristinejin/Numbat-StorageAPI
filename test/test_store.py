# # Surya Gunasekaran
# # Team Fudge 

# '''
# Store Function 
    
#     - Given an XML file, parses the data and stores important information in DB.
#     - Invoice id is unique

# Assumptions:

#     - Function is called, storeInvoice(String,String)
#         - Param1: xml, as string
#         - Param2: filename, as string
#             Filename Rules:
#                 - Min 1 char :: Max 50 char
#                 - valid Regex = valid_email = '^[a-zA-Z0-9]+[\\._]?[a-zA-Z0-9]+[@]\\w+[.]\\w{2,3}$'

#         - returns "file saved" on success
#         - returns "error" on error

#     - Function is called, retrieveInvoice(String)
#         - Param1: filename, as string
#         - Returns xml, as string
    
# List of possible errors:
    
#     - Wrong file format. Not xml
#     - Do not have permission to retrieve file
#     - Wrong file name to retrive


# '''
import pytest
import string
import random
import psycopg2
from src.store import storeInvoice
# from xmlString import xml_as_string

DATABASE_URL = "postgres://hugfbhqshfeuxo:bb21e74bd662eb54bbfb67841e33cb3994fee2526208ee3667c736777acd8658@ec2-44-195-191-252.compute-1.amazonaws.com:5432/drj7scqvv00fb"

def test_store():
    fileName = (''.join(random.choice(string.ascii_lowercase) for i in range(10)) )
    storeInvoice(fileName,xml_as_string)
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    #Open a cursor for db operations
    cur = conn.cursor()
    
    #Insert File Name and XML into 
    sql = "SELECT * FROM invoices where FileName = %s"
    val = (fileName)
    cur.execute(sql,val)
    retFileName, retXml = cur.fetchone()
    assert retFileName == fileName
    assert retXml == xml_as_string

# #Standard store and retrieve. No errors
# def test_StoreRetrive_normal():
#     fileName = "file1"
#     storeInvoice(fileName,xmlString)
#     conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    
#     #once invoice stored successfully
#     ret = retriveInvoice(fileName)
#     assert ret == xml_as_string

# def test_StoreRetrive_not_einvoice():
#     fileName = "file1"
#     with pytest.raises(Exception) as e:
#         ret = storeInvoice("not_xml_as_string", fileName)

# def test_StoreRetrive_fileNotfound():
#     fileName = "file1"
#     wrongFilename = "file2"
#     ret = storeInvoice("xml_as_string", fileName)
#     assert ret == "file saved"
#     #once invoice stored successfully
#     with pytest.raises(Exception) as e:
#         ret = retriveInvoice(wrongFilename)

# """
# File test to be written:
    
#     - Auth function and permission when retriving the file
#     - file name rules test 
# """

