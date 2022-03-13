import xml.etree.ElementTree as ET
import psycopg2
from src.extract import extract

DATABASE_URL = "postgres://hugfbhqshfeuxo:bb21e74bd662eb54bbfb67841e33cb3994fee2526208ee3667c736777acd8658@ec2-44-195-191-252.compute-1.amazonaws.com:5432/drj7scqvv00fb"


def storeInvoice(xml: str, file_name: str):

    if not isinstance(xml, str):
        raise Exception("Please provide the invoice xml in a string")

    # raise an error if there's a file in the database associate with the given file name
    if extract(file_name):
        raise Exception("This file name is taken! Please try another one.")

    # Convert string to XML
    root = ET.fromstring(xml)

    # Extract key from XML
    key_list = []
    for child in root.iter():
        if child.text.strip():
            key_list.append(child.text)
    issue_date = key_list[4]
    sender_name = key_list[10]

    try:
        DATABASE_URL = "postgres://hugfbhqshfeuxo:bb21e74bd662eb54bbfb67841e33cb3994fee2526208ee3667c736777acd8658@ec2-44-195-191-252.compute-1.amazonaws.com:5432/drj7scqvv00fb"
        # Connect to DB
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')

        # Open a cursor for db operations
        cur = conn.cursor()

        # Insert data into db
        sql = "INSERT INTO invoices VALUES (%s,XMLPARSE (DOCUMENT %s), %s, %s)"
        val = (file_name, xml, issue_date, sender_name)
        cur.execute(sql, val)

        # Save changes
        conn.commit()

        # Close DB connection
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Cannot connect to the database, {e}")
