import sqlite3

conn = sqlite3.connect('Users.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE Users
    (userID INT PRIMARY KEY,
     userName VARCHAR(80),
     email VARCHAR(80),
     loginPassword VARCHAR(40),
     creditCard INT,
     city VARCHAR(80),
     state VARCHAR(80),
     country VARCHAR(80),
     address VARCHAR(80),
     phone INT)''')
