from calendar import month
from distutils.log import info
from tkinter import Canvas, font
from turtle import color
from unicodedata import name
from numpy import full
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle

from reportlab.lib import colors
from reportlab.lib.colors import Color

from reportlab.lib.pagesizes import A4
from Print import importdata
from reportlab.lib.styles import getSampleStyleSheet
import mysql.connector
import os
from datetime import datetime, timedelta
from datetime import date
from dateutil.relativedelta import relativedelta

# ! *********************************************************************************************************************************
# global prolone_no
# global proIntrest
# global protoday
# proIntrest = 2
# prolone_no = 87
# protoday = datetime(2022, 8, 24)
# def dataforProcess(prolone_no,proIntrest,protoday):
#     prolone_no = prolone_no
#     proIntrest = proIntrest
#     protoday = protoday
def gInvoice(prolone_no,proIntrest,protoday):
    global out1
    out1 = importdata.importdatalone(prolone_no,proIntrest)
    proloneno1 = prolone_no

    makepdf(out1,protoday,proIntrest,prolone_no,proloneno1)
    # ! *********************************************************************************************************************************
def makepdf(out1,protoday,proIntrest,prolone_no,proloneno1):
    prolone_no,approvedate, proIntrest = importdata.approvedate(proloneno1)

    out,approvedate,protoday = importdata.getdata(prolone_no, approvedate, proIntrest,protoday)

    monthlist,monthis,diff = importdata.get_forward_month_list(approvedate,protoday)
        # amountval(monthis, diff)
    amount,month_num = importdata.amountval(monthis,diff+1)
    intrestlist = importdata.intrestrate(month_num, diff)

    data = []
    data1 = []
    headder = ["Month","Amount","Intrest"]
    for (a,b,c) in zip(monthlist,amount,intrestlist):
        data = [a,b,c]
        # print(data)
        data1.append(data)
        # data1.insert([0:1],headder)
    data1.insert(0,headder)

    # print(data1)

    tableData = data1



    # creating a Document structure with A4 size page

    docu = SimpleDocTemplate("C:/pdftemp/invoice.pdf", pagesize=A4)

    styles = getSampleStyleSheet()



    doc_style = styles["Heading1"]

    doc_style.alignment = 1
    basic_info = styles["Heading5"]
    basic_info.alignment = 0
    date = ("Date: "+str(out1[2]))
    prolone_no = ("Lone No: "+str(out1[0]))
    fullName = ('Name: '+str(out1[1]))
    lonetake = ("Lone Take: "+str(out1[3]))
    proIntrest = ("proIntrest: "+str(out1[4]))
    FullName = Paragraph(fullName,basic_info)
    LoneTake = Paragraph(lonetake,basic_info)
    proIntrest = Paragraph(proIntrest,basic_info)
    Date = Paragraph(date,basic_info)
    prolone_no = Paragraph(prolone_no,basic_info)
    importdata.approvedate(str(proloneno1))
    title = Paragraph("Green Thought Farmers", doc_style)
    # d.add(String(150,100, 'Hello World', fontSize=18, fillColor=colors.red))
    style = TableStyle(
    [ ("BOX", (0, 0), (-1, -1), 1, colors.black),

            ("GRID", (0, 0), (4, 15), 1, colors.chocolate),

            ("BACKGROUND", (0, 0), (3, 0), colors.skyblue),

            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),

            ("ALIGN", (0, 0), (-1, -1), "CENTER"),

            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
     ])
    # creates a table object using the Table() to pass the table data and the style object

    table = Table(tableData, style=style)

    # finally, we have to build the actual pdf merging all objects together

    docu.build([title,Date,prolone_no,FullName,LoneTake,proIntrest, table])


