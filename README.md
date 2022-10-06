# Numbat Storage API

This an API for e-invoice storage developed in Python and PostgresSQL that supports basic functionalities to manipulate the e-invoice database. 

Base url for requests: https://teamfudgeh17a.herokuapp.com

Routes
---
- /store
  Stores an e-invoice in xml or text format with a given name
  
- /remove
  Removes an e-invoice associates with a given name
 
- /extract
  Extracts an e-invoice associates with a given name

- /search
  Searches for e-invoices user have access to by keywords 
  
Restrictions / Authentication
---
1. Name of the e-invoice must be unique amongst the invoices an user stored
2. A user is identified an id we named 'password'

Future Improvements 
---
1. Stronger authentication: currently not really protecting user's data, will need to implement a comprehensive authentication feature including identifying a particular registered user by username, email, and passord etc.

2. Store and remove multiple e-invoices the same time
 

Notes
---
This API is built for SENG2021 (Software Engineering Workshop) project by myself, Mathew, Peter and Surya. I primarily worked on the storing e-invoice and searching e-invoices by keywords features. 
