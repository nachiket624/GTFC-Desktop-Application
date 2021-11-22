# ! ***************************** Manage  Update Member Function *****************************
def updatamember(self):
    self.stackedWidget.setCurrentWidget(self.UpdateInformation)
    self.search.clicked.connect(self.searchfun)


def searchfun(self):
    id = self.id_2.text()
    username = os.environ.get('db_user')
    userpass = os.environ.get('db_pass')
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    cur.execute("select * from memberinfo where id = " + id)
    for data in cur:
        data
    fname = data[1]
    mname = data[2]
    lname = data[3]
    bgroup = data[4]
    nomine = data[5]
    dob = data[6]
    doj = data[7]
    addherNo = data[8]
    account = data[9]
    mobile1 = data[10]
    mobile2 = data[11]
    email = data[12]
    opnningBalance = data[13]

    # ? @@@@@@@@@@@ setting value to line edit @@@@@@@@@@@
    self.firstname_2.setText(fname)
    self.middlename_2.setText(mname)
    self.lastname_2.setText(lname)
    self.bloodgroup_2.setCurrentText(bgroup)
    self.nomine_2.setText(nomine)
    self.dob_2.setDate(dob)
    self.doj_2.setDate(doj)
    self.addhernumber_2.setText(str(addherNo))
    self.accountno_2.setText(account)
    self.mobile1_2.setText(str(mobile1))
    self.mobile2_2.setText(str(mobile2))
    self.email_2.setText(email)
    self.balance_2.setText(str(opnningBalance))

    # ? @@@@@@@@@@@ Updataing value from line edit @@@@@@@@@@@