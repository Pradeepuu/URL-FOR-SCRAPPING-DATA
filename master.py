import csv
import mysql.connector
from numerical import fractionByvalue, sortingvalue, copy, Range2, thread, range1
from fractions import Fraction

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3307",
    password="",
    database="data_filter"
)
mycursor = mydb.cursor()
filename = "/home/pradeep/Desktop/Saumya L3s/csv/Shoulder Screws 17 Nov. SAUMYA.csv"
with open(filename, 'r', encoding='latin1') as f:
    df = csv.reader(f)
    for row in df:
        sql = "INSERT INTO DATA(MPN,L3,DataType,SuperAtt,Type,ATTRIBUTE,VALUE,PreP,value1,unit1,PostP,value2,unit2,keyvalue) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s,%s,%s,%s,%s,%s)"
        val = (
        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
        row[13])
        mycursor.execute(sql, val)
        print("done")
    mydb.commit()

# function to copy raw values data into value1
copy()
# function to filter attributes which having thread dia and thread Per inch,thread size
thread()
# function to filter range 1 values
range1()
# function to filter discrete and varchar values
sortingvalue()
# function to filter Range2 values
Range2()
# function to filter values that have / and fraction values
fractionByvalue()
