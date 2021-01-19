from typing import Any, Tuple

import mysql.connector as MYDB

# Class for DB connection
class DBConnection:
    # Static method that returns connection connection variable of database
    @staticmethod
    def getConn():
        conn = MYDB.connect(
            host="localhost",
            user="root",
            password="",
            database="taxibookingsystem"
        )
        return conn
