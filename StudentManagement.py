import mysql.connector as m

db=m.connect(host="localhost",user="root",password="root")
cursor=db.cursor()
cursor.execute("create database if not exists School_data")
cursor.execute("use School_data")
#db=m.connect(host="localhost",user="root",password="root",database="project")
cursor.execute("create table if not exists school(roll_number int primary key auto_increment,sname varchar(30))")
#print("Done")


def addstudent():
    import mysql.connector as m
    db=m.connect(host="localhost",user="root",password="root",database="project")
    cursor=db.cursor()
    query1="insert into school(sname) values(%s)"
    sname=input("Enter the Name : ")
    cursor.execute(query1,[sname])

    db.commit()
    

    print("Record Saved")
    print("\n")


def delstudent():
    import mysql.connector as m
    db=m.connect(host="localhost",user="root",password="root",database="project")
    cursor=db.cursor()
    n=int(input("Enter the roll number"))
    query="delete from school where roll_number=%s;"
    cursor.execute(query,[n])
    result=cursor.fetchall()
    for record in result:
        print(record)
    db.commit()
    print("Done")
    show()
    print("\n")



def update():
    import mysql.connector as m
    db=m.connect(host='localhost',user="root",password="root",database='project')
    cursor=db.cursor()
    n=int(input("Enter the roll number"))
    usname=input("Enter the updated name")
    query="update school set sname=%s where roll_number=%s;"
    cursor.execute(query,[usname,n])
    result=cursor.fetchall()
    for record in result:
        print(record)
    db.commit()
    print("Done")
    show()
    print("\n")



def show():
    import mysql.connector as m
    db=m.connect(host='localhost',user="root",password="root",database='project')
    cursor=db.cursor()
    query="select * from school;"
    cursor.execute(query)
    result=cursor.fetchall()
    for record in result:
        print(record)
    db.commit()
    print("\n")

""" n=int(input("Enter your choice"))

if n==1:
    addstudent(n)
elif n==2:
    delstudent(n)
elif n==3:
    update(n)
elif n==4:
    show(n) """

print("Student Admission System\nPress Enter for more options")
input()
while 1:
    print(1,".Add Student")
    print(2,".Delete Student")
    print(3,".Update Student")
    print(4,".Show Student")
    print(0,".Exit")

    print("\n")
    n=int(input("Enter Your Choice: "))
    match n:
        case 1:
            addstudent()
        case 2:
            delstudent()
        case 3:
            update()
        case 4:
            show()
        case 0:
            exit() 