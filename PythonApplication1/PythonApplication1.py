from sqlalchemy import *

#make engine and connect to MS SQL Server using DSN from ODBC
db = create_engine('mssql+pyodbc://aab')

#connect to db
db.connect();

#execute select command with raw SQL
result = db.execute("SELECT QuestionId FROM Questions")

names = []
for row in result:
    names.append(row[0])

#print result
print(names)