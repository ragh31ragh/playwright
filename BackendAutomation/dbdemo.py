import mysql.connector
#host,databases,username,password
#connection string  ,connection object
conn = mysql.connector.connect(host='localhost',database='PythonAutomation',
                        user='raga',password = ' root ')
result = conn.is_connected()#it will return true or false
print(result)

cursor = conn.cursor()
cursor.execute('select * from customerInfo')
row = cursor.fetchone()
print(row )
#the printed row will be tuple
#('selenium',datetime.date(2020,6,7),120,'Africa')
print(row[3])
#Africa
rowsall= cursor.fetchall()#list of tuples

allrows = cursor.fetchall()