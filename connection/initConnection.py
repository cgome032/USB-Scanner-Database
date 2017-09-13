import pyodbc

class DatabaseConnect:

    """ Initial database function upon creation """
    def __init__(self,connection=None):
        self.connection = connection


    """ Function to connect to Materials database """
    def connectDatabase(self,connectionString):
        # Specifying the ODBC driver, server name, database, etc. directly
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=WESTSERV2.WESTCOINDUSTRIES.local;DATABASE=Material Inventory;UID=sa;PWD=EY9x35qK')



    """ Function to grab all data from Materials database """
    def getDatabase(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM materialAttributes ORDER BY Material_id")
        data = cursor.fetchall()
        print(data)


    """ Function to grab specific item from Materials database """
    def getMaterialItem(self,materialId):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM materialAttributes WHERE Material_id=" + materialId)
        data = cursor.fetchall()
        print(data)


    """ Function to grab all materials of a specific type """
    def getAllMaterials(self, materialType):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM materialAttributes WHERE Material_type=" + materialType)
        data = cursor.fetchall()
        print(data)

    """ Function to delete material from inventory """
    def takeMaterial(self, materialId):
        cursor = connection.cursor()
        cursor.execute("DELETE FROM materialAttributes WHERE Material_id=" + materialId)
        data = cursor.fetchall()
        print(data)


if __name__ == '__main__':
    initConnectionString = 'DRIVER={SQL Server};SERVER=WESTSERV2.WESTCOINDUSTRIES.local;DATABASE=Material Inventory;UID=sa;PWD=EY9x35qK'
    connection = pyodbc.connect(initConnectionString)
    print("Connection completed")

