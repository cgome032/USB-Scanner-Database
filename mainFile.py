import pyodbc

# Specifying the ODBC driver, server name, database, etc. directly
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=WESTSERV2.WESTCOINDUSTRIES.local;DATABASE=Material Inventory;UID=sa;PWD=EY9x35qK')


# Using a DSN, but providing a password as well
#cnxn = pyodbc.connect('DSN=test;PWD=password')

# Create a cursor from the connection
cursor = connection.cursor()
cursor.execute("SELECT * FROM materialAttributes ORDER BY Material_id")
data = cursor.fetchall()
print (data)