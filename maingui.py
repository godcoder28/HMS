from tkinter import *
from tkinter import messagebox
import mysql.connector
mydb=mysql.connector.connect(user="root", password="shivang280703",host="localhost",database="coder01")
c=mydb.cursor()
c.execute("delete from bookings where cout <(select curdate())")
c.execute("update rooms set status=0 where roomn not in (select bookings.roomno from bookings);")
mydb.commit()
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
        i_d2=c.fetchall()
        messagebox.showinfo("ID & Room No.","Your ID & Room No. are: "+str(i_d2[0][0])+" and "+str(i_d2[0][1]))
        c.execute("UPDATE rooms SET status=1 WHERE roomn=%s",(rn1,))
def cancel():
    messagebox.askquestion("Confirm", "Are you sure?")
    id=(str(i_d.get()),)
    c.execute("DELETE FROM BOOKINGS WHERE BOOKINGID=%s",id)
    mydb.commit()
mainw=Tk()
mainw.title("The LEELA PLACE Systems")
mainw.geometry('740x780')
welc=Label(mainw, text='WELCOME',relief='solid',font='times 64 bold',anchor='s')
welc.place(y=20,x=130)
leftframe=Frame(mainw,bd=10,height=600,width=700,relief=RIDGE,bg="powder blue")
leftframe.place(x=20,y=150)

newb=Label(leftframe, text='New Bookings',font='times 30 bold')
newb.place(y=20,x=250)
canb=Label(leftframe, text='Cancel Bookings',font='times 30 bold')
canb.place(x=220,y=350)
name = Label(leftframe, text="Name").place(x=30,y=70)
email = Label(leftframe, text="Email").place(x=30, y=110)
n1=StringVar()
e3=StringVar()
e1 = Entry(leftframe,textvar=n1).place(x=80, y=70)
e2 = Entry(leftframe,textvar=e3).place(x=80, y=110)
roomtype = Label(leftframe, text="Room Type:").place(x=30, y=150)
room=StringVar()
r1=Radiobutton(leftframe, text="Deluxe", variable=room, value='deluxe').place(x=120,y=150)
r2=Radiobutton(leftframe, text="Executive", variable=room, value='executive').place(x=200, y=150)
r3=Radiobutton(leftframe, text="Suit", variable=room, value='suit').place(x=290, y=150)
sbtn_1 = Button(leftframe,text="Submit",command=new,activebackground="pink", activeforeground="blue").place(x=200, y=270)
cin = Label(leftframe, text="CheckIN Date").place(x=30, y=190)
cout = Label(leftframe, text="CheckOUT Date").place(x=30, y=230)
ind=StringVar()
outd=StringVar()
c1 = Entry(leftframe,textvar=ind).place(x=160, y=190)
c2 = Entry(leftframe,textvar=outd).place(x=160, y=230)
book_id= Label(leftframe, text="Booking ID :-").place(x=30, y=450)
i_d=StringVar()
e1 = Entry(leftframe,textvar=i_d).place(x=130, y=450)
sbtn_2 = Button(leftframe,text="Submit",command=cancel,activebackground="pink", activeforeground="blue").place(x=150, y=500)
mainw.mainloop()





