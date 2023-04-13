###--BANKING--###

import random
import pandas as pd
from csv import writer
import csv
from re import A

data=pd.read_csv("test.csv",index_col=0)
print("\t\t\t\tBANKING PORTAL\n")

#TO CREATE AN A BANK ACCOUNT
def createAccount(account_num,name_of_holder,typeof_account,amount,username,password):
  l=[account_num,name_of_holder,typeof_account,amount,username,password]
  with open("test.csv","a") as f:
    writer_object = writer(f,lineterminator='\n')
    writer_object.writerow(l)
    f.close()
  print("\nYOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED...\n")
  return



#TO CHECK ACCOUNT BALANCE
def checkBalance(account_num):
  data=pd.read_csv("test.csv",index_col=0)
  print("\nYOUR CURRENT BANK BALANCE:",data['amount'][account_num])


#TO WITHDRAW AMOUNT FROM AN ACCOUNT
def withdrawAmount(account_num,amount):
  data=pd.read_csv("test.csv",index_col=0)
  text = open("test.csv", "r")
  text = ''.join([i for i in text]) \
      .replace(str(data['amount'][account_num]),str(data['amount'][account_num]-amount))
  x = open("test.csv","w")
  x.writelines(text)
  x.close()

#TO DEPOSIT AMOUNT TO A BANK ACCOUNT
def depositAmount(account_num,amount):
  data=pd.read_csv("test.csv",index_col=0)
  text = open("test.csv", "r")
  text = ''.join([i for i in text]) \
      .replace(str(data['amount'][account_num]),str(data['amount'][account_num]+amount))
  x = open("test.csv","w")
  x.writelines(text)
  x.close()
#TRANSFER AMOUNT
def transferAmount(account_num1,account_num2,amount):
  withdrawAmount(account_num1,amount)
  depositAmount(account_num2,amount)

#TO CLOSE A BANK ACCOUNT
def deleteAccount(accnum):
  file=open("test.csv","r")
  data=csv.reader(file)
  list=[]
  for row in data:
    if str(accnum) not in row:
        list.append(row)
  file.close()
  csvfile=open("test.csv","w",newline="")
  write=csv.writer(csvfile)
  write.writerows(list)
  csvfile.close()

#LOGIN SECTION
def login():
    file=open("test.csv","r")
    data=csv.reader(file)
    dict={}
    for row in data:
        if len(row)!=0 and row[4]!="username" and row[5]!="password":
            dict[row[4]]=row[5]
    username=input("Enter USERNAME :")
    if username in dict.keys():
        password=input("ENTER PASSWORD: ")
        if(dict[username]==password):
            print("\nLOGIN SUCCESSFUL!\n")
            return 1
        else:
            print("INCORRECT PASSWORD")
            return 0
    else:
        print("INCORRECT USERNAME")
        return 0
    file.close()


#CODE
print("1.NEW ACCOUNT HOLDER")
print("2.EXISTING ACCOUNT HOLDER")
choice=int(input("ENTER YOUR CHOICE:"))
if choice==1:
    #ACCOUNT CREATION SECTION
    data=pd.read_csv("test.csv")
    while 1:
        account_num = random.randint(1111,9999)
        if account_num not in list(data["account_num"]):
            break
    name_of_holder=input("ENTER THE ACCOUNT HOLDER NAME:")
    typeof_account=input("ENTER THE TYPE OF ACCOUNT (S(SAVINGS)/C(CURRENT)) : ")
    username=input("ENTER THE USERNAME : ")
    password=input("ENTER PASSWORD : ")
    amount=int(input("ENTER THE INITIAL AMOUNT(>=500 FOR SAVING AND >=1000 FOR CURRENT):"))
    createAccount(account_num,name_of_holder,typeof_account,amount,username,password)

elif choice==2:
    login_func=login()
    while (login_func):
        print("1.BALANCE ENQUIRY")
        print("2.WITHDRAW AMOUNT")
        print("3.DEPOSIT AMOUNT")
        print("4.TRANSFER THE AMOUNT")
        print("5.DELETE ACCOUNT")
        print("6.EXIT")
        n=int(input("ENTER YOUR CHOICE:"))
        if n==1:
            #BALANCE ENQUIRY SECTION
            account_num=int(input("ENTER THE ACCOUNT NUMBER:"))
            checkBalance(account_num)
        elif n==2:
            #AMOUNT WITHDRAW SECTION
            account_num=int(input("ENTER THE ACCOUNT NUMBER:"))
            data=pd.read_csv("test.csv",index_col=0)
            total_amount=data['amount'][account_num]
            print("YOUR CURRENT ACCOUNT BALANCE IS = ",total_amount)
            amount=int(input("ENTER THE AMOUNT TO BE WITHDRAW:"))
            withdrawAmount(account_num,amount)
            print(amount,"AMOUNT HAS BEEN WITHDRAWN FROM XXXX ACCOUNT")
            
        elif n==3:
            #AMOUNT DEPOSIT SECTION
            account_num=int(input("ENTER THE ACCOUNT NUMBER:"))
            amount=int(input("ENTER THE AMOUNT TO BE DEPOSITED:"))
            depositAmount(account_num,amount)
            print("SUCCESSFULLY DEPOSITED...")
        elif n==4:
            #TRANSFER OF AMMOUNT
            data=pd.read_csv("test.csv",index_col=0)
            account_num1=int(input("ENTER YOUR ACCOUNT NUMBER:"))
            print("YOUR CURRENT ACCOUNT BALANCE IS = ",data['amount'][account_num1])
            account_num2=int(input("ENTER RECIPIENT ACCOUNT NUMBER:"))
            amount=int(input("ENTER THE AMOUNT TO TRANSFER:"))
            transferAmount(account_num1,account_num2,amount)
            print("TRANSFERED SUCCESSFULLY....")
        elif n==5:
            #CLOSING AN ACCOUNT SECTION
            account_num=int(input("ENTER THE ACCOUNT NUMBER TO CLOSE:"))
            deleteAccount(account_num)
            print("YOUR ACCOUNT HAS BEEN SUCESSFULLY CLOSED..")
        elif n==6:
            break
