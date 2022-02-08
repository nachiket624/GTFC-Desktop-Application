import os
import mysql.connector
import operator
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')

class mainTransactionTable():
    def transaction_saving(Id,name,addher,date,amount,remark):
        conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("""select count(*) from transaction_detail""")
        data = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        first_no = map(operator.itemgetter(0), data)
        for i in first_no:
            data1 = i
            if data1 == 0:
                tr_no = 1
                insert_data = [tr_no,Id, name, addher, date, amount,remark]
                conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
                cur = conn.cursor()
                cur.execute(
                    "Insert into transaction_detail (transaction_no, Id,name,addher_no,date, amount,remark) values(%s,%s,%s,%s,%s,%s,%s)",
                    insert_data)
                cur.close()
                conn.commit()
                conn.close()
            else:
                insert_data = [Id, name, addher, date, amount,remark]
                conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
                cur = conn.cursor()
                cur.execute(  "Insert into transaction_detail (Id,name,addher_no,date, amount,remark) values(%s,%s,%s,%s,%s,%s)",insert_data)
                cur.close()
                conn.commit()
                conn.close()
    # transaction_saving()
