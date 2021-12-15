from datetime import datetime

import mysql.connector
import  os
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')

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


def loaddata():
        conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        query = "SELECT * FROM memberinfo"
        cur.execute(query)
        record = cur.fetchall()

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
        print("if stament")
        return lone_no
    else:
        return (lone_no[-1]) + 1

    # strlone = str(lone_no)
    # # return strlone
    # print(strlone)
    # print(type(strlone))
def trancationNumber():
    conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    query = "select trancation_no from lone_collection"
    cur.execute(query)
    i = 0
    data = cur.fetchall()
    data.sort()
    for i in data:
        i
    trancation_no = i
    lone_no2 = 1
    if trancation_no == 0:
        lone_no = 1
        print("if stament")
        return trancation_no
    else:
        return (trancation_no[-1]) + 1

def getdatalone():
    conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    query = "select lone_no from lone"
    cur.execute(query)
    i = 0
    data = cur.fetchall()
    data.sort()
    for i in data:
        i

def getdatalone(lone_no,name,addher,amount,totalAmounttopay,totalIntersetpay,totalintersetamount):
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    print(lone_no)
    getdatalonevalue1 = (lone_no,name,addher,amount,totalAmounttopay,totalIntersetpay,totalintersetamount)
    cur.execute("""INSERT INTO lone_info (Lone_no,Name,AddherNo,Lone_take,total_ammount_to_pay,Total_interest_pay,Total_interest_amount) VALUES(%s,%s,%s,%s,%s,%s,%s)""",getdatalonevalue1)
    cur.close()
    conn.commit()
    conn.close()

def lonecollection(collectiodata):
    date =datetime.strptime(collectiodata,'%Y/%m/%d')#%m/%d/%Y
    print("the date is ",date)

# lonecollection('1/1/2000')

def calrow():
    conn = mysql.connector.connect(host="localhost", user="root", password="1900340220", database="green")
    cur = conn.cursor()
    query = """SELECT * from lone_info"""
    cur.execute(query)
    i = 0
    record = cur.fetchall()
    for row in record:
        i = i + 1

    cur.close()
    conn.close()
    print(i)
    return i

calrow()

