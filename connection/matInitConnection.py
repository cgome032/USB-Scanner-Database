import pyodbc
from Material import material
import csv


class MatDatabaseConnect:

    """ Initial database function upon creation """
    def __init__(self):
        self.connection = None
        self.__loginId = None

        # Connection to Mike Manning server
        self.sqlServer = 'SQL Server'
        self.server = 'WESTSERV2\SQLEXPRESS'
        self.database = 'ProNest12'
        self.userId='carlosg'
        self.password='EY9x35qK'
        self.connectionString = 'DRIVER={'+self.sqlServer+'};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.userId+';PWD='+self.password

    """ Function to connect to Materials database """
    def connectDatabase(self):
        # Specifying the ODBC driver, server name, database, etc. directly
        self.connection = pyodbc.connect(self.connectionString)
        print('You are connected')

    """ Function to grab all data from Materials database """
    def getDatabase(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM PlateInv ORDER BY PlateID")
        data = cursor.fetchall()
        for material in data:
            print(material)


    """ 
        Function to grab specific item from Materials database
        returns material item from database in the form of a dictionary 
    """
    def getMaterialItem(self,materialId):

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM PlateInv WHERE PlateID=" + str(materialId))
        columns = cursor.description
        detail = []
        for column in columns:
            detail.append(column[0])
        data = list(cursor.fetchone())
        matDict = dict(zip(detail,data))
        chosenMaterial = material(matDict)
        print(chosenMaterial.Description)

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
    newDatabase = MatDatabaseConnect()
    newDatabase.connectDatabase()
    if newDatabase.connection is not None:
        print("Connection completed")
        newDatabase.getMaterialItem(input("Enter id: "))
    else:
        print("Connection not completed")

