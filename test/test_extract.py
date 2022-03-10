import pytest
import string
import random
import psycopg2
from src.store import storeInvoice
from src.extract import extract
from test.xmlString import xml_as_string
#import xml.etree.ElementTree as ET

DATABASE_URL = "postgres://hugfbhqshfeuxo:bb21e74bd662eb54bbfb67841e33cb3994fee2526208ee3667c736777acd8658@ec2-44-195-191-252.compute-1.amazonaws.com:5432/drj7scqvv00fb"

def test_store():
    fileName = (''.join(random.choice(string.ascii_lowercase) for i in range(4)) )
    storeInvoice(xml_as_string,fileName)
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    #Open a cursor for db operations
    cur = conn.cursor()
    
    
    # assert extract(fileName)[0] = fileName
    # assert extract(fileName)[1] = xml_as_string

    #Insert File Name and XML into 
    filenamereturned, xmlreturned = extract(fileName)
    assert filenamereturned == fileName
    # sql = "SELECT filename FROM invoices WHERE FileName = %s"
    # val = (fileName)
    # cur.execute(sql,[val])
    # retFileName = cur.fetchone()
    # print(type(retFileName))
    # retFileName = retFileName[0]
    # assert retFileName == fileName
    # cur.close()
