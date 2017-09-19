import pyodbc

class MatDatabaseConnect:

    """ Initial database function upon creation """
    def __init__(self):
        """
        # Connection to Westserv2 server
        self.sqlServer = 'SQL Server'
        self.server = 'WESTSERV2.WESTCOINDUSTRIES.local'
        self.database='Material_Inventory'
        self.userId='sa'
        self.password='EY9x35qK'
        """

        # Connection to Mike Manning server
        self.sqlServer = 'SQL Server'
        self.server = 'MMANNING64\MTCSOFTWARE'
        self.database = 'ProNest10'

        # self.connectionString = 'DRIVER={'+self.sqlServer+'};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.userId+';PWD='+self.password
        self.connectionString = 'DRIVER={' + self.sqlServer + '};SERVER=' + self.server + ';DATABASE=' + self.database + ';Trusted_Connection=True;'
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

