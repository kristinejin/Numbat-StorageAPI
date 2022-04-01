CREATE TABLE Invoices(
    id1 SERIAL PRIMARY KEY, 
    File_Name TEXT NOT NULL,
    XML     TEXT NOT NULL,
    Issue_Date  DATE,
    Sender_Name TEXT,
    Password TEXT NOT NULL,
    UNIQUE (File_Name, Password)

);


INSERT INTO Invoices(id1, File_Name, XML, Issue_Date, Sender_Name, Password)
VALUES (DEFAULT, 'whatsup', 'ssddfasfa','2022-02-02','Michael','kristine');