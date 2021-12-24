import mysql.connector
import datetime
from datetime import datetime
import os
import database
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')

def setlone(lone_no,amount,loen_date,addher,intrest,name,tr_type):
    a1 = str(name)
    a2 = str(addher)
    a3 = str(loen_date)
    a4 = str(amount)
    a5 = tr_type
    s0 = str(lone_no)
    s1 = str(amount)
    s2 = loen_date.replace("/"," ")
    s3 = str(intrest)
    datetime_object =datetime.strptime(s2,'%Y %m %d')

    month_name = datetime_object.strftime("%B")
    month_name1 = datetime_object.strftime("%b")
    trn_no = database.count_transaction_detail()
    print(month_name1)
    # month_name1 = str(month_name)
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    cur.execute("update lone_info set Lone_take ="+s1+" ,Intrest = "+ s3+ " Where lone_no = "+s0)

    cur.close()
    conn.commit()
    conn.close()
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    trn_data = [trn_no,a1,a2,a3,a4,a5]
    print(trn_data)
    cur.execute("insert into transaction_detail (transaction_no, name, addher_no, date, amount, remark) values(%s,%s,%s,%s,%s,%s)",trn_data)
    cur.close()
    conn.commit()
    conn.close()

def set_intrest_amount(lone_no,Collect_date,amount,intrest):
    am = amount
    intr = intrest
    s1 = lone_no
    s2 = Collect_date.replace("/", " ")
    datetime_object = datetime.strptime(s2, '%Y %m %d')
    month_name = datetime_object.strftime("%B")
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    cur.execute("""Update lone_info set ="""+Collect_date+"""where lone_no = """+s1)




