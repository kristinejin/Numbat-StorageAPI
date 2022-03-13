import psycopg2


def extract(file_name: str):
    assert isinstance(file_name, str), 'Please provide the xml as a string'

    try:
        # Connect to DB
        DATABASE_URL = "postgres://hugfbhqshfeuxo:bb21e74bd662eb54bbfb67841e33cb3994fee2526208ee3667c736777acd8658@ec2-44-195-191-252.compute-1.amazonaws.com:5432/drj7scqvv00fb"
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')

        # Open a cursor for db operations
        cur = conn.cursor()

        # Extract File Name and XML
        sql = "SELECT * FROM invoices WHERE file_name = %s"
        val = (file_name)
        cur.execute(sql, [val])
        returnvalues = cur.fetchone()
        # Close DB connection
        cur.close()
        conn.close()

        return returnvalues

    except Exception as e:
        print(e)
