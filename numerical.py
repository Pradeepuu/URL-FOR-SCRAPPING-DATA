import csv
import mysql.connector
from fractions import Fraction

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3307",
    password="",
    database="data_filter"
)
mycursor = mydb.cursor()

def fractionByvalue():

    sql1 = "SELECT * from DATA   "
    mycursor.execute(sql1)
    l = mycursor.fetchall()
    for x in l:
            value = x[7]
            Datatype = x[3]
            attribute = x[6]
            value1=x[9]
            inc = "Inch"
            rp = "rp_"
            mm = "mm"
            id = x[0]
            Deg=""

            if  '"' in value1 and 'to' not in value1 and '-' not in value1 and '(' not in value1 and 'OD' not in value1 and "ID" not in value1 and 'Numerical'  in Datatype :
                print(value1)
                if '/' in value1 and ' ' not in value1:
                    a = value1.strip('rp_').strip('RP_')
                    b = a.strip('"')
                    a2 = float(Fraction(b))
                    rs = round(a2, 3)
                    rs1 = "rp_" + str(rs)
                    val = (rs1, inc, id)
                    sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                    mycursor.execute(sql1, val)

                elif '/' in value1 and ' ' in value1:
                    a = value1.strip('rp_').strip('RP_')
                    b = a.strip('"')
                    c = b.split(' ')[1]
                    d = float(b.split(' ')[0])
                    # print(d)
                    a2 = float(Fraction(c))
                    a3 = d + a2
                    rs = round(a3, 3)

                    rs1 = "rp_" + str(rs)
                    # print(rs1)
                    print(id)
                    val = (rs1, inc, id)
                    sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                    mycursor.execute(sql1, val)
                else:
                    a = value1.strip('rp_').strip('RP_')
                    rs = a.strip('"')
                    rs1 = "rp_" + str(rs)
                    val = (rs1, inc, id)
                    sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                    mycursor.execute(sql1, val)


            if '/' and 'mm' in value1 and 'to' not in value1 and '-' not in value1 and '(' not in value1 and 'OD' not in value1 and "ID" not in value1 and 'Numerical'  in Datatype :
                if ' mm' in value1:
                    f = value1.split(' mm', 1)[0]
                    print(value1)
                    i = round(eval(f.replace("rp_", '').replace(" ", '+')), 3)
                    p = rp + str(i)
                    print(p)
                    val = (p, mm, id)
                    sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                    mycursor.execute(sql1, val)
                    print("mm : ", value1)

    mydb.commit()


def sortingvalue():
    sql1 = "SELECT * from DATA   "
    mycursor.execute(sql1)
    l = mycursor.fetchall()
    for x in l:
        value = x[7]
        Datatype = x[3]
        attribute = x[6]
        value1 = x[9]
        inc = "Inch"
        rp = "rp_"
        mm = "mm"
        id = x[0]
        Deg = ""
        if 'Discrete' not in Datatype and 'VarChar' not in Datatype and '(' not in value1 and 'OD' not in value1 and "ID" not in value1:
            if ' Deg.' in value1 and 'Range 1' not in Datatype and ' Deg.F' not in value1:
                print(value1)
                dg = value1.replace(' Deg.F', '')
                print(dg)
                Deg = "Deg."
                val = (dg, Deg, id)
                sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                mycursor.execute(sql1, val)


            if ' Deg.F' in value1 and 'Range 1' not in Datatype:
                print(value1)
                dg = value1.replace(' Deg.', '')
                print(dg)
                Deg = "Deg."
                val = (dg, Deg, id)
                sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                mycursor.execute(sql1, val)
            if ' lbs.' in value1 and 'Numerical' in Datatype:
                lb = value1.replace(' lbs.', '')
                lbs = "lbs."
                val = (lb, lbs, id)
                sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                mycursor.execute(sql1, val)

            elif 'rp_M' in value1 and ',' not in value1:
                j = value1.replace('M', '')
                p = 'M'
                print(j, "fasdfds")
                val = (p, j, mm, id)
                sql1 = "Update DATA set PreP=%s,value1=%s,unit1=%s where id = %s"
                mycursor.execute(sql1, val)
            elif 'rp_No.' in value1 and ',' not in value1 and 'Numerical' in Datatype:
                i = value1.replace("No. ", '')
                print('no:', i)
                p = "No."
                val = (p, i, id)
                sql1 = "Update DATA set PreP=%s,value1=%s where id = %s"
                mycursor.execute(sql1, val)

            elif "ga" in value1 and 'Numerical' in Datatype:
                g = value1.replace("ga.", '')
                ga = "ga."
                val = (g, ga, id)
                sql = "UPDATE DATA SET value1=%s,unit1=%s WHERE id=%s"
                mycursor.execute(sql, val)
            elif "psi" in value1 or '' in value1 and 'Numerical' in Datatype:
                if "psi" in value1:
                    e = value1.split(" ")
                    val = (e[0], e[1], id)
                    sql = "UPDATE DATA SET value1=%s,unit1=%s WHERE id=%s"
                    mycursor.execute(sql, val)
                else:
                    val = (value1, id)
                    sql = "UPDATE DATA SET value1=%s WHERE id=%s"
                    mycursor.execute(sql, val)
            if 'min.' in value1 and 'Range 1' not in Datatype and 'Numerical' in Datatype:
                print(value1)
                mi1 = value1.replace('min.', '')
                min = "min."
                val = (mi1, min, id)
                sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                mycursor.execute(sql1, val)
            if 'hrs.' in value1 and 'Range 1' not in Datatype and 'Numerical' in Datatype:
                print(value1)
                hr1 = value1.replace('hrs.', '')
                print(hr1)
                hrs = "hrs."
                val = (hr1, hrs, id)
                sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                mycursor.execute(sql1, val)
    mydb.commit()

