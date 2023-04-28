import sqlite3
from datetime import date

conn = sqlite3.connect('Inventory_and_Users_and_Orders_Updated.db')
curs = conn.cursor()

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def obtainInventoryItem(inventoryID):
    sql = 'SELECT * FROM Inventory WHERE inventoryID ='
    inventoryID = str(inventoryID)
    curs.execute(sql + " " + inventoryID)
    row = curs.fetchone()
    return row

def deleteInventoryItem(inventoryID):
    sql = 'DELETE FROM Inventory WHERE inventoryID ='
    inventoryID = str(inventoryID)
    curs.execute(sql + " " + inventoryID)
    conn.commit()

def obtainUser(userID):
    sql = 'SELECT * FROM Users WHERE userID ='
    userID = str(userID)
    curs.execute(sql + " " + userID)
    row = curs.fetchone()
    return row

def deleteInventoryItem(userID):
    sql = 'DELETE FROM Users WHERE userID ='
    useID = str(userID)
    curs.execute(sql + " " + userID)
    conn.commit()

class User():
    def __init__(self):
        pass

    def newUser(self, userID, userName, email, loginPassword, creditCard, address, city, state, country, phone):
        self.userID = userID
        self.userName = userName
        self.email = email
        self.loginPassword = loginPassword
        self.creditCard = creditCard
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.phone = phone

    def outputUser(self):
        print(f"User ID: {self.userID}")
        print(f"User Name: {self.userName}")
        print(f"User Email: {self.email}")
        print(f"User Passowrd: {self.loginPassword}")
        print(f"User Credit Card: {self.creditCard}")
        print(f"User Address: {self.address}")
        print(f"User City: {self.city}")
        print(f"User State: {self.state}")
        print(f"User Country: {self.country}")
        print(f"Phone: {self.phone}")

    def addUser(self):
        insUser = 'INSERT INTO Users (userID, userName, email, \
        loginPassword, creditCard, address, city, state, country, phone) \
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        curs.execute(insUser, (self.userID, self.userName, self.email, \
                               self.loginPassword, self.creditCard, self.address, \
                               self.city, self.state, self.country, self.phone))
        conn.commit()

    def retrieveUser(self, userID):
        getUser = 'SELECT * FROM Users WHERE userID ='
        userID = str(userID)
        curs.execute(getUser + " " + userID)
        userData = curs.fetchone()
        self.userID = userData[0]
        self.userName = userData[1]
        self.email = userData[2]
        self.loginPassword = userData[3]
        self.creditCard = userData[4]
        self.city = userData[5]
        self.state = userData[6]
        self.country = userData[7]
        self.address = userData[8]
        self.phone = userData[9]

    def updateInfo(self, userName, email, loginPassword, creditCard, address, city, state, country, phone):
        self.userName = userName
        self.email = email
        self.loginPassword = loginPassword
        self.creditCard = creditCard
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.phone = phone

    def commitUpdatedInfo(self):
        updUser = 'UPDATE Users SET userName = ?, email = ?, loginPassword = ?, \
                   creditCard = ?, address = ?, city = ?, state = ?, \
                   country = ?, phone = ? \
                   WHERE userID = ?'
        curs.execute(updUser, (self.userName, self.email, self.loginPassword, \
                               self.creditCard, self.address, self.city, \
                               self.state, self.country, self.phone, \
                               self.userID))
        conn.commit()

    def resetPassword(self, loginPassword):
        self.loginPassword = loginPassword

    def commitResetPassword(self):
        updPassword = 'UPDATE Users SET loginPassword = ? WHERE userID = ?'
        curs.execute(updPassword, (self.loginPassword, self.userID))
        conn.commit()

    def deleteUser(self):
        delUser = 'DELETE FROM Users WHERE userID ='
        userID = str(self.userID)
        curs.execute(delUser + " " + userID)
        conn.commit()

    def loginUser(self, userID, inputPassword):
        getUser = 'SELECT * FROM Users WHERE userID ='
        userID = str(userID)
        curs.execute(getUser + " " + userID)
        userData = curs.fetchone()

        correctPassword = userData[3]
        
        if inputPassword == correctPassword:
            self.userID = userData[0]
            self.userName = userData[1]
            self.email = userData[2]
            self.loginPassword = userData[3]
            self.creditCard = userData[4]
            self.city = userData[5]
            self.state = userData[6]
            self.country = userData[7]
            self.address = userData[8]
            self.phone = userData[9]
        else:
            print("Incorrect password.")
