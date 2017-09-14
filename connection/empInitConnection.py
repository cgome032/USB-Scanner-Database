import pyodbc

class EmpDatabaseConnect:

    """ Initial database function upon creation """
    def __init__(self):
        self.connectionString = 'DRIVER={SQL Server};SERVER=WESTSERV2.WESTCOINDUSTRIES.local;DATABASE=Material_Inventory;UID=sa;PWD=EY9x35qK'
        self.__loginId = None


    """ Function to connect to Materials database """
    def connectDatabase(self):
        # Specifying the ODBC driver, server name, database, etc. directly
        self.connection = pyodbc.connect(self.connectionString)
        print('You are connected')

    """ Function to verify employee credentials against employee database """
    def verifyCredentials(self,user_id,user_pw):
        cursor = self.connection.cursor()
        cursor.execute("""Select Employee_id From employeeDatabase WHERE Employee_username='%s' AND Employee_password='%s'""" % (user_id,user_pw))
        data = cursor.fetchone()
        if data == None:
            print("Employee not found")
        else:
            __loginId = data[0]
            print(__loginId)
        return True

    """ Function to grab all data from Materials database """
    def getDatabase(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM employeeDatabase ORDER BY Employee_id")
        data = cursor.fetchall()
        print(data)


if __name__ == '__main__':
    initConnectionString = 'DRIVER={SQL Server};SERVER=WESTSERV2.WESTCOINDUSTRIES.local;DATABASE=Material_Inventory;UID=sa;PWD=EY9x35qK'
    connection = pyodbc.connect(initConnectionString)
    print("Connection completed")

