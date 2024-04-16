from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("costumer")
        self.root.geometry("1295x550+230+220")

#title for hms 
        lbl_title=Label(self.root, text="ADD COSTUMER DETAILS", font=("time new roman",20,"bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0, width=1295, height=50)
# logo
        img2=Image.open(r"C:\Users\ASUS\Desktop\HMS\image\h2.png")
        img2=img2.resize((230,140))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100 , height=50)
###lable frame
        labelframeleft=LabelFrame(self.root,bd=2,text="COSTUMER DETAILS", relief=RIDGE, font=("time new roman",18,"bold"), fg="gold" )
        labelframeleft.place(x=4, y=50, width=425, height=490)

# label and entry
        lbl_cust_ref=Label(labelframeleft, text="Costumer Ref",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)  

        enty_ref=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        enty_ref.grid(row=0, column=1)

        # name
        cname=Label(labelframeleft, text="Costurmer Name",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)  

        txt_cname=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_cname.grid(row=1, column=1)

        #parents name
        pname=Label(labelframeleft, text="Parents Name",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        pname.grid(row=2, column=0, sticky=W)  

        txt_pname=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_pname.grid(row=2, column=1)

        #gender
        label_gender=Label(labelframeleft, text="Gender",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)  

        combo_gender=ttk.Combobox(labelframeleft,width=27, font=("times new roman",13, "bold"),state="read only")
        combo_gender["value"]=("Male","Female","Others")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)



        #postcode
        lblpostcode=Label(labelframeleft, text="Post Code",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lblpostcode.grid(row=4, column=0, sticky=W)  

        txt_postcode=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_postcode.grid(row=4, column=1)

        # mobile number
        lblmobile=Label(labelframeleft, text="Mobile Number",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lblmobile.grid(row=5, column=0, sticky=W)  

        txt_mobile=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_mobile.grid(row=5, column=1)

        #email
        lblemail=Label(labelframeleft, text="Email ",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lblemail.grid(row=6, column=0, sticky=W)  

        txt_email=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_email.grid(row=6, column=1)

        #nationality
        lblNationality=Label(labelframeleft, text="Nationality",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)  

        combo_Nationality=ttk.Combobox(labelframeleft,width=27, font=("times new roman",13, "bold"),state="read only")
        combo_Nationality["value"]=("Nepal","china","USA", "UK", "Switzerland", "Canada", "Dubai", "Qatar")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        #id-proof
        lblidproof=Label(labelframeleft, text="Id ",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lblidproof.grid(row=8, column=0, sticky=W)  

        combo_idproof=ttk.Combobox(labelframeleft,width=27, font=("times new roman",13, "bold"),state="read only")
        combo_idproof["value"]=("National Id Card", "Passport", "Driving license Card")
        combo_idproof.current(0)
        combo_idproof.grid(row=8, column=1)
     

        #id number
        lblidnumber=Label(labelframeleft, text="Id number",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lblidnumber.grid(row=9, column=0, sticky=W)  

        txt_idnumber=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_idnumber.grid(row=9, column=1)

        #address 
        lbladdress=Label(labelframeleft, text="Address",fg="black", font=("times new romain",13,"bold"), padx=2, pady=6)
        lbladdress.grid(row=10, column=0, sticky=W)  

        txt_address=ttk.Entry(labelframeleft,width=29, font=("times new roman",13, "bold"))
        txt_address.grid(row=10, column=1)
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

#table frame
        table_frame=LabelFrame(self.root, text="Details and History",relief=RIDGE, bd=4, font=("times new roman",14,"bold"))
        table_frame.place(x=435, y=50, width=860, height=490)

        lblsearchBy=Label(table_frame, text="Search By", bd=2, font=("times new roman",14,"bold"),bg="white",fg="red")
        lblsearchBy.grid(row=0, column=0, sticky=W, padx=2)

        combo_searchBy=ttk.Combobox(table_frame,width=24, font=("times new roman",13, "bold"),state="read only")
        combo_searchBy["value"]=("mobile", "Ref")
        combo_searchBy.current(0)
        combo_searchBy.grid(row=0, column=1, padx=2)

        txt_searchBy=ttk.Entry(table_frame,width=24, font=("times new roman",13, "bold"))
        txt_searchBy.grid(row=0, column=2, padx=2)

        btnshow=Button(table_frame,text="SHOW",fg="gold",bg="black", font=("times new romain",13,"bold"), width=9)
        btnshow.grid(row=0, column=3, padx=1)

        btnshowall=Button(table_frame,text="SHOW ALL",fg="gold",bg="black", font=("times new romain",13,"bold"), width=9)
        btnshowall.grid(row=0, column=4, padx=1)

# show data table
        details_table=Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x=ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)
        self.cust_details_table = ttk.Treeview(details_table, columns=("ref", "cname", "pname", "gender", "postcode", "mobile", "email", "Nationality", "idproof", "idnumber", "address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref", text="Ref No")
        self.cust_details_table.heading("cname",text="Name")
        self.cust_details_table.heading("pname", text="Parents name ")
        self.cust_details_table.heading("gender", text="Gender")
        self.cust_details_table.heading("postcode", text="Post Code")
        self.cust_details_table.heading("mobile", text="Mobile No")
        self.cust_details_table.heading("email", text="Email")        
        self.cust_details_table.heading("Nationality", text="Nationality")
        self.cust_details_table.heading("idproof", text="ID proof")
        self.cust_details_table.heading("idnumber", text="ID Number")
        self.cust_details_table.heading("address", text="Address")

        self.cust_details_table["show"]="headings"    
        self.cust_details_table.column("ref",width=100)    
        self.cust_details_table.column("cname",width=100)    
        self.cust_details_table.column("pname",width=100)    
        self.cust_details_table.column("gender",width=100)    
        self.cust_details_table.column("postcode",width=100)     
        self.cust_details_table.column("mobile",width=100)     
        self.cust_details_table.column("email",width=100)   
        self.cust_details_table.column("Nationality",width=100)    
        self.cust_details_table.column("idproof",width=100)    
        self.cust_details_table.column("idnumber",width=100)    
        self.cust_details_table.column("address",width=100)     
        
        self.cust_details_table.pack(fill=BOTH,expand=1)

#title for hms 
if __name__ == '__main__':
    root=Tk()
    object=Cust_Win(root)
    root.mainloop()

