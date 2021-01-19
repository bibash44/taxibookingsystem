from DBCONNECTION import *


# Business logic layer for User
class UserBLL:
    # Function to check existing user and add new user
    # Function takes name, email, phone, address, gender, payment, password, licenseplate, usertype as paramaters
    def registerUser(self, name, email, phone, address, gender, payment, password, licenseplate, usertype):
        DB = DBConnection()
        getConnection = DB.getConn()
        cursor = getConnection.cursor()
        # Check if the user exist based on email
        SQL = "SELECT * FROM USER WHERE EMAIL='" + email + "'"
        cursor.execute(SQL)
        userExist = cursor.fetchall()

        if (len(userExist) >= 1):
            return 0
        else:
            # Add new user if the user doesnot exist
            SQL1 = "INSERT INTO USER(name, email, phone, address, gender, payment, password, licenseplate, usertype) values(%s, %s,%s, %s, %s, %s, %s, %s, %s)"
            VALUES = (name, email, phone, address, gender, payment, password, licenseplate, usertype)
            cursor.execute(SQL1, VALUES)
            getConnection.commit()
            return 1

    # Function to check login based on email and password
    # Function takes email and password as paramaters
    def loginUser(self, email, password):
        DB = DBConnection()
        getConnection = DB.getConn()
        cursor = getConnection.cursor()
        SQL = "SELECT * FROM USER WHERE EMAIL='" + email + "' AND PASSWORD='" + password + "' LIMIT 1"
        cursor.execute(SQL)
        userData = cursor.fetchall()

        if (len(userData) >= 1):
            return userData

        else:
            return 0

    # Function to get users data that has user type driver
    def getDriverDatas(self):
        DB = DBConnection()
        getConnection = DB.getConn()
        cursor = getConnection.cursor()
        SQL = "SELECT * FROM USER WHERE USERTYPE='driver'"
        cursor.execute(SQL)
        userData = cursor.fetchall()

        if (len(userData) >= 1):
            return userData

        else:
            return 0
