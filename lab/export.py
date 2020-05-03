import csv
import cx_Oracle

username = 'hr'
password = '11'
database = 'localhost/ORCL'


connection = cx_Oracle.connect(username, password, database)

cursor = connection.cursor()

tables = ["Player", "Teams", "Years"]

for table in tables:
    with open(table+'.csv', 'w', newline='') as file:
        all_records = csv.writer(file)

        query = 'select * from '+ table

        cursor.execute(query)

        column = [i[0] for i in cursor.description]

        all_records.writerow(column)

        for i in cursor:
            all_records.writerow(i)


cursor.close()
connection.close()