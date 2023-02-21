import random
import mysql.connector as m
p=input("Please Enter Your Mysql Password: ")
db=m.connect(host="localhost",user="root",password=p)
cursor=db.cursor()
cursor.execute("create database if Not Exists PassbookManagement;")    
cursor.execute("use PassbookManagement")
cursor.execute("create table if not exists Accounts (AccountNo int auto_increment,Name varchar(100),Balance int default 1500, primary key(AccountNo,Name)) auto_increment=100000")

def createAccount():
    print('\033[1m' +"You Chose to create an Account please Follow the Steps Ahead to Create An Account "+'\033[0m')
    
    while 1 :
        name=input("Enter Your Name: ")
        if ((any(chr.isdigit() for chr in name)) or len(name)==1 or name==''):
            print("Name can't have Numbers or Single Character or Empty \n Please Try again")
            break
            
        b=input("Default Initial Amount is 1500 do you Want to Deposit More (y/n) ")
        if(b.casefold()=='y'.casefold() ):
            q2="insert into Accounts (balance,name) values (%s,%s)"
            balance=int(input("Enter Amount You Want to Deposit: "))
            if (balance<1500):
                print("Minimum is 1500")
                break
            cursor.execute(q2,[balance,name])
            db.commit()
            break
            
        elif(b.casefold()=='n'.casefold()):
            q4=("insert into Accounts (name) values (%s);")
            cursor.execute(q4,[name])
            db.commit()
            break
        else:
            print("Wrong Input Try Again")
            break
            
    q1=("select AccountNo from Accounts where name = %s;")
    cursor.execute(q1,[name])
    # db.commit()
    result=cursor.fetchall()
    for i in result:
        for j in i:
            print('\033[1m'+name,"\nYour Accoount No is : ",j,'\033[0m')
            

        

def checkbalance():
    AccNo=input("Please Enter Your AccountNo: ")
    q1="select name,balance from Accounts where AccountNo=%s;"
    cursor.execute(q1,[AccNo])
    # db.commit()
    balance=cursor.fetchall()
    if (balance==[]):
        print("OOps! Wrong AccountNo\n Please Try Again\n")
    for i in balance:
        print(i[0],':\n'+'\033[1m'+"Available Balance :",i[1],'₹'+'\033[0m')

             
        

def deposit():
    temp=0
    AccNo=input("Please Enter Your AccountNo: ")
    
    q1="select balance from Accounts where AccountNo=%s;"
    cursor.execute(q1,[AccNo])
    # db.commit()
    balance=cursor.fetchall()
    if (balance==[]):
        print("OOps! Wrong AccountNo\n Please Try Again\n")
        return 
    Amt=int(input("Enter The deposit Amount: "))
    for i in balance:
        print("\033[1m"+"Balance Befor Deposite: ",i[0],'₹'+'\033[0m')
        temp=i[0]+Amt
    q2="update Accounts set balance=%s where Accountno=%s;"
    cursor.execute(q2,[temp,AccNo])
    db.commit()
    q3="select name,balance from Accounts where AccountNo=%s;"
    cursor.execute(q3,[AccNo])
    # db.commit()
    balance=cursor.fetchall()
    for i in balance:
        print(i[0],':\n'+'\033[1m'+'\033[1m'+"Balance After Deposit :",i[1],'₹'+'\033[0m')
    


def withdraw():
    temp=0
    AccNo=input("Please Enter Your AccountNo: ")
    
    q1="select balance from Accounts where AccountNo=%s;"
    cursor.execute(q1,[AccNo])
    balance=cursor.fetchall()
    if (balance==[]):
        print("Oops! Wrong AccountNo\n Please Try Again\n")
        return 
    Amt=int(input("Enter The Withdrawal Amount: "))
    for i in balance:
        print("\033[1m"+"Balance Before Withdrawal: ",i[0],'\033[0m')
        temp=i[0]-Amt
    if(temp>1500):
        for i in balance:
            print("\033[1m"+"Balance Before Withdrawal: ",i[0],'\033[0m')
        q2="update Accounts set balance=%s where Accountno=%s;"
        cursor.execute(q2,[temp,AccNo])
        db.commit()
        q3="select name,balance from Accounts where AccountNo=%s;"
        cursor.execute(q3,[AccNo])
        # db.commit()
        balance=cursor.fetchall()
        for i in balance:
            print(i[0],':\n'+'\033[1m'+'\033[1m'+"Balance After Withdrawal :",i[1],'₹'+'\033[0m')
    else:
        for i in balance:
            print("\033[1m"+"Available Balance: ",i[0],'\033[0m')
        print('\033[1m'+"Low Balance Can't Withdraw :("+'\033[0m')
        print('\033[1m'+"Minimum Balance Should be 1500 ₹"+'\033[0m')
    
    

print("Passbook Management System\nPress Enter for more options")
input()
while 1:
    print(1,".Create Account")
    print(2,".Check Balance")
    print(3,".Deposit An Amount")
    print(4,".Withdraw An Amount")
    print(0,".Exit")
    a=int(input("Enter Your Choice: "))
    match a:
        case 1:
            createAccount()
        case 2:
            checkbalance()
        case 3:
            deposit()
        case 4:
            withdraw()
        case 0:
            exit()