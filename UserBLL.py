from DBCONNECTION import *


class UserBLL:

    def registerUser(self, name, email, phone, address, gender, payment, password, licenseplate, usertype):
        DB = DBConnection()
        getConnection = DB.getConn()
        cursor = getConnection.cursor()
        SQL = "SELECT * FROM USER WHERE EMAIL='" + email + "'"
        cursor.execute(SQL)
        userExist = cursor.fetchall()

        if (len(userExist) >= 1):
            return 0
        else:
            SQL1 = "INSERT INTO USER(name, email, phone, address, gender, payment, password, licenseplate, usertype) values(%s, %s,%s, %s, %s, %s, %s, %s, %s)"
            VALUES = (name, email, phone, address, gender, payment, password, licenseplate, usertype)
            cursor.execute(SQL1, VALUES)
            getConnection.commit()
            return 1

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
