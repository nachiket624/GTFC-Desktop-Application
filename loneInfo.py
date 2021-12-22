import mysql.connector
import datetime
from datetime import datetime
import os
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')


# x = datetime.datetime.now()
#
# month = (x.strftime("%m"))
# print(month)
def setlone(lone_no,amount,loen_date):
    s0 = str(lone_no)
    s1 = str(amount)
    s2 = loen_date.replace("/"," ")
    # print(s2)
    datetime_object =datetime.strptime(s2,'%Y %m %d')

    month_name = datetime_object.strftime("%B")
    print(month_name)
    month_name1 = str(month_name)
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    cur.execute("update lone_info set "+month_name1+" = "+s1+" Where lone_no = "+s0)
    cur.close()
    conn.commit()
    conn.close()
# setlone(6,700,"2000/3/3")





