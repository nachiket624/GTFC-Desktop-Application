import os
import datetime
import mysql.connector
entered = ('2', 'Nachiket', 'Anil', 'Parjane', 'O+', 'Nachiket11', datetime.date(2003, 1, 1), datetime.date(2000, 1, 1), 234234234123, '234234234', 123123123, 1312141412, 'nachiket@mail.com', '100')

d = tuple(entered)
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')
conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
cur = conn.cursor()
id1 = d[0]
date = d[6]
print()
input_data=(date,id1)
command = ("""update memberinfo set nomine = %s where id = %s""",input_data)
print(command)
cur.execute("""update memberinfo set data_of_brith = %s where id = %s""",input_data)
cur.close()
conn.commit()
# conn.close()