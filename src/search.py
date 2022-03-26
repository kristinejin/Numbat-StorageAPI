import psycopg2
from src.config import DATABASE_URL


def search(issue_date: list, sender_name: list, password: str):
    """_summary_
    Args:
       - issue_date (list): a list of a single issue date as a string, can be empty if sender name is not empty
       - sender_name (list): a list of a single sender name as a string, can be empty if sender name is not empty

    Exceptions:
        - Both inputs are empty
        - No file matches the searched keys
        - Connection to database failed

    Returns:
       list of file name that matches the user search on success
    """

    empty_input = ['']
    request_list = []

    # check if both inputs are empty
    if issue_date == empty_input and sender_name == empty_input:
        raise Exception("Please input at least one key")

    if issue_date != empty_input and issue_date[0] != None:
        request_list.append(f"issue_date = '{issue_date[0]}'")

    if sender_name != empty_input and sender_name[0] != None:
        request_list.append(f"sender_name = '{sender_name[0]}'")

    # generating querying command
    if issue_date != empty_input and sender_name != empty_input:
        request_list = ' AND '.join(request_list)
    else:
        request_list = request_list[0]
    ret_list = []

    try:
        # connect to db
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()

        # extracting desired invoice names
        cur.execute(
            f"SELECT file_name FROM invoices WHERE {request_list} AND password = '{password}'"
        )
        rows = cur.fetchall()
        # close db connection
        cur.close()
        conn.close()
        # coverting a list of tuple to a list
        for t in rows:
            for name in t:
                ret_list.append(name)
    except Exception as e:
        print(e)

    # check if the return list is empty
    if ret_list == []:
        raise Exception("There is no invoice match your search")

    return ret_list
