from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class room_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("costumer")
        self.root.geometry("1295x550+230+220")

#title for hms 
        lbl_title=Label(self.root, text="ROOM BOOKING SERVICES", font=("time new roman",20,"bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0, width=1295, height=50)
# logo
        img2=Image.open(r"C:\Users\ASUS\Desktop\HMS\image\h2.png")
        img2=img2.resize((230,140))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100 , height=50)
###lable frame
        labelframeleft=LabelFrame(self.root,bd=2,text="Costumer Details", relief=RIDGE, font=("time new roman",18,"bold"), fg="gold" )
        labelframeleft.place(x=4, y=50, width=425, height=490)


# label and entry
#costumer contact
        lbl_cust_contact=Label(labelframeleft, text="Costumer Contact",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)  

        enty_contact=ttk.Entry(labelframeleft,width=20, font=("times new roman",13, "bold"))
        enty_contact.grid(row=0, column=1,sticky=W)

        #fetch data button
        btnfetchdata=Button(labelframeleft,text="Fetch Data",fg="gold",bg="black", font=("times new romain",8,"bold"), width=9 )
        btnfetchdata.place(x=350,y=4)

        # checkin date
        check_in_date=Label(labelframeleft, text="Check in Date",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)  

        txt_check_in_date=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_check_in_date.grid(row=1, column=1)

        #checkout date
        checkout_date=Label(labelframeleft, text="Checkout Date",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        checkout_date.grid(row=2, column=0, sticky=W)  

        txt_checkout_date=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_checkout_date.grid(row=2, column=1)

        #Room type
        label_type=Label(labelframeleft, text="Room Type",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        label_type.grid(row=3, column=0, sticky=W)  

        combo_gender=ttk.Combobox(labelframeleft,width=27, font=("times new roman",13, "bold"),state="read only")
        combo_gender["value"]=("silver","Gold","Platinium")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)



        #Avilable room
        lblAvilableroom=Label(labelframeleft, text="Avilable Room",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lblAvilableroom.grid(row=4, column=0, sticky=W)  

        txt_Avilable=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_Avilable.grid(row=4, column=1)

        # meal
        lblmeal=Label(labelframeleft, text="Meal",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lblmeal.grid(row=5, column=0, sticky=W)  

        txt_meal=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_meal.grid(row=5, column=1)

        #no of days
        lblno=Label(labelframeleft, text="No of Days ",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lblno.grid(row=6, column=0, sticky=W)  

        txt_no=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_no.grid(row=6, column=1)

        #paid tax
        lblpaidtax=Label(labelframeleft, text="Paid tax",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lblpaidtax.grid(row=7, column=0, sticky=W)  

        txt_paidtax=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_paidtax.grid(row=7, column=1)

        #sub total
        lblsubtotal=Label(labelframeleft, text="Sub total" ,fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lblsubtotal.grid(row=8, column=0, sticky=W)  
       
        txt_subtotal=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_subtotal.grid(row=8, column=1)
      #total
        lbltotal=Label(labelframeleft, text="Total" ,fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lbltotal.grid(row=9, column=0, sticky=W)  
       
        txt_total=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_total.grid(row=9, column=1)
####bill buttons
        btnbill=Button(labelframeleft,text="Bill",fg="gold",bg="black", font=("times new romain",13,"bold"), width=9 )
        btnbill.grid(row=10, column=0, padx=1,sticky=W)     

# buttons
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnadd=Button(btn_frame,text="ADD",fg="gold",bg="black", font=("times new romain",13,"bold"), width=9)
        btnadd.grid(row=0, column=0, padx=1)

        btnupdate=Button(btn_frame,text="UPDATE",fg="gold",bg="black", font=("times new romain",13,"bold"), width=9)
        btnupdate.grid(row=0, column=1, padx=1)

        btndelete=Button(btn_frame,text="DELETE",fg="gold",bg="black", font=("times new romain",13,"bold"), width=9)
        btndelete.grid(row=0, column=2, padx=1)

        btnreset=Button(btn_frame,text="RESET",fg="gold",bg="black", font=("times new romain",13,"bold"), width=9 )
        btnreset.grid(row=0, column=3, padx=1)

if __name__ == '__main__':
    root=Tk()
    object=room_Win(root)
    root.mainloop()
