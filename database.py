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
def getdatalone(lone_no,id,name,addher,last_transaction_date,amount,interast,totalAmounttopay,totalIntersetpay,totalintersetamount,total_interest_he_pay):
    print("the amount is getlone functrion is ",amount)
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    cur.execute("""SELECT count(*) from lone_info""")
    rowcountoftable = cur.fetchall()
    rowcountoftable = [a_tuple[0] for a_tuple in rowcountoftable]
    print("Row count is ", rowcountoftable[0])

    if rowcountoftable == 0:
        lone_no = 1
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        print(lone_no)
        getdatalonevalue1 = (lone_no,id,name,addher,last_transaction_date,amount,interast,totalAmounttopay,totalIntersetpay,totalintersetamount,total_interest_he_pay)
        cur.execute("""INSERT INTO lone_info (Lone_no,id,Name,AddherNo,last_transaction_date,Lone_take,Intrest,total_ammount_to_pay,Total_interest_pay,Total_interest_amount_pay,total_interest_he_pay) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",getdatalonevalue1)
        cur.close()
        conn.commit()
        conn.close()
    else:
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        print(lone_no)
        getdatalonevalue1 = (
        id, name, addher, last_transaction_date, amount, interast, totalAmounttopay, totalIntersetpay,
        totalintersetamount, total_interest_he_pay)
        cur.execute(
            """INSERT INTO lone_info (id,Name,AddherNo,last_transaction_date,Lone_take,Intrest,total_ammount_to_pay,Total_interest_pay,Total_interest_amount_pay,total_interest_he_pay) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            getdatalonevalue1)
        cur.close()
        conn.commit()
        conn.close()
def getdataloneupdate(lone_no,id,lastdate,new_transaction_date,amount,interast,totalAmounttopay,totalIntersetpay,totalintersetamount,total_interest_he_pay):
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    print(lone_no)
    totalAmounttopay = amount

    getdatalonevalue1 = (new_transaction_date,amount,interast,totalAmounttopay,totalIntersetpay,totalintersetamount,total_interest_he_pay)
    print("new lone date is ",new_transaction_date,", last date is ",lastdate)
    # print("""Update lone_info (last_transaction_date,Lone_take,Intrest,total_ammount_to_pay,Total_interest_pay,Total_interest_amount_pay,total_interest_he_pay) VALUES(%s,%s,%s,%s,%s,%s) Where id = """+str(id)+""" and last_transaction_date = '"""+str(lastdate)+"""'""",getdatalonevalue1)
    print("UPDATE lone_info SET last_transaction_date = '"+str(getdatalonevalue1[0])+"', Lone_take = "+str(getdatalonevalue1[1])+", Intrest = "+str(getdatalonevalue1[2])+", total_ammount_to_pay = "+str(getdatalonevalue1[3])+", Total_interest_pay = "+str(getdatalonevalue1[4])+", Total_interest_amount_pay = "+str(getdatalonevalue1[5])+", total_interest_he_pay = "+str(getdatalonevalue1[6])+" Where id = "+str(id)+" and last_transaction_date = '"+str(lastdate)+"'")
    cur.execute("UPDATE lone_info SET Lone_take = "+str(getdatalonevalue1[1])+", Intrest = "+str(getdatalonevalue1[2])+", total_ammount_to_pay = "+str(getdatalonevalue1[3])+", Total_interest_pay = "+str(getdatalonevalue1[4])+", Total_interest_amount_pay = "+str(getdatalonevalue1[5])+", total_interest_he_pay = "+str(getdatalonevalue1[6])+", last_transaction_date = '"+str(getdatalonevalue1[0])+"' Where id = "+str(id)+" and last_transaction_date = '"+str(lastdate)+"'")
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

def total_saving_count():
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    query = """select Sum(opning_balance) from memberinfo"""
    cur.execute(query)
    total_saving_count = (cur.fetchall()[0])
    return total_saving_count[0]

