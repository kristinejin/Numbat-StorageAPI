import pytest
import string
import random
import psycopg2
from src.store import storeInvoice
from test.xmlString import xml_as_string
#import xml.etree.ElementTree as ET

DATABASE_URL = "postgres://hugfbhqshfeuxo:bb21e74bd662eb54bbfb67841e33cb3994fee2526208ee3667c736777acd8658@ec2-44-195-191-252.compute-1.amazonaws.com:5432/drj7scqvv00fb"

def test_delete():
    fileName = (''.join(random.choice(string.ascii_lowercase) for i in range(4)) )
    storeInvoice(xml_as_string,fileName)

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    #Open a cursor for db operations
    cur = conn.cursor()
    
    #Insert File Name and XML into 
    sql = " SELECT fileName FROM invoices WHERE fileName = %s"
    val = (fileName)
    cur.execute(sql,[val])
    retFileName = cur.fetchone()
    retFileName = retFileName[0]
    assert retFileName == fileName

    #confirmed file saved
    #now delete
    storeDelete(fileName)
    sql = " SELECT fileName FROM invoices WHERE fileName = %s"
    val = (fileName)
    cur.execute(sql,[val])
    retFileName = cur.fetchone()
    retFileName = retFileName[0]
    assert retFileName == None


    cur.close()
    