def copy():
    sql1 = "SELECT * from DATA   "
    mycursor.execute(sql1)
    l = mycursor.fetchall()
    for x in l:
        value = x[7]
        id = x[0]
        val=(value,id)
        sql1 = "Update DATA set value1=%s where id = %s"
        mycursor.execute(sql1, val)

    mydb.commit()

def Range2():
    sql1 = "SELECT * from DATA  "
    mycursor.execute(sql1)
    l = mycursor.fetchall()
    for x in l:

        v = x[7]
        c = x[3]
        th = x[6]
        v1 = x[9]
        inc = "Inch"
        rp = "rp_"
        mm = "mm"
        id = x[0]
        mpn = x[1]
        type = x[5]



        if 'Range 2' in c and ',' in v or 'Thread Size' in th :
            d3 = v.replace(" ,", ',')
            s = d3.split(", ")
            n=th.split(' ')[0]
            print(s)
            k = s[0]
            A = n+'Dia.'
            B = n+'Per Inch'
            D = n+'Pitch'
            for i in s:
                if i == k:
                    key = 1
                    if "-" in i:
                        di = k.split('-')
                        print(di)
                        if '"' in i:
                            j = round(eval(di[0].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (x[8], A, v, p, inc, key, id)
                            print(p)
                            sql1 = "Update DATA set  SuperAtt=%s,ATTRIBUTE=%s,VALUE=%s,value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)
                            j = round(eval(di[1].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val1 = (c, th, B, v, p, inc, key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType, SuperAtt,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val1)
                        if 'mm' in i:
                            j = round(eval(di[0].replace('mm', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (x[8], A, v, p, mm, key, id)
                            print(p)
                            sql1 = "Update DATA set  SuperAtt=%s,ATTRIBUTE=%s,VALUE=%s,value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)
                            # i = round(eval(di[1].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            # p = rp + str(i)
                            # val1 = (c, th, A, i, p, mm, key, mpn)
                            # sql1 = "INSERT INTO DATA (DataType, SuperAtt,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn) values(%s,%s,%s,%s,%s,%s,%s,%s) "
                            # mycursor.execute(sql1, val1)
                        elif 'M' in i:
                            j = di[0].split('x')
                            p = j[0].replace('M', '')
                            M = "M"

                            val = (th, A, v, M, p, mm, key, id)
                            print(p)
                            sql1 = "Update DATA set  SuperAtt=%s,ATTRIBUTE=%s,VALUE=%s,PreP=%s,value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)
                            l = round(eval(di[1].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(l)
                            val1 = (c, th, M, D, v, p, mm, key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType, SuperAtt,PreP,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val1)
                        elif '#' in i:
                            ne = di[0].replace('#', '')
                            p = ne
                            M = '#'
                            val = (th, A, v, M, p, key, id)
                            print(p)
                            sql1 = "Update DATA set  SuperAtt=%s,ATTRIBUTE=%s,VALUE=%s,PreP=%s,value1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)
                            j = round(eval(di[1].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)

                            val1 = (c, th, D, v, p, key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType, SuperAtt,ATTRIBUTE,VALUE,value1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val1)



                    elif '-' not in i:
                        di = k.split('-')
                        if '"' in i:
                            j = round(eval(di[0].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (p, inc, key, id)
                            print(p)
                            sql1 = "Update DATA set  value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)
                        if 'mm' in i:
                            print(i)
                            i1 = i.replace(' mm', '')
                            j = round(eval(i1.replace('mm', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (p, mm, key, id)
                            print(p)
                            sql1 = "Update DATA set  value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)
                        elif 'M' in i:
                            j = di[0].split('x')
                            p = j[0].replace('M', '')
                            M = "M"

                            val = (M, p, mm, key, id)
                            print(p)
                            sql1 = "Update DATA set  PreP=%s,value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)
                            l = round(eval(j[1].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(l)
                            val1 = (c, th, M, D, v, p, mm, key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType, SuperAtt,PreP,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            mycursor.execute(sql1, val1)
                        elif 'No.' in i:
                            j = round(eval(di[0].replace('No.', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            no = 'No.'
                            val = (v, p, no, key, id)
                            print(p)
                            sql1 = "Update DATA set  VALUE=%s,value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)
                            # i = round(eval(di[1].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            # p = rp + str(i)
                            # val1 = (c, th, A, i, p, mm, key, mpn)
                            # sql1 = "INSERT INTO DATA (DataType, SuperAtt,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn) values(%s,%s,%s,%s,%s,%s,%s,%s) "
                            # mycursor.execute(sql1, val1)



                else:
                    key = key + 1
                    print(s)
                    A = 'Thread Dia.'
                    B = 'Thread Per Inch'
                    D = 'Thread Pitch'

                    di = i.split('-')
                    print(di)
                    if '-' in i or 'x' in i:
                        if '"' in i:
                            j = round(eval(di[0].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            print(p)
                            print(s)
                            val = (c, th, A, v, p, inc, key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType, SuperAtt,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)
                            j = round(eval(di[1].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (c, th, B, v, p,  key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType, SuperAtt,ATTRIBUTE,VALUE,value1, keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)
                        if 'mm' in i:
                            j = round(eval(di[0].replace('mm', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (c, th, A, v, p, mm, key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType, SuperAtt,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)
                        #     i = round(eval(di[1].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                        #     p = rp + str(i)
                        #     val = (c, th, A, s, p, mm, key, mpn)
                        #     sql1 = "INSERT INTO DATA (DataType, SuperAtt,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn) values(%s,%s,%s,%s,%s,%s,%s,%s) "
                        #     mycursor.execute(sql1, val)
                        elif 'M' in i:
                            print(i)
                            j = di[0].split('x')
                            print("Here :", j)
                            p = rp + j[0].replace('M', '')
                            M = "M"

                            val = (c, th, M, A, v, p, mm, key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType, SuperAtt,PreP,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)
                            l = round(eval(j[1].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(l)
                            val1 = (c, th, M, D, v, p, mm, key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType, SuperAtt,PreP,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val1)

                        elif '#' in i:
                            ne = di[0].replace('#', '')
                            p = rp + ne
                            M = '#'
                            val = (M,c, th, A, v, p, key, mpn, type)
                            sql1 = "INSERT INTO DATA (PreP,DataType, SuperAtt,ATTRIBUTE,VALUE,value1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)
                            i = round(eval(di[1].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(i)

                            val1 = (c, th, B, v, p, key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType, SuperAtt,ATTRIBUTE,VALUE,value1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val1)

                    elif '-' not in i:
                        if '"' in i:
                            j = round(eval(di[0].replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            print(p)
                            print(s)
                            val = (c, th, v, p, inc, key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)
                        if 'mm' in i:
                            j = round(eval(i.replace('mm', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            print(p)
                            print(s)
                            val = (c, th, v, p, mm, key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)
                        elif 'M' in i:
                            print(i)
                            j = di[0].split('x')
                            print("Here :", j)
                            p = rp + j[0].replace('M', '')
                            M = "M"

                            val = (c, M, th, v, p, mm, key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType,PreP,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)

                        elif 'No.' in i:
                            j = round(eval(di[0].replace('No.', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            no = 'No.'
                            val = (c, th, v, p, no, key, mpn, type)
                            sql1 = "INSERT INTO DATA (DataType,ATTRIBUTE,VALUE,value1, unit1,keyvalue,mpn,Type) values(%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)

    mydb.commit()



def thread():
    sql1 = "SELECT * from DATA"
    mycursor.execute(sql1)
    l = mycursor.fetchall()
    for x in l:
        value = x[7]
        Datatype = x[3]
        attribute = x[6]
        value1=x[9]
        inc = "Inch"
        rp = "rp_"
        mm = "mm"
        id = x[0]
        Deg=""
        if "Numerical" in Datatype or 'Range 2' in Datatype and ',' not in value1:

            if 'Thread Per Inch' in attribute or 'Thread Dia.' in attribute or "Threads Per Inch" in attribute:
                    if "Thread Dia." in attribute:
                        di = value1.split("-")
                        if '"' in value1 or "/" in value1:
                            p = di[0]
                            val = (p, id)
                            sql1 = "Update DATA set value1=%s  where id = %s"
                            mycursor.execute(sql1, val)
                        elif 'M' in value1:
                            print("afsdddddddddddD",value1)
                            Me = value1.split('x')
                            p = Me[0].replace('M', '')
                            M = "M"
                            val = (M, p, mm, id)
                            sql1 = "Update DATA set Prep=%s,value1=%s,unit1=%s where id = %s"
                            mycursor.execute(sql1, val)

                        elif '#' in value1:
                            he = value1.split('-')
                            ne = he[0].replace('#', '')
                            h = "#"
                            val = (h, ne, id)
                            sql1 = "Update DATA set PreP=%s,value1=%s where id = %s"
                            mycursor.execute(sql1, val)
                        else:
                            he = value1.split('-')
                            ne = he[0].replace('#', '')
                            val = (ne, id)
                            sql1 = "Update DATA set value1=%s where id = %s"
                            mycursor.execute(sql1, val)

                    if "Thread Per Inch" in attribute or "Threads Per Inch" in attribute:
                        di = value1.split("-")
                        if '"' in value1 or "/" in value1:
                            i = di[1]
                            p = rp + str(i)
                            val = (p,id)
                            sql1 = "Update DATA set value1=%s  where id = %s"
                            mycursor.execute(sql1, val)
                        elif 'M' in value1:
                            me = value1.split('x')
                            p = rp + me[1].replace('M', '')
                            val = (p, id)
                            sql1 = "Update DATA set value1=%s where id = %s"
                            mycursor.execute(sql1, val)

                        elif '#' in value1:
                            print(value1)
                            ne = rp + di[1].replace('#', '')
                            val = (ne, id)
                            sql1 = "Update DATA set value1=%s where id = %s"
                            mycursor.execute(sql1, val)
                        else:
                            print(value1)
                            he = value1.split('-')
                            n = rp + he[1]
                            val = (n, id)
                            sql1 = "Update DATA set value1=%s where id = %s"
                            mycursor.execute(sql1, val)

            if 'Thread Length' in attribute or 'Thread Pitch' in attribute:
                    if "Thread Length" in attribute:
                        di = value1.split("-")

                        if '"' in value1 or "/" in value1 and "mm" not in value1:
                            f = value1.split('"', 1)[0]
                            i = round(eval(f.replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(i)
                            print(p)
                            val = (p, inc, id)
                            sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                            mycursor.execute(sql1, val)
                        elif '/' in value1 or ' ' in value1 or 'mm' in value1:
                            f = value1.split('mm', 1)[0]
                            f = value1.split(' mm', 1)[0]
                            i = round(eval(f.replace("rp_", '').replace(" ", '+').replace("mm", '')), 3)
                            p = rp + str(i)
                            val = (p, mm, id)
                            sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                            mycursor.execute(sql1, val)



                    elif 'Thread Pitch' in attribute:
                        if '#' in value1:
                            i = value1.split('-')
                            ne = rp + i[1].replace('#', '')
                            val = (ne, id)
                            sql1 = "Update DATA set value1=%s where id = %s"
                            mycursor.execute(sql1, val)
                        elif 'M' in value1:
                            i = value1.split('x')
                            print("FASDdddddddd",p)
                            p = rp + i[1]
                            val = ( p, id)
                            sql1 = "Update DATA set value1=%s where id = %s"
                            mycursor.execute(sql1, val)
    mydb.commit()


def range1():
    sql1 = "SELECT * from DATA   "
    mycursor.execute(sql1)
    l = mycursor.fetchall()
    for x in l:
        value = x[7]
        Datatype = x[3]
        attribute = x[6]
        value1 = x[9]
        inc = "Inch"
        rp = "rp_"
        mm = "mm"
        id = x[0]
        Deg = ""
        # print(Datatype)
        datatype = Datatype.lower()
        print(datatype)
        if 'Range 1' in Datatype or 'Range1' in Datatype:
            if "Fits Hole Dia. (Min.-Max.)" in Datatype:
                if '"' in value1:
                    if '-' in value1:
                        b = value1.split('-')
                        print(b)
                        print(i)
                        d = b[1].replace('"', '')
                        # print(d)
                        e = d
                        s = '-'
                        val = (s, e, inc, id)
                        sql = "UPDATE DATA SET PreP=%s ,value1=%s, unit1=%s WHERE id=%s"
                        mycursor.execute(sql, val)

                        # print(i)
                        d = b[0].replace('"', '')
                        # print(d)
                        e = d
                        print(e)
                        print("sd")
                        s = '+'
                        val = (s, e, inc, id)
                        sql = "UPDATE DATA SET PostP=%s ,value2=%s ,unit2=%s WHERE id=%s"
                        mycursor.execute(sql, val)
                    else:

                        b = value1.replace('"', '')
                        # print(d)
                        e = b
                        val = (e, inc, id)
                        sql = "UPDATE DATA SET value1=%s, unit1=%s WHERE id=%s"
                        mycursor.execute(sql, val)
                # if 'mm' in value1:
                #     if '-' in value1:
                #         b = value1.split('-')
                #         print(b)
                #         print(i)
                #         d = b[1].replace('"', '')
                #         # print(d)
                #         e = d
                #         s = '-'
                #         val = (s, e, mm, id)
                #         sql = "UPDATE DATA SET PreP=%s ,value1=%s, unit1=%s WHERE id=%s"
                #         mycursor.execute(sql, val)
                #
                #         # prin(i)
                #         d = b[0].replace('"', '')
                #         # print(d)
                #         e = d
                #         print(e)
                #         print("sd")
                #         s = '+'
                #         val = (e, mm, id)
                #         sql = "UPDATE DATA SET value2=%s ,unit2=%s WHERE id=%s"
                #         mycursor.execute(sql, val)
                #     else:
                #         b = value1.replace('mm', '')
                #         # print(d)
                #         e = b
                #         val = (e, mm, id)
                #         sql = "UPDATE DATA SET value1=%s, unit1=%s WHERE id=%s"
                #         mycursor.execute(sql, val)
            if 'Deg. F' in value1:
                dt = value1.split("to")
                # print(r[0])
                # print(r[1])
                # print(v,":",n)
                # print(r)
                for i in dt:

                    if i == dt[0]:
                        if '-' in i:
                            print(i)
                            d = dt[0].replace('-', '').replace('Deg. F', '').replace('Deg.', '')
                            Deg = 'Deg. F'
                            si = '-'
                            val = (si, d, Deg, id)
                            sql = "UPDATE DATA SET PreP=%s,value1=%s,unit1=%s WHERE id=%s"
                            mycursor.execute(sql, val)
                        else:
                            if "rp_Not Rated" in value1:
                                j = "rp_0"
                                Deg = 'Deg. F'
                                si = '+'
                                val = (si, j, Deg, id)
                                sql = "UPDATE DATA SET PreP=%s,value1=%s,unit1=%s WHERE id=%s"
                                mycursor.execute(sql, val)


                    elif i == dt[1]:
                        d = dt[1].replace('-', '').replace('Deg. F', '').replace('Deg.', '')

                        e = rp + d.replace('-', '')
                        Deg = 'Deg.F'
                        si = "+"
                        val = (si, e, Deg, id)
                        sql = "UPDATE DATA SET PostP=%s,value2=%s,unit2=%s WHERE id=%s"
                        mycursor.execute(sql, val)

            if '-' in value1 and "mm" in value1:

                b = value1.split('-')
                c = "rp_"
                # print(b)
                for i in b:
                    if i == b[0]:
                        j = b[0].replace('mm', '')
                        print(j)
                        m = 'mm'
                        val = (j, m, id)
                        sql = "UPDATE DATA SET value1=%s,unit1=%s WHERE id=%s"
                        mycursor.execute(sql, val)

                    elif i == b[1]:
                        j = b[1].replace('mm', '')
                        print(j)
                        e = c + j
                        print(e)
                        m = 'mm'
                        val = (e, m, id)
                        sql = "UPDATE DATA SET value2=%s,unit2=%s WHERE id=%s"
                        mycursor.execute(sql, val)

            if '-' in value1 and '"' in value1:
                a = value1.strip('"')
                b = a.split('-')
                c = "rp_"
                print(value1)
                for i in b:
                    if i == b[0]:
                        j = b[0].strip('"')
                        print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeejjjjjjjjjjjj", j)
                        e = round(eval(j.replace(" ", '+').replace("rp_", '').replace('"', '')), 3)
                        print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeee", e)
                        val = (str(e), inc, id)
                        exit()
                        sql = "UPDATE DATA SET value1=%s,unit1=%s WHERE id=%s"
                        mycursor.execute(sql, val)

                    elif i == b[1]:
                        j = b[1].replace('"', '')
                        e = round(eval(j.replace(" ", '+').replace("rp_", '').replace('"', '')), 3)
                        e1 = c + str(e)
                        print(e)

                        val = (e1, inc, id)
                        sql = "UPDATE DATA SET value2=%s,unit2=%s WHERE id=%s"
                        mycursor.execute(sql, val)

            if 'to' in value1 and '"' in value1:
                # n = v.replace('"', '').replace('rp_', '').replace(" to",'')
                r = value1.split("to")
                print(r[0])
                print(r[1])
                # print(v,":",n)
                # print(r)
                if '-' in r[0] and '-' in r[1]:
                    M = float(r[0])
                    L = float(r[1])
                    if M < L:
                        d = r[1].replace("-", '').replace('"', '')
                        # print(d)
                        e = rp + d
                        s = '-'
                        val = (s, e, inc, id)
                        sql = "UPDATE DATA SET PostP=%s ,value2=%s,unit2=%sWHERE id=%s"

                        mycursor.execute(sql, val)
                        print(rp + r[1])
                        u = r[0].replace("-", '').replace('"', '')
                        e2 = rp + u
                        val = (s, e2, inc, id)
                        sql = "UPDATE DATA SET PreP=%s ,value1=%s,unit1=%sWHERE id=%s"
                        mycursor.execute(sql, val)

                elif '-' not in value1 and 'to' in value1:
                    print("Sfdsa", value1)
                    if "Tolerance" in attribute:
                        for i in r:
                            if i == r[0]:
                                hj = r[0].split('"', 1)[0]
                                i = round(eval(hj.replace(" ", '+').replace("rp_", '').replace('"', '')), 3)
                                e2 = rp + str(i)
                                s = "+"
                                val = (s, e2, inc, id)
                                sql = "UPDATE DATA SET PreP=%s,value1=%s,unit1=%sWHERE id=%s"
                                mycursor.execute(sql, val)
                            else:
                                hj = r[1].split('"', 1)[0]
                                i = round(eval(hj.replace(" ", '+').replace("rp_", '').replace('"', '')), 3)
                                e3 = rp + str(i)
                                s = "+"
                                val = (s, e3, inc, id)
                                sql = "UPDATE DATA SET PostP=%s,value2=%s,unit2=%sWHERE id=%s"
                                mycursor.execute(sql, val)
                    else:
                        print("Sfdsa222", value1)
                        for i in r:
                            print("ss")
                            if i == r[0]:
                                hj = r[0].split('"', 1)[0]
                                i = round(eval(hj.replace(" ", '+').replace("rp_", '').replace('"', '')), 3)
                                e2 = rp + str(i)

                                val = (e2, inc, id)
                                sql = "UPDATE DATA SET value1=%s,unit1=%sWHERE id=%s"
                                mycursor.execute(sql, val)
                            else:
                                hj = r[1].split('"', 1)[0]
                                i = round(eval(hj.replace(" ", '+').replace("rp_", '').replace('"', '')), 3)
                                e3 = rp + str(i)

                                val = (e3, inc, id)
                                sql = "UPDATE DATA SET value2=%s,unit2=%s WHERE id=%s"
                                mycursor.execute(sql, val)
                else:
                    n = value1.replace('"', '').replace('rp_', '')
                    r = n.split("to")
                    for i in r:
                        print("asfdsd")
                        if '-' in i:
                            print(i)
                            d = i.replace("-", '').replace('"', '')
                            # print(d)
                            e = rp + d
                            s = '-'
                            val = (s, e, inc, id)
                            sql = "UPDATE DATA SET PreP=%s ,value1=%s, unit1=%s WHERE id=%s"
                            mycursor.execute(sql, val)
                        elif i != '':
                            # print(i)
                            e = rp + i
                            print(e)
                            print("sd")
                            s = '+'
                            val = (s, e, inc, id)
                            sql = "UPDATE DATA SET PostP=%s ,value2=%s ,unit2=%s WHERE id=%s"
                            mycursor.execute(sql, val)
            elif 'to' in value1 and 'mm' in value1 and '-' not in value1:
                n = value1.replace('mm', '').replace('rp_', '')
                r = n.split("to")
                # print(v,":",n)
                # print(r)
                if '-' in r[0] and '-' in r[1]:
                    M = float(r[0])
                    L = float(r[1])
                    if M < L:
                        d = r[1].replace("-", '')
                        # print(d)
                        e = rp + d
                        s = '-'
                        val = (s, e, mm, id)
                        sql = "UPDATE DATA SET PostP=%s ,value2=%s,unit2=%sWHERE id=%s"

                        mycursor.execute(sql, val)
                        print(rp + r[1])
                        u = r[0].replace("-", '')
                        e2 = rp + u
                        val = (s, e2, mm, id)
                        sql = "UPDATE DATA SET PreP=%s ,value1=%s,unit1=%sWHERE id=%s"
                        mycursor.execute(sql, val)
                elif '-' not in r[0] and '-' not in r[1]:
                    M = float(r[0])
                    L = float(r[1])
                    if M < L:
                        d = r[1].replace("-", '')
                        # print(d)
                        e = rp + d
                        s = ''
                        val = (s, e, mm, id)
                        sql = "UPDATE DATA SET PostP=%s ,value2=%s,unit2=%sWHERE id=%s"

                        mycursor.execute(sql, val)
                        print(rp + r[1])
                        u = r[0].replace("+", '')
                        e2 = rp + u
                        s = ''
                        val = (s, e2, mm, id)
                        sql = "UPDATE DATA SET PreP=%s ,value1=%s,unit1=%sWHERE id=%s"
                        mycursor.execute(sql, val)


                else:
                    n = value1.replace('rp_', '')
                    r = n.split('to')

                    for i in r:
                        if '-' in i:
                            d = i.replace("-", '').replace('mm', '')
                            # print(d)
                            e = rp + d
                            s = '-'
                            val = (s, e, mm, id)
                            sql = "UPDATE DATA SET PreP=%s ,value1=%s, unit1=%s WHERE id=%s"
                            mycursor.execute(sql, val)
                        elif i != '':
                            # print(i)
                            e = rp + i
                            print(e)
                            print("sd")
                            s = '+'
                            val = (s, e, mm, id)
                            sql = "UPDATE DATA SET PostP=%s ,value2=%s ,unit2=%s WHERE id=%s"
                            mycursor.execute(sql, val)

            if ',' not in value1 and 'to' not in value1 and '-' not in value1:
                s = value1.replace("rp_", '')
                if '"' in value1 or '/' in value1:
                    if '/' not in value1 and '(' not in value1:
                        print(s)
                        s1 = s.replace('"', '').replace(' ', '')
                        print(s1)
                        s2 = rp + str(s1)
                        val = (s2, inc, id)
                        sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                        mycursor.execute(sql1, val)
                    if '/' in value1 and '(' not in value1:
                        print(s)
                        s1 = round(eval(s.replace('"', '').replace(' ', '')), 3)
                        print(s1)
                        s2 = rp + str(s1)
                        val = (s2, inc, id)
                        sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                        mycursor.execute(sql1, val)
                if 'mm' in value1 or '/' in value1:
                    if '/' not in value1 and '(' not in value1:
                        print(s)
                        s1 = s.replace('mm', '').replace(' ', '')
                        s2 = rp + str(s1)
                        val = (s2, mm, id)
                        sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                        mycursor.execute(sql1, val)
                    if '/' in value1 and '(' not in value1:
                        print(s)
                        s1 = round(eval(s.replace('"', '').replace(' ', '')), 3)
                        s2 = rp + str(s1)
                        val = (s2, mm, id)
                        sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                        mycursor.execute(sql1, val)

    mydb.commit()