from tkinter import *
from PIL import Image,ImageTk
class HMS():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management system")
        self.root.geometry("1550x800+0+0")

#1st image
        img1=Image.open(r"C:\Users\ASUS\Desktop\HMS\image\h1.png")
        img1=img1.resize((1550,140))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)
# logo
        img1=Image.open(r"C:\Users\ASUS\Desktop\HMS\image\h2.png")
        img1=img1.resize((230,140))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230 , height=140)
#title for hms 
        lbl_title=Label(self.root, text="Hotel Management System", font=("time new roman",40,"bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=140, width=1550, height=50)

#main frame
        main_frame=Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0,y=190, width=1550, height=620)

#menu frame
        lbl_menu=Label(main_frame, text="Menu", font=("time new roman",20,"bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0,y=0, width=230)
#btn frame
        btn_frame=Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0,y=35, width=230, height=230)
#Booking info
        Costumer_btn=Button(btn_frame, text="COSTUMER",width=22,font=("time new roman",14,"bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        Costumer_btn.grid(row=0, column=0, pady=1)

        booking_btn=Button(btn_frame, text="BOOKING",width=22,font=("time new roman",14,"bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        booking_btn.grid(row=1, column=0, pady=1)

        room_btn=Button(btn_frame, text="ROOM",width=22,font=("time new roman",14,"bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=2, column=0, pady=1)

        payment_btn=Button(btn_frame, text="PAYMENT",width=22,font=("time new roman",14,"bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        payment_btn.grid(row=3, column=0, pady=1)

        record_btn=Button(btn_frame, text="RECORD",width=22,font=("time new roman",14,"bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        record_btn.grid(row=4, column=0, pady=1)

        exit_btn=Button(btn_frame, text="EXIT",width=22,font=("time new roman",14,"bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        exit_btn.grid(row=5, column=0, pady=1)










if __name__ == '__main__':
    root=Tk()
    object=HMS(root)
    root.mainloop()




    