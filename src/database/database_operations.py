import mysql.connector
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

    def __init__(self) -> None:
        """
        This method creates sql connection and cursor
        Parameters = self
        Return Type = None
        """
        try:
            self.connection = mysql.connector.connect(user='root',
                password='Pratiksha15@Skit',
                host='127.0.0.1',
                database='covid_vaccine_tracker'
            )
            self.cursor = self.connection.cursor(dictionary=True)
            
        except mysql.connector.Error:
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
        # pw = "Pratiksha15@"
        # hash = hashlib.sha256(pw.encode()).hexdigest()
        # self.cursor.execute('INSERT INTO auth VALUES (?,?,?,?,?)', (1111, "pratiksha15@gmail.com", hash, "Admin", "True",))
        self.connection.commit()


    def save_data(self, query: Union[str, list], data: Union[tuple, list]) -> None:
        """
        This method saves data in the database
        """
        if isinstance(query, str):
            self.cursor.execute(query, data)
        else:
            for i in range(0, len(query)):
                self.cursor.execute(query[i], data[i])
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