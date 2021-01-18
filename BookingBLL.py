from DBCONNECTION import *


class BookingBLL:
    def makeBooking(self, userid, date, time, pickup_location, dropoff_location):
        DB = DBConnection()
        getConnection = DB.getConn()
        cursor = getConnection.cursor()
        SQL1 = "INSERT INTO BOOKING(userid, date, time, pickup_location, dropoff_location, status) values(%s, %s,%s, %s, %s, %s)"
        VALUES = (userid, date, time, pickup_location, dropoff_location, "not confirmed")
        cursor.execute(SQL1, VALUES)
        getConnection.commit()
        return 1

    def fetchBookingsdata(self, userData):
        DB = DBConnection()
        getConnection = DB.getConn()
        cursor = getConnection.cursor()
        SQL = "SELECT * FROM BOOKING WHERE USERID = " + str(userData[0][0]) + ""
        cursor.execute(SQL)
        bookingDatas = cursor.fetchall()
        if len(bookingDatas) >= 1:
            return bookingDatas
        else:
            return 0

    def fetchBookingsdataForAdmin(self):
        DB = DBConnection()
        getConnection = DB.getConn()
        cursor = getConnection.cursor()
        SQL = "SELECT * FROM BOOKING B " \
              " LEFT JOIN USER U " \
              " ON B.USERID=U.ID"
        cursor.execute(SQL)
        bookingDatas = cursor.fetchall()
        if len(bookingDatas) >= 1:
            return bookingDatas
        else:
            return 0

    def cancelBooking(self, bookingid):
        DB = DBConnection()
        getConnection = DB.getConn()
        cursor = getConnection.cursor()
        SQL = "DELETE FROM BOOKING WHERE ID = " + str(bookingid) + ""
        cursor.execute(SQL)
        getConnection.commit()
        if cursor.rowcount >= 1:
            return 1
        else:
            return 0

    def confirmBooking(self, bookingId):
        DB = DBConnection()
        getConnection = DB.getConn()
        cursor = getConnection.cursor()
        SQL = "UPDATE BOOKING SET STATUS='confirmed' WHERE ID=" + bookingId + ""
        cursor.execute(SQL)
        getConnection.commit()
        if cursor.rowcount >= 1:
            return 1
        else:
            return 0
