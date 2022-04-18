CREATE TABLE invoices (
    id1 SERIAL PRIMARY KEY,
    file_name text NOT NULL,
    xml text NOT NULL,
    issue_date date,
    sender_name text,
    password text NOT NULL,
    buyer_name text,
    amount_payable decimal(20, 2),
    tax_payable decimal(20, 2),
    goods_payable decimal(20, 2),
    UNIQUE (File_Name, Password)
);

INSERT INTO Invoices(id1, File_Name, XML, Issue_Date, Sender_Name, Password)
VALUES (DEFAULT, 'whatsup', 'ssddfasfa','2022-02-02','Michael','kristine');