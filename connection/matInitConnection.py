import pyodbc

class MatDatabaseConnect:

    """ Initial database function upon creation """
    def __init__(self):
        self.connectionString = 'DRIVER={SQL Server};SERVER=WESTSERV2.WESTCOINDUSTRIES.local;DATABASE=Material_Inventory;UID=sa;PWD=EY9x35qK'
        #self.connectionString = 'DRIVER={SQL Server};SERVER=WESTSERV2.WESTCOINDUSTRIES.local;INSTANCE=SQLEXPRESS12;DATABASE=ProNest12;UID=cgomez;PWD=EY9x35qK'
        self.__loginId = None


    """ Function to connect to Materials database """
    def connectDatabase(self):
        # Specifying the ODBC driver, server name, database, etc. directly
        self.connection = pyodbc.connect(self.connectionString)
        print('You are connected')

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
    initConnectionString = MatDatabaseConnect().connectionString
    connection = pyodbc.connect(initConnectionString)
    if connection is not None:
        print("Connection completed")
    else:
        print("Connection not completed")

