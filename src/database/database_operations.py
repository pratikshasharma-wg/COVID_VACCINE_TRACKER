import hashlib
import pymysql
from typing import Union

from config.queries.db_queries import DbConfig


class DBOperations:
    """
    This class contains method to perform all database related operations
    ...
    Methods
    -------
    init() : Creates connection and cursor
    create_all_tables() : Creates all the tables if not exists in database
    save_data() : Saves data in database
    fetch_data() : Fetches data from database
    """
    connection = None
    cursor = None

    def __init__(self) -> None:
        """
        This method creates sql connection and cursor
        Parameters = self
        Return Type = None
        """
        if DBOperations.connection is None:
            try:
                DBOperations.connection = pymysql.connect(
                    user='avnadmin',
                    password='AVNS_cl7x1MQtwAjEsPLPmUg',
                    cursorclass=pymysql.cursors.DictCursor,
                    host='mysql-1debdabb-pratikshas152001-e8c8.a.aivencloud.com',
                    database='my_db',
                    port = 27856
                )
                DBOperations.cursor = DBOperations.connection.cursor()
            except pymysql.Error:
                print("Connection to DB cannot be made. Please try again!")


    def create_tables(self) -> None:
        """
        This method creates all tables of not exists
        Parameters = self
        Return Type = None
        """
        self.cursor.execute(DbConfig.CREATE_AUTH_TABLE)
        self.cursor.execute(DbConfig.CREATE_USER_DETAILS_TABLE)
        self.cursor.execute(DbConfig.CREATE_DOSE_DETAILS_TABLE)
        self.cursor.execute(DbConfig.CREATE_ADMIN_APPROVAL_TABLE)
        self.cursor.execute(DbConfig.CREATE_VACCINE_TABLE)
        self.cursor.execute(DbConfig.CREATE_REVOKED_TOKENS_TABLE)
        
        # pw = "Pratiksha15@"
        # hash = hashlib.sha256(pw.encode()).hexdigest()
        # self.cursor.execute('INSERT INTO auth VALUES (%s,%s,%s,%s,%s)', (1111, "pratiksha15@gmail.com", hash, "Admin", 'True',))


    def save_data(self, query: str, data: tuple) -> None:
        """
        This method saves data in the database
        """
        self.cursor.execute(query, data)
        self.connection.commit()


    def fetch_data(self, query: str, tup: tuple = None) -> list:
        """
        This method fetches data from the database
        """
        if not tup:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, tup)
        data = self.cursor.fetchall()
        return data


db = DBOperations()
