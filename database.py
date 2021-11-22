import mysql.connector

def rowcount():
    conn = mysql.connector.connect(host="localhost", user="root", password="1900340220", database="green")
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
    conn = mysql.connector.connect(host="localhost", user="root", password="1900340220", database="green")
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
        conn = conn = mysql.connector.connect(host="localhost", user="root", password="1900340220", database="green")
        cur = conn.cursor()
        query = "SELECT * FROM memberinfo"
        cur.execute(query)
        record = cur.fetchall()

def lastlonen():
    conn = conn = mysql.connector.connect(host="localhost", user="root", password="1900340220", database="green")
    cur = conn.cursor()
    query = "select lone_no from lone"
    cur.execute(query)
    i = 0
    data = cur.fetchall()
    print("Type of data",type(data))
    data.sort()
    for i  in data:
        i
    lone_no = i[-1]
    return lone_no + 1
    # strlone = str(lone_no)
    # return strlone
    # print(strlone)
    # print(type(strlone))
lastlonen()




