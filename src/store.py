import xml.etree.ElementTree as ET
import psycopg2
from src.extract import extract
from src.config import DATABASE_URL


def store(xml: str, file_name: str):
    """given a standardised e-invoice xml in a string and a file name, save this e-invoice to database with the file name.

    Args:
        xml (str): the e-invoice that the user wants to be saved
        file_name (str): the file name that the user wants the e-invoice to be saved with

    Raises:
        Exception: when the invoice xml is not a string
        Exception: when file name already exists in the db
        Exception: when connection to db failed
    """
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
