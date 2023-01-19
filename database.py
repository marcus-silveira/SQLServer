import pyodbc


class SQLServer:
    """
    This is a class that sets up a SQLServer connection using the 'pyodbc' library

    ...

    Attributes
    __________

    :param driver (str): Microsoft ODBC Driver for SQL Server is a single dynamic-link library (DLL) containing run-time
     support for applications using native-code APIs to connect to SQL Server.
    :param server (str): Server where the query will be made
    :param database (str): Database used in the query
    :param username (str): User with access to the Database
    :param password(str): User password
    :param cnxn (pyodbc.Connection): Accepts an ODBC connection string and returns a new Connection object.
    :param cursor (pyodbc.Cursor): Return a new Cursor object using the connection

    Methods
    _______
    execute_query(query):
        performs the query
    execute_read_query(query):
        read the query
    close_connection():
        close the connection
    exception(error):
        static method that returns the error type
    :
    """

    def __init__(self, server: str = '***', database: str = '***', username: str = '***', password: str = '***!@'):
        """
        Constructs all the necessary attributes

        :param server: Server where the query will be made
        :param database: Database used in the query
        :param username: User with access to the Database
        :param password: User password
        """
        self.driver: str = '{ODBC Driver 17 for SQL Server}'
        self.server: str = server
        self.database: str = database
        self.username: str = username
        self.password: str = password
        self.cnxn: pyodbc.Connection = pyodbc.connect(f'DRIVER={self.driver};SERVER={self.server};DATABASE='
                                                      f'{self.database};UID={self.username};PWD={self.password}')
        self.cursor: pyodbc.Cursor = self.cnxn.cursor()

    def execute_query(self, query: str) -> pyodbc.Cursor:
        """
        Prepare and execute a database query or command
        :param query: str
        :return: returns a Cursor representing a database cursor, which is used to manage the context
        of a search operation
        """
        try:
            return self.cursor.execute(query)
        except pyodbc.ProgrammingError as error:
            self.exception(error)

    def execute_read_query(self, query: str) -> list:
        """
        Reads the cursor object and turns it into a list
        :param query: str
        :return: Returns a list of query information
        """
        cursor = self.cnxn.cursor()
        try:
            return cursor.execute(query).fetchall()
        except pyodbc.ProgrammingError as error:
            self.exception(error)
            return []

    def close_connection(self) -> None:
        """
        Close the connection
        :return:
        """
        try:
            self.cursor.close()
        except pyodbc.ProgrammingError as error:
            self.exception(error)
        try:
            self.cnxn.close()
        except pyodbc.ProgrammingError as error:
            self.exception(error)

    @staticmethod
    def exception(error):
        return print(
            f'Exception raised for programming errors, e.g. table not found or already exists, syntax error in '
            f'the SQL statement, wrong number of parameter specified, etc.\n'
            f'An error of type occurred: {error}')


if __name__ == '__main__':
    db = SQLServer()
   
