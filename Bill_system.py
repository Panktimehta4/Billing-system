from tkinter import*
import math,random
import os
from tkinter import messagebox
import mysql.connector


class bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title(" ")
        title=Label(self.root,text="BILLING SYSTEM",bd=12,relief=GROOVE,bg="#616A6B ",fg="white",font=("times of roman",15,"bold"),pady=2).pack(fill=X)
        #======variables===
        #=========cosmetics======
        self.soap=IntVar()
        self.facewash=IntVar()
        self.facecream=IntVar()
        self.hairgel=IntVar()
        self.hairspray=IntVar()
        self.bodylotion=IntVar()
        #=========groceries====
        self.wheat=IntVar()
        self.oil=IntVar()
        self.cereals=IntVar()
        self.rice=IntVar()
        self.tea=IntVar()
        self.sugar=IntVar()
        #========refreshments=====
        self.coke=IntVar()
        self.sprite=IntVar()
        self.redbull=IntVar()
        self.kitkat=IntVar()
        self.sofit=IntVar()
        self.thumbsup=IntVar()
        #========total product price &tax variables
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.refreshment_price=StringVar()
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.refreshment_tax=StringVar()
        #=======customer=======
        self.cname=StringVar()
        self.cphn=StringVar()
        self.billno=StringVar()
        x=random.randint(1000,9999)
        self.billno.set(str(x))
        self.searchbill=StringVar()
        #====customer detail frame
        f1=LabelFrame(self.root,text="Customer Detail",bd=10,relief=GROOVE,bg="#616A6B",fg="gold",font=("times of roman",15,"bold"))
        f1.place(x=0,y=55,relwidth=1)
        cname=Label(f1,text="Customer name",bg="#616A6B",fg="white",font=("times of roman",15,"bold")).grid(row=0,column=0)
        ctext=Entry(f1,width=20,textvariable=self.cname,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=20)
        cphn=Label(f1,text="Phone no",bg="#616A6B",fg="white",font=("times of roman",15,"bold")).grid(row=0,column=2)
        cphn_txt=Entry(f1,width=20,textvariable=self.cphn,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=20)
        
        
        cbill=Label(f1,text="Bill no",bg="#616A6B",fg="white",font=("times of roman",15,"bold")).grid(row=0,column=4)
        cbill_text=Entry(f1,width=20,textvariable=self.billno,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=20)
        bill_btn=Button(f1,text="Search",command=self.find_bill,width=15,fg="black",bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10)
        #============cosmetic detail frame
        f2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,bg="#616A6B",fg="gold",font=("times of roman",15,"bold"))
        f2.place(x=4,y=145,width=325,height=380)
        bath_lbl=Label(f2,text="Bath soap",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=0,column=0,pady=10,sticky="w")
        bath_txt=Entry(f2,width=10,textvariable=self.soap,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        face_lbl=Label(f2,text="face wash",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=1,column=0,pady=10,sticky="w")
        face_txt=Entry(f2,width=10,textvariable=self.facewash,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        cream_lbl=Label(f2,text="face cream",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=2,column=0,pady=10,sticky="w")
        cream_txt=Entry(f2,width=10,textvariable=self.facecream,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        spray_lbl=Label(f2,text="Hair spray",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=3,column=0,pady=10,sticky="w")
        spray_txt=Entry(f2,width=10,textvariable=self.hairspray,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        gel_lbl=Label(f2,text="Hair gel",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=4,column=0,pady=10,sticky="w")
        gel_txt=Entry(f2,width=10,textvariable=self.hairgel,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        lotion_lbl=Label(f2,text="Body lotion",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=5,column=0,pady=10,sticky="w")
        lotion_txt=Entry(f2,width=10,textvariable=self.bodylotion,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        #================grocery detail frame
        f3=LabelFrame(self.root,text="Groceries",bd=10,relief=GROOVE,bg="#616A6B",fg="gold",font=("times of roman",15,"bold"))
        f3.place(x=338,y=145,width=325,height=380)
        wheat_lbl=Label(f3,text="Wheat",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=0,column=0,pady=10,sticky="w")
        wheat_txt=Entry(f3,width=10,textvariable=self.wheat,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        oil_lbl=Label(f3,text="Food oil",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=1,column=0,pady=10,sticky="w")
        oil_txt=Entry(f3,width=10,textvariable=self.oil,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        cereals_lbl=Label(f3,text="Cereals",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=2,column=0,pady=10,sticky="w")
        cereals_txt=Entry(f3,width=10,textvariable=self.cereals,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        tea_lbl=Label(f3,text="Tea",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=3,column=0,pady=10,sticky="w")
        tea_txt=Entry(f3,width=10,textvariable=self.tea,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        suger_lbl=Label(f3,text="Suger",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=4,column=0,pady=10,sticky="w")
        suger_txt=Entry(f3,width=10,textvariable=self.sugar,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        rice_lbl=Label(f3,text="Rice",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=5,column=0,pady=10,sticky="w")
        rice_txt=Entry(f3,width=10,textvariable=self.rice,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        #====================refreshment detail frame
        f4=LabelFrame(self.root,text="Refreshment",bd=10,relief=GROOVE,bg="#616A6B",fg="gold",font=("times of roman",15,"bold"))
        f4.place(x=670,y=145,width=325,height=380)
        coke_lbl=Label(f4,text="Coke",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=0,column=0,pady=10,sticky="w")
        coke_txt=Entry(f4,width=10,textvariable=self.coke,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        Sprite_lbl=Label(f4,text="Sprite",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=1,column=0,pady=10,sticky="w")
        Sprite_txt=Entry(f4,width=10,textvariable=self.sprite,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        redbull_lbl=Label(f4,text="Redbull",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=2,column=0,pady=10,sticky="w")
        redbull_txt=Entry(f4,width=10,textvariable=self.redbull,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        kitkat_lbl=Label(f4,text="Kitkat",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=3,column=0,pady=10,sticky="w")
        kitkat_txt=Entry(f4,width=10,textvariable=self.kitkat,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        Sofit_lbl=Label(f4,text="Sofit",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=4,column=0,pady=10,sticky="w")
        Sofit_txt=Entry(f4,width=10,textvariable=self.sofit,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        thumsup_lbl=Label(f4,text="Thums up",font=("times new roman",15,"bold"),bg="#616A6B",fg="black").grid(row=5,column=0,pady=10,sticky="w")
        thumsup_txt=Entry(f4,width=10,textvariable=self.thumbsup,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        #========bill generation frame
        f5=Frame(self.root,bd=10,relief=GROOVE)
        f5.place(x=1000,y=145,width=336,height=380)
        bill_title=Label(f5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #=========bill menu frame
        f6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,bg="#616A6B",fg="gold",font=("times of roman",15,"bold"))
        f6.place(x=0,y=532,relwidth=1,height=158)
        m1=Label(f6,text="Total cosmetic price",bg="#616A6B",fg="black",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(f6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=4)
        m2=Label(f6,text="Total grocery price",bg="#616A6B",fg="black",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(f6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=4)
        m3=Label(f6,text="Total refreshment price",bg="#616A6B",fg="black",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(f6,width=18,textvariable=self.refreshment_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=4)
        m4=Label(f6,text="Cosmetic Tax ",bg="#616A6B",fg="black",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        m4_txt=Entry(f6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=4)
        m5=Label(f6,text="Grocery Tax",bg="#616A6B",fg="black",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        m5_txt=Entry(f6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=4)
        m6=Label(f6,text="Refreshment Tax",bg="#616A6B",fg="black",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        m6_txt=Entry(f6,width=18,textvariable=self.refreshment_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=4)
        #=========button frame
        btn_frm=Frame(f6,bd=7,relief=GROOVE)
        btn_frm.place(x=755,width=570,height=115)
        total_btn=Button(btn_frm,command=self.total,text="Total",bg="cadetblue",fg="black",width=12,height=4,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_frm,command=self.bill_area,text="Generate Bill",bg="cadetblue",fg="black",width=12,height=4,font="arial 12 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_frm,text="Clear",command=self.clear_data,bg="cadetblue",fg="black",width=12,height=4,font="arial 12 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_frm,text="Exit",command=self.exit,bg="cadetblue",fg="black",width=12,height=4,font="arial 12 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
        self.cnx = mysql.connector.connect(user='root', 
                              host='localhost',
                              database='software')
        self.cursor = self.cnx.cursor()

    def total(self):
        self.csp=self.soap.get()*40
        self.fwp=self.facewash.get()*50
        self.fcp=self.facecream.get()*60
        self.hsp=self.hairspray.get()*100
        self.hgp=self.hairgel.get()*60
        self.blp=self.bodylotion.get()*120
        self.totalcosmetic_price=float(self.csp+self.fwp+self.fcp+self.hsp+self.hgp+self.blp)
        self.cosmetic_price.set("RS."+str(self.totalcosmetic_price))
        self.c_tax=round(self.totalcosmetic_price*0.28)
        self.cosmetic_tax.set("RS."+str(self.c_tax))
        #====grocery=====
        self.gwp=self.wheat.get()*35
        self.gop=self.oil.get()*100
        self.gcp=self.cereals.get()*60
        self.gtp=self.tea.get()*80
        self.gsp=self.sugar.get()*40
        self.grp=self.rice.get()*35
        self.totalgrocery_price=float(self.gwp+self.gop+self.gcp+self.gtp+self.gsp+self.grp)
        self.grocery_price.set("RS."+(str(self.totalgrocery_price)))
        self.g_tax=round(self.totalgrocery_price*0.28)
        self.grocery_tax.set("RS."+(str(self.g_tax)))
        #=======refreshent====
        self.rcp=self.coke.get()*35
        self.rsp=self.sprite.get()*40
        self.rrp=self.redbull.get()*100
        self.rkp=self.kitkat.get()*25
        self.rop=self.sofit.get()*90
        self.rtp=self.thumbsup.get()*45
        self.totalrefreshment_price=float(self.rcp+self.rsp+self.rrp+self.rkp+self.rop+self.rtp)
        self.refreshment_price.set("RS."+(str(self.totalrefreshment_price)))
        self.r_tax=round(self.totalrefreshment_price*0.28)
        self.refreshment_tax.set("RS."+(str(self.r_tax)))
        self.total_bill=float(self.totalcosmetic_price+self.totalgrocery_price+self.totalrefreshment_price+self.c_tax+self.g_tax+self.r_tax)
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to GCM retail")
        self.txtarea.insert(END,f"\n************************************")
        self.txtarea.insert(END,f"\nBill Number:{self.billno.get()}")
        self.txtarea.insert(END,f"\nCustomer Name:{self.cname.get()}")
        self.txtarea.insert(END,f"\nPhone Number:{self.cphn.get()}")
        self.txtarea.insert(END,f"\n************************************")
        self.txtarea.insert(END,f"\n Product\t\tQTY\t  Price")
        self.txtarea.insert(END,f"\n************************************")
    def bill_area(self):
        
        if self.cname.get()==""or self.cphn.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif len(self.cphn.get())!=10:
            messagebox.showerror("Error","phone digit should be 10")        
        elif self.cosmetic_price.get()=="RS.0.0"and self.grocery_price.get()=="RS.0.0"and self.refreshment_price.get()=="RS.0.0":
            messagebox.showerror("Error","No product purchased")
        else:
            self.welcome_bill()
        #===cosmetics
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\nSoap\t\t{self.soap.get()}\t  {self.csp}")    
            if self.facewash.get()!=0:
                self.txtarea.insert(END,f"\nFacewash\t\t{self.facewash.get()}\t  {self.fwp}")    
            if self.facecream.get()!=0:
                self.txtarea.insert(END,f"\nFacecream\t\t{self.facecream.get()}\t  {self.fcp}")    
            if self.hairgel.get()!=0:
                self.txtarea.insert(END,f"\nHairgel\t\t{self.hairgel.get()}\t  {self.hgp}")    
            if self.hairspray.get()!=0:
                self.txtarea.insert(END,f"\nHairspray\t\t{self.hairspray.get()}\t  {self.hsp}")    
            if self.bodylotion.get()!=0:
                self.txtarea.insert(END,f"\nBodylotion\t\t{self.bodylotion.get()}\t  {self.blp}")    
        #===groceries
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\nWheat\t\t{self.wheat.get()}\t  {self.gwp}")    
            if self.oil.get()!=0:
                self.txtarea.insert(END,f"\nOil\t\t{self.oil.get()}\t  {self.gop}")    
            if self.cereals.get()!=0:
                self.txtarea.insert(END,f"\nCereals\t\t{self.cereals.get()}\t  {self.gcp}")    
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\nTea\t\t{self.tea.get()}\t  {self.gtp}")    
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\nSuger\t\t{self.sugar.get()}\t  {self.gsp}")    
            if self.rice.get()!=0:
               self.txtarea.insert(END,f"\nRice\t\t{self.rice.get()}\t  {self.grp}")    
        #===refreshment
            if self.coke.get()!=0:
               self.txtarea.insert(END,f"\nCoke\t\t{self.coke.get()}\t  {self.rcp}")    
            if self.sprite.get()!=0:
               self.txtarea.insert(END,f"\nSprite\t\t{self.sprite.get()}\t  {self.rsp}")    
            if self.redbull.get()!=0:
               self.txtarea.insert(END,f"\nRedbull\t\t{self.redbull.get()}\t  {self.rrp}")    
            if self.kitkat.get()!=0:
               self.txtarea.insert(END,f"\nKitkat\t\t{self.kitkat.get()}\t  {self.rkp}")    
            if self.sofit.get()!=0:
               self.txtarea.insert(END,f"\nSofit\t\t{self.sofit.get()}\t  {self.rop}")    
            if self.thumbsup.get()!=0:
               self.txtarea.insert(END,f"\nThumbsup\t\t{self.thumbsup.get()}\t  {self.rtp}")    
            self.txtarea.insert(END,f"\n------------------------------------")
            if self.cosmetic_tax.get()!="RS.0":
               self.txtarea.insert(END,f"\nCosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="RS.0":
               self.txtarea.insert(END,f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.refreshment_tax.get()!="RS.0":
               self.txtarea.insert(END,f"\nRefreshment Tax\t\t\t{self.refreshment_tax.get()}")
            self.txtarea.insert(END,f"\n------------------------------------")
            self.txtarea.insert(END,f"\nTotal Amount\t\t\t{self.total_bill}")
            self.txtarea.insert(END,f"\n------------------------------------")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("save bill","do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get("1.0",END)
            r1=open("E:/bills/abc/"+str(self.billno.get())+".txt","w")
            r1.write(self.bill_data)
            r1.close()
            messagebox.showinfo("saved",f"Bill no:{self.billno.get()}saved successfully")
        else:
            return 
        add_employee = ("INSERT INTO bill"
        "(name, phone, billno, soap,facewash,facecream,hairspray,hairgel,bodylotion,wheat,oil,cereal,tea,suger,rice,coke,sprite,redbull,kitkat,sofit,thumbsup)"
        "VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s)")
        data_employee = (self.cname.get(), self.cphn.get(),self.billno.get(),self.soap.get(),self.facewash.get(),self.facecream.get(),self.hairspray.get(),self.hairgel.get(),self.bodylotion.get(),self.wheat.get(),self.oil.get(),self.cereals.get(),self.tea.get(),self.sugar.get(),self.rice.get(),self.coke.get(),self.sprite.get(),self.redbull.get(),self.kitkat.get(),self.sofit.get(),self.thumbsup.get())
        self.cursor.execute(add_employee, data_employee)
        self.cnx.commit()

    def find_bill(self):
        present="no"
        for i in os.listdir("E:/bills/abc/"):
            if i.split('.')[0]==self.billno.get():
                r1=open(f"E:/bills/abc/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in r1:
                    self.txtarea.insert(END,d)
                r1.close()
                present="yes"
        if present=="no": 
            messagebox.showerror("error","invalid bill no")  
    def clear_data(self):
        op=messagebox.askyesno("clear","do you really want to clear screen?")
        if op>0:
            self.soap.set(0)
            self.facewash.set(0)
            self.facewash.set(0)
            self.facecream.set(0)
            self.hairgel.set(0)
            self.hairspray.set(0)
            self.bodylotion.set(0)
        #=========groceries====
            self.wheat.set(0)
            self.oil.set(0)
            self.cereals.set(0)
            self.rice.set(0)
            self.tea.set(0)
            self.sugar.set(0)
        #========refreshments=====
            self.coke.set(0)
            self.sprite.set(0)
            self.redbull.set(0)
            self.kitkat.set(0)
            self.sofit.set(0)
            self.thumbsup.set(0)
        #========total product price &tax variables
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.refreshment_price.set("")
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.refreshment_tax.set("")
        #=======customer=======
            self.cname.set("")
            self.cphn.set("")
            self.billno.set("")
            x=random.randint(1000,9999)
            self.billno.set(str(x))
            self.searchbill.set("")
            self.welcome_bill()
    def exit(self):
        op=messagebox.askyesno("exit","Do you really want to exit?") 
        if op>0:
            self.root.destroy()    



root=Tk()
obj=bill_app(root)
root.mainloop() 
        
