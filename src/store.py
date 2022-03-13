import psycopg2
from src.extract import extract

DATABASE_URL = "postgres://hugfbhqshfeuxo:bb21e74bd662eb54bbfb67841e33cb3994fee2526208ee3667c736777acd8658@ec2-44-195-191-252.compute-1.amazonaws.com:5432/drj7scqvv00fb"


def storeInvoice(xml: str, filename: str):

    if not isinstance(xml, str):
        raise Exception("Please provide the invoice xml in a string")

    # raise an error if there's a file in the database associate with the given filename
    if extract(filename):
        raise Exception("This filename is taken! Please try another one.")

    try:
        # Connect to DB
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')

        # Open a cursor for db operations
        cur = conn.cursor()

        # Insert File Name and XML into
        sql = "INSERT INTO invoices VALUES (%s,XMLPARSE (DOCUMENT %s))"
        val = (filename, xml)
        cur.execute(sql, val)

        # Save changes
        conn.commit()

        # Close DB connection
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
