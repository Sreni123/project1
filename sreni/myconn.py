import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='abc123')
print("Connected")
cur=conn.cursor()
print("cursor created")
cur.execute("create database india")
print("database created")
