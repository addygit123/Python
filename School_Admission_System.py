import mysql.connector as mcon
#from tabulate import tabulate
mydb = mcon.connect(database = "a",host = "localhost",password = "sql123",user ="root")
if mydb.is_connected() :
    print("Connectivity is ensured ")
def addstu():
    l =[]
    k = []
    
    n = str(input("Enter name of the student")) ; l.append(n)
    c = int(input("enter class of admission"));l.append(c)
    ln = str(input("Enter lastname of the student")) ; l.append(ln)
    guardian = str(input("enter name of parent"));l.append(guardian)
    pc = str(input("Enter previous class of the student"));l.append(pc)
    per = int(input("Previous Class Percentage Obtained"));l.append(per)
    if c in range(1,11):
        sec = str(input("sent to section ex.A,B,C,D")) ; k.append(sec)
    #ch = input("enter your choice")
    data = {"name" : n,"lastname" : ln,"class" :c,"guardian": guardian,"previousclass":pc,"percentage": per}
    if ((l[1] == 1) and (k[0] == "A" or "a" )):
        b = ("insert into class1" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] ==1) and (k[0] == "B" or "b" )):
        b = ("insert into class1B" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] ==1) and (k[0] == "C" or "c" )):
        b = ("insert into class1C" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] ==1) and (k[0] == "D" or "d" )):
        b = ("insert into class1D" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")

    elif ((l[1] == 2) and (k[0] == "A" or "a" )):
        b = ("insert into class2" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 2) and (k[0] == "B" or "b" )):
        b = ("insert into class2B" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 2) and (k[0] == "C" or "c" )):
        b = ("insert into class2C" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 2) and (k[0] == "D" or "d" )):
        b = ("insert into class2D" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    
    elif ((l[1] == 3) and (k[0] == "A" or "a" )):
        b = ("insert into class3" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 3) and (k[0] == "B" or "b" )):
        b = ("insert into class3B" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 3) and (k[0] == "C" or "c" )):
        b = ("insert into class3C" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 3) and (k[0] == "D" or "d" )):
        b = ("insert into class3D" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")


    elif ((l[1] == 4) and (k[0] == "A" or "a" )):
        b = ("insert into class4" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 5) and (k[0] == "A" or "a" )):
        b = ("insert into class5" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 6) and (k[0] == "A" or "a" )):
        b = ("insert into class6" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 7) and (k[0] == "A" or "a" )):
        b = ("insert into class7" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 8) and (k[0] == "A" or "a" )):
        b = ("insert into class8" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 9) and (k[0] == "A" or "a" )):
        b = ("insert into class9" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 10) and (k[0] == "A" or "a" )):
        b = ("insert into class10" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 4) and (k[0] == "B" or "a" )):
        b = ("insert into class4B" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 5) and (k[0] == "B" or "a" )):
        b = ("insert into class5B" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 6) and (k[0] == "B" or "a" )):
        b = ("insert into class6B" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 7) and (k[0] == "B" or "b" )):
        b = ("insert into class7B" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 8) and (k[0] == "B" or "b" )):
        b = ("insert into class8B" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 9) and (k[0] == "B" or "b" )):
        b = ("insert into class9B" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 10) and (k[0] == "B" or "b" )):
        b = ("insert into class10B" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 4) and (k[0] == "C" or "c" )):
        b = ("insert into class4C" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 5) and (k[0] == "C" or "c" )):
        b = ("insert into class5C" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 6) and (k[0] == "C" or "c" )):
        b = ("insert into class6C" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 7) and (k[0] == "C" or "c" )):
        b = ("insert into class7C" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 8) and (k[0] == "C" or "c" )):
        b = ("insert into class8C" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 9) and (k[0] == "C" or "c" )):
        b = ("insert into class9C" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 10) and (k[0] == "C" or "c" )):
        b = ("insert into class10C" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 4) and (k[0] == "D" or "d" )):
        b = ("insert into class4D" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 5) and (k[0] == "D" or "d" )):
        b = ("insert into class5D" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 6) and (k[0] == "D" or "d" )):
        b = ("insert into class6D" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 7) and (k[0] == "D" or "d" )):
        b = ("insert into class7D" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 8) and (k[0] == "D" or "d" )):
        b = ("insert into class8D" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 9) and (k[0] == "D" or "d" )):
        b = ("insert into class9D" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 10) and (k[0] == "D" or "d" )):
        b = ("insert into class10D" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 11) and (l[5] >= 76)):
        b = ("insert into class11a" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 12) and (l[5] >= 76)):
        b = ("insert into class12a" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 11) and (l[5] >=65 and l[5]<=75)):
        b = ("insert into class11b" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 12) and (l[5] >=65 and l[5]<=75)):
        b = ("insert into class12b" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 11) and (l[5] >=33 and l[5]<=65)):
        b = ("insert into class11c" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 12) and (l[5] >=33 and l[5]<=65)):
        b = ("insert into class12c" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 11) and (l[5] >=70 and l[5]<=75)):
        b = ("insert into class11d" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    elif ((l[1] == 12) and (l[5] >=70 and l[5]<=75)):
        b = ("insert into class12d" "(name,lastname,class,guardian,previousclass,percentage)" "VALUES (%(name)s,%(lastname)s,%(class)s,%(guardian)s,%(previousclass)s,%(percentage)s)")
    
    
     

    cursor = mydb.cursor()
    cursor.execute(b,data)
    mydb.commit()
    print("Data Entered Successfully")
    print("")
#addstu()
#c = cursor.fetchall()
#
#cursor.execute("select * from class1" )
#c1 = cursor.fetchall()
#
#cursor.execute("select * from class2" )
#b = cursor.fetchall()
#cla = int(input("enter"))
#if cla == 1:
#    print(c1)


#display classes
#def displayclass():
    #c = input("class:")
    #data = (c,)
    #sql = 'select * from cla;'
    #cursor = mydb.cursor()
    #cursor.execute(sql,data)
    #mydb.commit()
    #d = cursor.fetchall()
    #print(d)
#displayclass()
def display():
    classn = str(input("Class of which you want to display data :"+"ex. 1,2,3,  4etc"))
    if classn == "1A": 
       cur = mydb.cursor()
       cur.execute("select * from class1")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    
    if classn == "1B": 
        cur = mydb.cursor()
        cur.execute("select * from class1B")
        f = cur.fetchall()
        data = []
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
        for i in f:
         data.append(i)
         print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    
    if classn == "1C": 
        cur = mydb.cursor()
        cur.execute("select * from class1C")
        f = cur.fetchall()
        data = []
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
        for i in f:
         data.append(i)
         print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "1D": 
        cur = mydb.cursor()
        cur.execute("select * from class1D")
        f = cur.fetchall()
        data = []
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
        for i in f:
         data.append(i)
         print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    

    if classn == "2": 
       cur = mydb.cursor()
       cur.execute("select * from class2")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "2B": 
       cur = mydb.cursor()
       cur.execute("select * from class2B")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
   
    if classn == "2C": 
       cur = mydb.cursor()
       cur.execute("select * from class2C")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "2D": 
       cur = mydb.cursor()
       cur.execute("select * from class2D")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "3": 
       cur = mydb.cursor()
       cur.execute("select * from class3")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "3B": 
       cur = mydb.cursor()
       cur.execute("select * from class3B")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
   
    if classn == "3C": 
       cur = mydb.cursor()
       cur.execute("select * from class3C")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "3D": 
       cur = mydb.cursor()
       cur.execute("select * from class3D")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))


    if classn == "4": 
       cur = mydb.cursor()
       cur.execute("select * from class4")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "4B": 
       cur = mydb.cursor()
       cur.execute("select * from class4B")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
   
    if classn == "4C": 
       cur = mydb.cursor()
       cur.execute("select * from class4C")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "4D": 
       cur = mydb.cursor()
       cur.execute("select * from class4D")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "5": 
       cur = mydb.cursor()
       cur.execute("select * from class5")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "5B": 
       cur = mydb.cursor()
       cur.execute("select * from class5B")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
   
    if classn == "5C": 
       cur = mydb.cursor()
       cur.execute("select * from class5C")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "5D": 
       cur = mydb.cursor()
       cur.execute("select * from class5D")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "6": 
       cur = mydb.cursor()
       cur.execute("select * from class6")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "6B": 
       cur = mydb.cursor()
       cur.execute("select * from class6B")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
   
    if classn == "6C": 
       cur = mydb.cursor()
       cur.execute("select * from class6C")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "6D": 
       cur = mydb.cursor()
       cur.execute("select * from class6D")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "7": 
       cur = mydb.cursor()
       cur.execute("select * from class7")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "7B": 
       cur = mydb.cursor()
       cur.execute("select * from class7B")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
   
    if classn == "7C": 
       cur = mydb.cursor()
       cur.execute("select * from class7C")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "7D": 
       cur = mydb.cursor()
       cur.execute("select * from class7D")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "8": 
       cur = mydb.cursor()
       cur.execute("select * from class8")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "8B": 
       cur = mydb.cursor()
       cur.execute("select * from class8B")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
   
    if classn == "8C": 
       cur = mydb.cursor()
       cur.execute("select * from class8C")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "8D": 
       cur = mydb.cursor()
       cur.execute("select * from class8D")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "9": 
       cur = mydb.cursor()
       cur.execute("select * from class9")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "9B": 
       cur = mydb.cursor()
       cur.execute("select * from class9B")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
   
    if classn == "9C": 
       cur = mydb.cursor()
       cur.execute("select * from class9C")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "9D": 
       cur = mydb.cursor()
       cur.execute("select * from class9D")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "10A": 
       cur = mydb.cursor()
       cur.execute("select * from class10")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "10B": 
       cur = mydb.cursor()
       cur.execute("select * from class10B")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
   
    if classn == "10C": 
       cur = mydb.cursor()
       cur.execute("select * from class10C")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    if classn == "10D": 
       cur = mydb.cursor()
       cur.execute("select * from class10D")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)
        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if (classn == "11A") : 
       cur = mydb.cursor()
       cur.execute("select * from class11A")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "12A": 
       cur = mydb.cursor()
       cur.execute("select * from class12A")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "11B": 
       cur = mydb.cursor()
       cur.execute("select * from class11B")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10} ".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "12B": 
       cur = mydb.cursor()
       cur.execute("select * from class12B")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "11C": 
       cur = mydb.cursor()
       cur.execute("select * from class11C")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "12C": 
       cur = mydb.cursor()
       cur.execute("select * from class12C")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "11D": 
       cur = mydb.cursor()
       cur.execute("select * from class11D")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

    if classn == "12D":
       cur = mydb.cursor()
       cur.execute("select * from class12D")
       f = cur.fetchall()
       data = []
       print ("{:<10} {:<15} {:<10} {:<20} {:<10} ".format('Name','Lastname','Class','Guardian','Previous Class','Percentage'))
       for i in f:
        data.append(i)

        print ("{:<10} {:<15} {:<10} {:<20} {:<10} ".format(i[0],i[1],i[2],i[3],i[4],i[5]))

        #print(tabulate(data,headers=["Name","Lastname","Class","Guardian","Privous     Class"]))

       #print("Name"+" "*5,"Lastname"+" "*5,"Class"+" "*5,   "Guardian"+" "*8,  "Previous Class")
       #for i in f:
        #print(str(i[0])+" "*5,str(i[1])+" "*6,str(i[2])+" "*10,str(i[3])+" "*5,str (i[4]))
#main part
def quit():
    print("thankyou")
dict = {1:addstu,2:display,3:quit}
choice =  0
while choice != 3:

    print('''     ------------------------------------------------
         Christ Church Boys' Senior Secondary School
               Admission for session 2022-23    
     ------------------------------------------------''')
    print("         \n       -----Select from the following options-----")
    print("\n")
    print('''           -------------------------------
            1.To Add a New Students Data\n
         -------------------------------------''')
    print('''      \n       -------------------------------------------
        2.To Display Record of a Particular Class
        -------------------------------------------''')
    choice = int(input("enter your choice"))
    dict.get(choice)()
    






