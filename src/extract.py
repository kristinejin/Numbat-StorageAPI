def extract(filename: str):
    assert isinstance(filename, str), 'Please provide the xml as a string'

#Convert string to XML
    # root = ET.fromstring(xml)
    

#Extract key from XML
#     list1 = []
#     for child in root.iter():
#         if child.text.strip():
#             list1.append(child.text)

# #Store key and XML in DB

#     #Connect to DB
    try:
      DATABASE_URL = "postgres://hugfbhqshfeuxo:bb21e74bd662eb54bbfb67841e33cb3994fee2526208ee3667c736777acd8658@ec2-44-195-191-252.compute-1.amazonaws.com:5432/drj7scqvv00fb"
      conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    #Open a cursor for db operations
      cur = conn.cursor()
    
    #Extract File Name and XML 
      sql = "SELECT * FROM invoices WHERE FileName = %s"
      val = (filename)
      cur.execute(sql,val)
      retFileName, retXml = cur.fetchone()
      print(retFileName)
      

    #Save changes
      #conn.commit()

    #Close DB connection
      cur.close()
      conn.close()
    except Exception as e:
      print(e)
