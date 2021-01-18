from typing import Any, Tuple

import mysql.connector as MYDB


class DBConnection:
    @staticmethod
    def getConn():
        conn = MYDB.connect(
            host="localhost",
            user="root",
            password="",
            database="taxibookingsystem"
        )
        return conn
