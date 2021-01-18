from DBCONNECTION import *


class AssignedBookingBLL:

    def assignDriver(self, driverid, bookingid):
        DB = DBConnection()
        getConnection = DB.getConn()
        cursor = getConnection.cursor()
        SQL = "SELECT * FROM ASSIGNEDBOOKING WHERE driverid='" + driverid + "' OR bookingid='" + bookingid + "'"
        cursor.execute(SQL)
        data = cursor.fetchall()
        if len(data) >= 1:
            return 0
        else:
            SQL1 = "INSERT INTO ASSIGNEDBOOKING(driverid, bookingid) values(%s, %s)"
            VALUES = (driverid, bookingid)
            cursor.execute(SQL1, VALUES)
            getConnection.commit()
            return 1

    def getAssignDrivers(self):
        DB = DBConnection()
        getConnection = DB.getConn()
        cursor = getConnection.cursor()
        SQL = "SELECT * FROM ASSIGNEDBOOKING A " \
              "LEFT JOIN USER U " \
              " ON A.driverid= U.ID " \
              "LEFT JOIN BOOKING B " \
              " ON A.bookingid= B.ID " \
              "LEFT JOIN USER UU " \
              " ON UU.id= B.userid"
        cursor.execute(SQL)
        data = cursor.fetchall()
        if len(data) >= 1:
            return data
        else:
            return 0

    def getDriversBoookings(self, driverid):
        DB = DBConnection()
        getConnection = DB.getConn()
        cursor = getConnection.cursor()
        SQL = "SELECT * FROM ASSIGNEDBOOKING A " \
              "LEFT JOIN USER U " \
              " ON A.driverid= U.ID " \
              "LEFT JOIN BOOKING B " \
              " ON A.bookingid= B.ID " \
              "LEFT JOIN USER UU " \
              " ON UU.id= B.userid " \
              " WHERE A.driverid = " + driverid + ""
        cursor.execute(SQL)
        data = cursor.fetchall()
        if len(data) >= 1:
            return data
        else:
            return 0
