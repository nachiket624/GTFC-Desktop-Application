# from LoneSaving.add_lone import lonedig
import mysql.connector
import os
import sys
import operator
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')
class trancationSavingLone():
    def savingtr(amount,date,id,addher):
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("SELECT count(*) from savingaccounttransaction")
        data = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        first_no = map(operator.itemgetter(0),data)
        for i in first_no:
            data1 = i
            print("Inside for loop")
            if data1 == 0:
                insert_data = [1 ,id,date,addher,amount]
                conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
                cur = conn.cursor()
                cur.execute("insert into savingaccounttransaction (TrNo , Id, date, addher_no, amount) values(%s,%s,%s,%s,%s)",insert_data)
                cur.close()
                conn.commit()
                conn.close()
            else:
                insert_data = [id,date,addher,amount]
                conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
                cur = conn.cursor()
                cur.execute("insert into savingaccounttransaction(Id, date, addher_no, amount) values(%s,%s,%s,%s)",insert_data)
                cur.close()
                conn.commit()
                conn.close()
