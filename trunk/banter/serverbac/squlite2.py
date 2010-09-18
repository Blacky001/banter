import sqlite3
connection = sqlite3.connect('banter.db')
cursor = connection.cursor()
#sql = """CREATE TABLE Userdetails (id INTEGER PRIMARY KEY AUTOINCREMENT,fname TEXT,lname TEXT,uname TEXT UNIQUE,passwd TEXT )"""   
#sql = "INSERT INTO Userdetails (fname,lname,uname,passwd ) VALUES ('vijesh', 'v','vijay','catfoss')"
#sql = "INSERT INTO Settings (setting, value) VALUES ('display_molecule_name', 'True')"
#sql = "UPDATE Userdetails SET lanme='vv' WHERE fanme='vijesh'"
#sql = "DELETE FROM Userdetails WHERE id=1"
sql = "SELECT * FROM Userdetails"
cursor.execute(sql)
#print cursor.lastrowid   # get the autoincremented id from the previously inserted record
data = cursor.fetchall()
print data
connection.commit()
connection.close()
