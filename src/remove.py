#import xml.etree.ElementTree as ET
import psycopg2
from src.extract import extract


def removeInvoice(filename: str):

    if isinstance(filename, str) == 0:
      raise Exception (description="Invalid file name: must be a string")
# Convert string to XML
    # root = ET.fromstring(xml)
    # print(root)

# Store key and XML in DB

# Connect to DB
    try:
      DATABASE_URL = "postgres://hugfbhqshfeuxo:bb21e74bd662eb54bbfb67841e33cb3994fee2526208ee3667c736777acd8658@ec2-44-195-191-252.compute-1.amazonaws.com:5432/drj7scqvv00fb"
      conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # Open a cursor for db operations
      cur = conn.cursor()
    
    # Check the file exists
      extractOutput = extract(filename)

      if extractOutput is None:
        return "File name does not exist"

    # Remove invoice via filename
      sql = "DELETE FROM invoices WHERE filename = %s"
      val = filename
      cur.execute(sql,[val])

    # Save changes
      conn.commit()

    # Close DB connection
      cur.close()
      conn.close()

      return "Invoice deleted"
    except Exception as e:
      print(e)
