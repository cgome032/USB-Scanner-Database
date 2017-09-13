import pyodbc

class DatabaseConnect:

    def __init__(self,connection=None):
        self.connection = connection

    def connectDatabase(connectionString):
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



if __name__ == '__main__':
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=WESTSERV2.WESTCOINDUSTRIES.local;DATABASE=Material Inventory;UID=sa;PWD=EY9x35qK')

