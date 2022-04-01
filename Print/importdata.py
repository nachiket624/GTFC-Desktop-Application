from datetime import datetime, timedelta
from datetime import date, timedelta
from calendar import monthrange
from dateutil.relativedelta import relativedelta
import dateutil
from glob import glob
from time import strftime
from dateutil.relativedelta import relativedelta
import mysql.connector
import os
import itertools

username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')

out = []

def importdatalone(lone_no,Intrest):
    username = os.environ.get('db_user')
    userpass = os.environ.get('db_pass')
    conn = mysql.connector.connect(
        host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    cur.execute("select Lone_no,Name,last_transaction_date,Lone_take,Intrest from lone_info where lone_no = "+str(lone_no))
    data = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    out = [item for t in data for item in t]
    return out

def approvedate(lone_no):
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    print("Lone No is ",lone_no)
    print("select lone_date,insrast_rate from lone where lone_no = ",str(lone_no))
    lone_no1 = str(lone_no)
    cur.execute("""select lone_date,insrast_rate from lone where lone_no = """+str(lone_no))
    approvedata = cur.fetchall()
    print('approve date is ',approvedata)
    cur.close()
    conn.commit()
    conn.close()
    appdate = [item for t in approvedata for item in t]
    # print(appdate)
    approvedate = appdate[0]
    Intrest = appdate[1]
    return lone_no, approvedate, Intrest


def getdata(Lone_no, approvedate, Intrest,today):
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    cur.execute("select * from lone_info where Lone_no = " + str(Lone_no) + " and Intrest = " + str(Intrest))
    data = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    global out
    out = [item for t in data for item in t]

    get_forward_month_list(approvedate, today)
    return out, approvedate, today


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


def get_forward_month_list(approvedate, today):
    global monthis
    diff = diff_month(today, approvedate)  # 3
    print("Differnece is ", diff)
    diff = diff + 1
    now = approvedate
    monthis = now.strftime("%m")
    months = ([(now + relativedelta(months=i)).strftime('%B') for i in range(diff)])
    print('months ', months)
    return months[1:diff + 1], monthis, diff
    # amountval(monthis, diff)


def amountval(monthis, diff):
    global month_num
    month_num = (int(monthis))
    monthdata = out[7:31]
    monthno = []
    indexval = 0
    for i in range(len(monthdata)):
        if indexval <= 23:
            sub_list = [(monthdata[indexval])]
            monthno.append(sub_list)
            indexval = indexval + 2
    mn = int(month_num)
    lenofm = (monthno[mn:12])
    lenofm2 = (monthno[0:mn])
    res_list1 = [*lenofm, *lenofm2]

    # diff = int(diff - 1)
    # monthno = [item for t in monthno for item in t]
    # lenofm = ((monthno[mn:diff]))
    # lenofm2 = (monthno[0:mn])
    res_list1 = [item for sublist in res_list1 for item in sublist]
    # print('res_list1: ',res_list1)

    return res_list1, month_num
    # intrestrate(month_num, diff)


def intrestrate(month_num, diff):
    monthdata = out[7:31]
    monthno = []
    monthno1 = []
    indexval = 0
    monthdata = out[7:31]
    monthno = []
    monthno1 = []
    indexval = 0
    for i in range(len(monthdata)):
        if indexval <= 24:
            if indexval == 0:
                sub_list1 = [(monthdata[indexval])]
                monthno1.append(sub_list1)
                indexval = indexval + 1
            else:
                sub_list = [(monthdata[indexval])]
                monthno.append(sub_list)
                indexval = indexval + 2
    mn = int(month_num)
    # lenofm = ((monthno[mn:diff+1]))
    lenofm = (monthno[mn:12])
    # print('lenofn: ',lenofm)
    lenofm2 = (monthno[0:mn])
    res_list2 = [*lenofm, *lenofm2]
    marged = [item for t in res_list2 for item in t]
    print("marged: ", marged)
    # merged = list(itertools.chain(*lenofm2))
    print('intrest rate ', res_list2)
    return (marged)

    # return (lenofm)

# l = listoflonedate(91)