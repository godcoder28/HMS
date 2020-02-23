from tkinter import *
from tkinter import messagebox
import mysql.connector
mydb=mysql.connector.connect(user="root", password="shivang280703",host="localhost",database="coder01")   #Connecting Db to project
c=mydb.cursor()
c.execute("delete from bookings where cout <(select curdate())")
c.execute("update rooms set status=0 where roomn not in (select bookings.roomno from bookings);")     #Daily necessary tasks
mydb.commit()
def shwin():
    c.execute("SELECT bookingid,name,roomno,cin,cout FROM bookings")
    data = c.fetchall()
    sh=Tk()
    sh.geometry('520x500')
    sh.title("CURRENT BOOKINGS")
    welc = Label(sh, text='Current Bookings', relief='solid', font='times 32 bold').pack()
    frame = Frame(sh, bd=10, height=600, width=450, relief=RIDGE, bg="powder blue")
    frame.place(x=20, y=100)
    h1 = Label(frame, padx=15,text="Booking ID").grid(row=0,column=0)
    h2 = Label(frame, padx=15,text="Name").grid(row=0, column=1)
    h3 = Label(frame, padx=15,text="Room No").grid(row=0, column=2)
    h4 = Label(frame, padx=15,text="Checkin Date").grid(row=0, column=3)
    h5 = Label(frame, padx=15,text="Checkout Date").grid(row=0, column=4)
    m=2
    for i in data:
        n=0
        for j in i:
            x=Label(frame, bg="powder blue",padx=15,text=j).grid(row=m,column=n)
            n+=1
        m+=2
def new():
    name=n1.get()
    mail=e3.get()
    rtype=(str(room.get()),)
    indt=ind.get()
    outdt=outd.get()
    c.execute("SELECT roomn FROM rooms WHERE status=0 and type = %s",rtype)
    rn=c.fetchall()
    if len(rn) == 0:
        messagebox.showerror("Error", "No Rooms Available")
    else:
        rn1=rn[0][0]
        sql = "INSERT INTO bookings (name,email,roomno,cin,cout) VALUES (%s, %s,%s, %s, %s)"
        val = (name, mail, rn1,indt, outdt)
        c.execute(sql, val)
        mydb.commit()
        c.execute("SELECT bookingid,roomno FROM bookings WHERE roomno=%s",(rn1,))
        id2=c.fetchall()
        messagebox.showinfo("ID & Room No.","Your Booking ID is: "+str(id2[0][0])+" and Room No is: "+str(id2[0][1]))
        c.execute("UPDATE rooms SET status=1 WHERE roomn=%s",(rn1,))
def cancel():
    messagebox.askquestion("Confirm", "Are you sure?")
    id=(str(cancelid.get()),)
    c.execute("DELETE FROM BOOKINGS WHERE BOOKINGID=%s",id)
    mydb.commit()
#Main Function
mainwin=Tk()
mainwin.title("THE LEELA PLACE")
mainwin.geometry('740x780')
welc=Label(mainwin, text='WELCOME',relief='solid',font='times 64 bold',anchor='s')
welc.place(y=20,x=30)
leftframe=Frame(mainwin,bd=10,height=600,width=700,relief=RIDGE,bg="powder blue")
leftframe.place(x=20,y=150)
showbook=Button(mainwin,text="SHOW BOOKINGS",command=shwin,font='times 16 bold',activebackground="pink", activeforeground="blue").place(x=520, y=50)
newbook=Label(leftframe, text='New Bookings',font='times 30 bold').place(y=20,x=250)
canbook=Label(leftframe, text='Cancel Bookings',font='times 30 bold').place(x=220,y=350)
name = Label(leftframe, text="Name").place(x=30,y=70)
n1=StringVar()
e1 = Entry(leftframe,textvar=n1).place(x=80, y=70)
email = Label(leftframe, text="Email").place(x=30, y=110)
e3=StringVar()
e2 = Entry(leftframe,textvar=e3).place(x=80, y=110)
roomtype = Label(leftframe, text="Room Type:").place(x=30, y=150)
room=StringVar()
r1=Radiobutton(leftframe, text="Deluxe", variable=room, value='deluxe').place(x=120,y=150)
r2=Radiobutton(leftframe, text="Executive", variable=room, value='executive').place(x=200, y=150)
r3=Radiobutton(leftframe, text="Suit", variable=room, value='suit').place(x=290, y=150)
submitbtn=Button(leftframe,text="Submit",command=new,activebackground="pink", activeforeground="blue").place(x=200, y=270)
checkin = Label(leftframe, text="CheckIN Date").place(x=30, y=190)
checkout = Label(leftframe, text="CheckOUT Date").place(x=30, y=230)
dateformat=Label(leftframe,text="Date Format- YYYY/MM/DD").place(x=320,y=210)
ind=StringVar()
c1 = Entry(leftframe,textvar=ind).place(x=160, y=190)
outd=StringVar()
c2 = Entry(leftframe,textvar=outd).place(x=160, y=230)
book_id= Label(leftframe, text="Booking ID :-").place(x=30, y=450)
cancelid=StringVar()
e1 = Entry(leftframe,textvar=cancelid).place(x=130, y=450)
cancelbtn=Button(leftframe,text="Submit",command=cancel,activebackground="pink", activeforeground="blue").place(x=150, y=500)
mainwin.mainloop()