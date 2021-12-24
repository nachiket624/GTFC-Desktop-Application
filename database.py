from datetime import datetime

import mysql.connector
import  os
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')

# return last number of member on Dashboard
def rowcount():
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    query = """SELECT * from memberinfo"""
    cur.execute(query)
    i = 0
    record = cur.fetchall()
    for row in record:
        i = i+1

    cur.close()
    conn.close()

    return i+1
# last lone count for Dashboard
def lonecount():
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    query = """SELECT * from lone"""
    cur.execute(query)
    i = 0
    record = cur.fetchall()
    for row in record:
        i = i+1

    cur.close()
    conn.close()
    return i


# return last lone lone number
def lastlonen():
    conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    query = "select lone_no from lone"
    cur.execute(query)
    i = 0
    data = cur.fetchall()
    data.sort()
    for i in data:
        i
    lone_no = i
    lone_no2 = 1
    if lone_no == 0:
        lone_no = 1
        return lone_no
    else:
        return (lone_no[-1]) + 1




# This function create add new lone detail into lone info table
def getdatalone(lone_no,name,addher,amount,interast,totalAmounttopay,totalIntersetpay,totalintersetamount):
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    print(lone_no)
    getdatalonevalue1 = (lone_no,name,addher,amount,interast,totalAmounttopay,totalIntersetpay,totalintersetamount)
    cur.execute("""INSERT INTO lone_info (Lone_no,Name,AddherNo,Lone_take,Intrest,total_ammount_to_pay,Total_interest_pay,Total_interest_amount) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",getdatalonevalue1)
    cur.close()
    conn.commit()
    conn.close()
def count_transaction_detail():
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    query = "select transaction_no from transaction_detail"
    cur.execute((query))
    i = 0
    data = cur.fetchall()
    data.sort()
    for i in data:
        i
    transaction_no = i

    if transaction_no == 0:
        transaction_no = 1
        return transaction_no
    else:
        return (transaction_no[-1]) + 1
