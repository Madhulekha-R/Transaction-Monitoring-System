#DETAILS OF ACCOUNT HOLDERS

#SENDER'S DETAILS

print('SENDERS DETAILS\n')
bank_name = "abc_1"
senders_country = "india"
senders_ifsc_code = "abc001"
senders_swift_code = "hgsdgmhgb"
senders_name = input('Account holder name:')
senders_account_no = int(input('Account number:'))
print('\n')

#RECEIVER'S DETAILS

print('RECEIVERS DETAILS\n')
receivers_name = input('Account holder name:')
bank_name = input('Bank name:')
receiver_country = input('Country:')
receiver_account_no = int(input('Account number:'))
receiver_ifsc_code=input("IFSC code:")
receiver_swift_code = input('SWIFT code:')
print('\n')

#INTERFACING SQL AND PYTHON

import mysql.connector
mycon=mysql.connector.connect(host="myhost",user="myuser",passwd="mypassword",
database="rbi",auth_plugin="mysql_native_password")
cur=mycon.cursor()

#AUTHENTICATION PROCESS

#NRI TRANSACTION

if senders_country=="india" and receiver_country=="india":
    mode="local"
else:
    mode="nri"
print(".....VERIFYING.....")
print('\n')

if mode=="nri":
    cur.execute("select name,address,pannumber from abc_holders;")
    data=cur.fetchall()
    lst1=[]

    for i in data:
        lst1.append(list(i))
    lst2=[]

    for j in lst1:
        if senders_name==j[0]:
        lst2.append(j)

    name=lst2[0][0]
    address=lst2[0][1]
    pannumber=lst2[0][2]
 
    query="Insert into transferer values('{}','{}','{}')".format(name,address,pannumber)
    cur.execute(query)
    mycon.commit()
    cur.execute("select*from transferer;")
    data=cur.fetchall()
 
    query="select blacklist.pannumber, transferer.pannumber from blacklist inner join transferer on blacklist.pannumber=transferer.pannumber;"
    cur.execute(query)
    data=cur.fetchall()

    if data==[]:
        print('PROCEED FURTHER')
        print('\n')

        cur.execute("select*from swiftcode;")
        data=cur.fetchall()
        lst=[]

        for i in range(0,len(data)):
            lst.append(data[i][1])

        while True:
            if receiver_swift_code not in lst:
                print("Enter the correct SWIFT code")
                receiver_swift_code=input("SWIFT code:")
                print('\n')
                print(".....VERIFYING.....")
                print('\n')
                break
            else:
                break

        print("TRANSACTION CONFIRMATION DETAILS\n")
        amount=int(input("Enter the amount to be transferred:"))
        print('\n')
        trans=input("Is All The Above Details Correct(Yes/No):")

        if trans=="Yes":
            from tkinter import *
            import tkinter.messagebox
            root=tkinter.Tk()
            root.title("Conformation")
            root.geometry('300x200')

            def yes():
                tkinter.messagebox.showinfo("Conformation", "Transaction Proceeds")

            button1=Button(root,text="YES", command=yes, height=2, width=3)
            button1.place(relx=0.5, rely=0.5, anchor=E)
            root.mainloop()

        else:
            from tkinter import *
            import tkinter.messagebox
            root=tkinter.Tk()
            root.title("Conformation")
            root.geometry('300x200')

            def no():
                tkinter.messagebox.showinfo("Conformation", "Transaction Denied")

            button2=Button(root,text="NO", command=no, height=2, width=3)
            button2.place(relx=0.5, rely=0.5, anchor=W)
            root.mainloop()

    else:
        print('TRANSACTION DENIED')
        print('YOUR ACCOUNT IS NOT ACCESSIBLE')
        cur.execute("delete from transferer where name='raj';")
        data=cur.fetchall()
        mycon.commit()
    print('\n')

#LOCAL TRANSACTION

else:
    cur.execute("select name,address,pannumber from abc_holders;")
    data=cur.fetchall()
    lst1=[]

    for i in data:
        lst1.append(list(i))
    lst2=[]

    for j in lst1:
        if senders_name==j[0]:
            lst2.append(j)
    name=lst2[0][0]
    address=lst2[0][1]
    pannumber=lst2[0][2]

    query="Insert into transferer values('{}','{}','{}')".format(name,address,pannumber)
    cur.execute(query)
    mycon.commit()
    cur.execute("select*from transferer;")
    data=cur.fetchall()

    query="select blacklist.pannumber, transferer.pannumber from blacklist inner join transferer on blacklist.pannumber=transferer.pannumber;"
    cur.execute(query)
    data=cur.fetchall()

    if data==[]:
        print('PROCEED FURTHER')
        print('\n')
        cur.execute("select*from ifsccodes;")
        data=cur.fetchall()
        lst=[]

        for i in range(0,len(data)):
            lst.append(data[i][1])

        while True:
            if receiver_ifsc_code not in lst:
                print("Enter the correct IFSC code")
                receiver_ifsc_code=input("IFSC code:")
                print('\n')
                print(".....VERIFYING.....")
                print('\n')
                break
            else:
                break

        print("TRANSACTION CONFIRMATION DETAILS\n")
        amount=int(input("Enter the amount to be transferred:"))
        print('\n')

        trans=input("Is All The Above Details Correct(Yes/No):")

        if trans=="Yes":
            from tkinter import *
            import tkinter.messagebox
            root=tkinter.Tk()
            root.title("Conformation")
            root.geometry('300x200')

            def yes():
                tkinter.messagebox.showinfo("Conformation", "Transaction Proceeds")

            button1=Button(root,text="YES", command=yes, height=2, width=3)
            button1.place(relx=0.5, rely=0.5, anchor=E)
            root.mainloop()

        else:
            from tkinter import *
            import tkinter.messagebox
            root=tkinter.Tk()
            root.title("Conformation")
            root.geometry('300x200')

            def no():
                tkinter.messagebox.showinfo("Conformation", "Transaction Denied")

            button2=Button(root,text="NO", command=no, height=2, width=3)
            button2.place(relx=0.5, rely=0.5, anchor=W)
            root.mainloop()

    else:
        print('TRANSACTION DENIED')
        print('YOUR ACCOUNT IS NOT ACCESSIBLE')
        cur.execute("delete from transferer where name='raj';")
        data=cur.fetchall()
        mycon.commit()
    print('\n')
    
print("YOUR HEARTLY WELCOME TO OUR BANK")
