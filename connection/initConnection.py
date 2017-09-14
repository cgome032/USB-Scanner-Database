import pyodbc

class DatabaseConnect:

    """ Initial database function upon creation """
    def __init__(self,connection=None):
        self.connection = connection
        self.__loginId = None


    """ Function to connect to Materials database """
    def connectDatabase(self):
        # Specifying the ODBC driver, server name, database, etc. directly
        self.connection = pyodbc.connect('DRIVER={SQL Server};SERVER=WESTSERV2.WESTCOINDUSTRIES.local;DATABASE=Material_Inventory;UID=sa;PWD=EY9x35qK')
        print('You are connected')

    """ Function to verify employee credentials against employee database """
    def verifyCredentials(self,user_id,user_pw):
        cursor = self.connection.cursor()
        cursor.execute("""Select Employee_id From employeeDatabase WHERE Employee_password='%s'""" % (user_pw))
        data = cursor.fetchall()
        __loginId = data[0]
        print(__loginId)
        return True

    """ Function to grab all data from Materials database """
    def getDatabase(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM materialAttributes ORDER BY Material_id")
        data = cursor.fetchall()
        print(data)


    """ Function to grab specific item from Materials database """
    def getMaterialItem(self,materialId):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM materialAttributes WHERE Material_id=" + materialId)
        data = cursor.fetchall()
        print(data)


    """ Function to grab all materials of a specific type """
    def getAllMaterials(self, materialType):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM materialAttributes WHERE Material_type=" + materialType)
        data = cursor.fetchall()
        print(data)

    """ Function to delete material from inventory """
    def takeMaterial(self, materialId):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM materialAttributes WHERE Material_id=" + materialId)
        data = cursor.fetchall()
        print(data)


if __name__ == '__main__':
    initConnectionString = 'DRIVER={SQL Server};SERVER=WESTSERV2.WESTCOINDUSTRIES.local;DATABASE=Material_Inventory;UID=sa;PWD=EY9x35qK'
    connection = pyodbc.connect(initConnectionString)
    print("Connection completed")

