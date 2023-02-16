import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='abc123',db='india')
print("Connected")
cur=conn.cursor()
print("cursor created")
cur.execute("select * from states")
data=cur.fetchone()
print(data)
#print ("deleted")
