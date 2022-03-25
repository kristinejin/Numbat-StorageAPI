import psycopg2
from src.extract import extract
from src.config import DATABASE_URL


def remove(file_name: str, password: str):
    """given a file name of an invoice and a password, remove the invoice associate with the file name and password

    Args:
        file_name (str): the file name that the user wants to remove

    Raises:
        Exception: when file name is not a string
        Exception: when connection to db failed

    Returns:
        str: "invoice deleted" on success
    """
    if isinstance(file_name, str) == 0:
        raise Exception(description="Invalid file name: must be a string")

    try:
        # Connect to DB
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')

        # Open a cursor for db operations
        cur = conn.cursor()

        # Check the file exists
        extract_output = extract(file_name, password)

        if extract_output is None:
            raise Exception(description="File name does not exist or incorrect password")

        # Remove invoice via file_name
        sql = "DELETE FROM invoices WHERE (File_Name = %s AND Password = %s)"
        val = (file_name, password)
        cur.execute(sql, list(val))

        # Save changes
        conn.commit()

        # Close DB connection
        cur.close()
        conn.close()

        return 200
    except Exception as e:
        print(e)
