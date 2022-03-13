import psycopg2
from src.extract import extract


def removeInvoice(file_name: str):

    if isinstance(file_name, str) == 0:
        raise Exception(description="Invalid file name: must be a string")

    try:
        DATABASE_URL = "postgres://hugfbhqshfeuxo:bb21e74bd662eb54bbfb67841e33cb3994fee2526208ee3667c736777acd8658@ec2-44-195-191-252.compute-1.amazonaws.com:5432/drj7scqvv00fb"

        # Connect to DB
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')

        # Open a cursor for db operations
        cur = conn.cursor()

        # Check the file exists
        extractOutput = extract(file_name)

        if extractOutput is None:
            return "File name does not exist"

        # Remove invoice via file_name
        sql = "DELETE FROM invoices WHERE file_name = %s"
        val = file_name
        cur.execute(sql, [val])

        # Save changes
        conn.commit()

        # Close DB connection
        cur.close()
        conn.close()

        return "Invoice deleted"
    except Exception as e:
        print(e)
