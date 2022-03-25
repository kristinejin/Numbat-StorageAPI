import psycopg2
from src.config import DATABASE_URL


def extract(file_name: str, password: str):
    """given a file name, return the invoice associate with the file name

    Args:
        file_name (str): the file name that the user wants to extract

    Returns:
        tuple: consisting (file_name, invoice_file) on success

    Exception:
        when connect to db failed
    """
    assert isinstance(file_name, str), 'Please provide the filename as a string'

    try:
        # Connect to DB
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')

        # Open a cursor for db operations
        cur = conn.cursor()

        # Extract File Name and XML
        sql = "SELECT XML FROM invoices WHERE File_name = %s AND password = %s"
        val = (file_name, password)
        cur.execute(sql, list(val))
        return_val = cur.fetchone()
        # Close DB connection
        cur.close()
        conn.close()
        return return_val

    except Exception as e:
        print(e)
