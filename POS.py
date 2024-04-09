from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
import sqlite3
import tempfile
import os
import tkinter.messagebox
class POS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("POS (Inventory Management System)")
        self.root.config(bg="White")
        self.input_value = True

        self.burger1 = ImageTk.PhotoImage(file="images/burger1.png")
        self.burger2 = ImageTk.PhotoImage(file="images/burger2.png")
        self.burger3 = ImageTk.PhotoImage(file="images/burger3.png")
        self.fries1 = ImageTk.PhotoImage(file="images/fries1.png")
        self.fries2 = ImageTk.PhotoImage(file="images/fries2.png")
        self.fries3 = ImageTk.PhotoImage(file="images/fries3.png")
        
        self.coffee1 = ImageTk.PhotoImage(file="images/coffee1.png")
        self.coffee2 = ImageTk.PhotoImage(file="images/coffee2.png")
        self.coffee3 = ImageTk.PhotoImage(file="images/coffee3.png")
        self.icecream1 = ImageTk.PhotoImage(file="images/icecream1.png")
        self.icecream2 = ImageTk.PhotoImage(file="images/icecream2.png")
        self.icecream3 = ImageTk.PhotoImage(file="images/icecream3.png")
        
        self.pizza1 = ImageTk.PhotoImage(file="images/pizza1.png")
        self.pizza2 = ImageTk.PhotoImage(file="images/pizza2.png")
        self.pizza3 = ImageTk.PhotoImage(file="images/pizza3.png")
        self.sandwich1 = ImageTk.PhotoImage(file="images/sandwich1.png")
        self.sandwich2 = ImageTk.PhotoImage(file="images/sandwich2.png")
        self.sandwich3 = ImageTk.PhotoImage(file="images/sandwich3.png")
        
        
        
        

        global operator
        operator=""
        Change_input = StringVar()
        Cash_input = StringVar()
        Tax_input = StringVar()
        SubTotal_input = StringVar()
        Total_input = StringVar()
        Item_input = StringVar()
        Qty_input = StringVar()
        Amount_input = StringVar()
        Choice_input = StringVar()
        Cash_input = StringVar()
        
        
        

        MainFrame = Frame(self.root, bg='cadetblue')
        MainFrame.grid(padx=8,pady=5)

        ButtonFrame = Frame(MainFrame, bd=5, width=1350, height=160, padx=4, pady=4, bg='cadetblue', relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=5, width=1300, height=400, padx=5, bg='cadetblue', relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeftCover = LabelFrame(DataFrame, bd=5, width=800, height=300, pady=2, relief=RIDGE,
                                        bg='cadetblue', font=('arial',12,'bold'),text="Point Of Sale")
        DataFrameLeftCover.pack(side=LEFT)

        ChangeButtonFrame = Frame(DataFrameLeftCover, bd=5, width=300, height=460, pady=5, relief=RIDGE)
        ChangeButtonFrame.pack(side=LEFT,padx=4)

        ReceitFrame = Frame(DataFrameLeftCover, bd=5, width=200, height=400, pady=5,padx=1, relief=RIDGE)
        ReceitFrame.pack(side=RIGHT,padx=0)

        FoodItemFrame = LabelFrame(DataFrame, bd=5, width=450, height=300, padx=5, pady=2,relief=RIDGE,
                                   bg='cadetblue', font=('arial', 12, 'bold'),text="Items",)
        FoodItemFrame.pack(side=RIGHT)

        CalFrame = Frame(ButtonFrame, bd=5, width=432, height=140, relief=RIDGE)
        CalFrame.grid(row=0, column=0,padx=5)

        ChangeFrame = Frame(ButtonFrame, bd=5, width=500, height=140, pady=2, relief=RIDGE)
        ChangeFrame.grid(row=0, column=1,padx=5)

        RemoveFrame = Frame(ButtonFrame, bd=5, width=400, height=140, pady=4, relief=RIDGE)
        RemoveFrame.grid(row=0, column=2,padx=5)
        
        #==================Function calls=====================
        def iprint():
            q=self.txtReceit.get("1.0", "end-1c")
            print(q)
            filename = tempfile.mktemp(".txt")
            open(filename,"w").write(q)
            os.startfile(filename,"print")
            
        def btnClearDisplay():
            global operator
            operator = ""
            Change_input.set("")
            Cash_input.set("0")
            Tax_input.set("")
            SubTotal_input.set("")
            Total_input.set("")
            for i in self.POS_record.get_children():
                self.POS_record.delete(i)
                
        def change():
            Change_input.set("")
            Cash_input.set("0")
                
        def delete():
            ItemCost=0.0
            Tax = 1
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child, "values")[2])
            SubTotal_input.set(str('₹%.2f' %(ItemCost)))
            Tax_input.set(str('₹%.2f'%((ItemCost * Tax)/100)))
            Total_input.set(str('₹%.2f' %((ItemCost) + ((ItemCost * Tax)/100))))
            selected_item=(self.POS_record.selection()[0])
            self.POS_record.delete(selected_item)
            giveChange()
            
        def giveChange():
            ItemCost = 0.0
            Tax = 1
            CashInput = float(Cash_input.get())
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child, "values")[2])
            Change_input.set(str('₹%.2f' %(CashInput-((ItemCost) + ((ItemCost * Tax)/100)))))
            if (Cash_input.get() =="0"):
                Change_input.set("")
                Method_of_Pay()
                
        def Method_of_Pay():
            if (Choice_input.get() == "Cash"):
                self.txtCost.focus()
                Cash_input.set("")
            elif (Choice_input.get()==""):
                Cash_input.set("0")
                Change_input.set("")
                
                        

        #===========calculatorFrame widget=======
        self.lblSubTotal = Label(CalFrame, font=('arial', 14, 'bold'), text="Sub Total", bd=5)
        self.lblSubTotal.grid(row=0,column=0,sticky=W, padx=5)
        self.txtSubTotal = Entry(CalFrame, font=('arial', 14, 'bold'),bd=2, width=24, justify='left',textvariable=SubTotal_input)
        self.txtSubTotal.grid(row=0,column=1,sticky=W)

        self.lblTax = Label(CalFrame, font=('arial', 14, 'bold'), text="Tax", bd=5)
        self.lblTax.grid(row=1,column=0,sticky=W, padx=5)
        self.txtTax = Entry(CalFrame, font=('arial', 14, 'bold'),bd=2, width=24, justify='left',textvariable=Tax_input)
        self.txtTax.grid(row=1,column=1,sticky=W)

        self.lblTotal = Label(CalFrame, font=('arial', 14, 'bold'), text="Total", bd=5)
        self.lblTotal.grid(row=2,column=0,sticky=W, padx=5)
        self.txtTotal = Entry(CalFrame, font=('arial', 14, 'bold'),bd=2, width=24, justify='left',textvariable=Total_input)
        self.txtTotal.grid(row=2,column=1,sticky=W)

         #===========calculatorFrame widget=======
        self.lblMoP = Label(ChangeFrame, font=('arial', 14, 'bold'), text="Method of Payment", bd=2)
        self.lblMoP.grid(row=0,column=0,sticky=W, padx=2)
        self.cboMoP = ttk.Combobox(ChangeFrame,width=36, font=('arial', 14, 'bold'), state='readonly',justify='right',textvariable=Choice_input)
        self.cboMoP['values'] = ('','Cash', 'Visa Card', 'Master Card')
        self.cboMoP.current(0)
        self.cboMoP.grid(row=0,column=1)

        self.lblCost = Label(ChangeFrame, font=('arial', 14, 'bold'), text="Cost", bd=5)
        self.lblCost.grid(row=1,column=0,sticky=W, padx=2)
        self.txtCost = Entry(ChangeFrame, font=('arial', 14, 'bold'),bd=2, width=38, justify='right',textvariable=Cash_input)
        self.txtCost.grid(row=1,column=1,pady=5)
        self.txtCost.insert(0,"0")

        self.lblChange= Label(ChangeFrame, font=('arial', 14, 'bold'), text="Change", bd=5)
        self.lblChange.grid(row=2,column=0,sticky=W, padx=2)
        self.txtChange = Entry(ChangeFrame, font=('arial', 14, 'bold'),bd=2, width=38, justify='right',textvariable=Change_input)
        self.txtChange.grid(row=2,column=1,pady=5,sticky=W)
        #===================function===========
        def FreshVeggie():
            ItemCost = 379
            Tax = 1
            self.POS_record.insert("",tk.END, values=("FreshVeggie","1","379"))
            self.txtReceit.insert(END,("Pizza1" +"\t\t\t" + "1" + "\t\t\t" + "379" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-379)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-379)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-379) + ((ItemCost-300)* Tax)/100))) 
        
        def NonVeg():
            ItemCost = 599
            Tax = 1
            self.POS_record.insert("",tk.END, values=("NonVeg","1","599"))
            self.txtReceit.insert(END,("NonVeg" +"\t\t\t" + "1" + "\t\t\t" + "599" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-599)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-599)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-599) + ((ItemCost-200)* Tax)/100))) 
        
        def Margherita():
            ItemCost = 250
            Tax = 1
            self.POS_record.insert("",tk.END, values=("Margherita","1","250"))
            self.txtReceit.insert(END,("Margherita" +"\t\t\t" + "1" + "\t\t\t" + "250" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-250)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-250)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-250) + ((ItemCost-250)* Tax)/100))) 
                
        def ChanaSandwich():
            ItemCost = 50
            Tax = 1
            self.POS_record.insert("",tk.END, values=("ChanaSandwich","1","50"))
            self.txtReceit.insert(END,("ChanaSandwich" +"\t\t\t" + "1" + "\t\t\t" + "50" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-50)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-50)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-50) + ((ItemCost-50)* Tax)/100))) 
        
        def Vegsandwich():
            ItemCost = 30
            Tax = 1
            self.POS_record.insert("",tk.END, values=("Vegsandwich","1","30"))
            self.txtReceit.insert(END,("Vegsandwich" +"\t\t\t" + "1" + "\t\t\t" + "30" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-30)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-30)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-30) + ((ItemCost-30)* Tax)/100))) 
        
        def GrillSandwich():
            ItemCost = 70
            Tax = 1
            self.POS_record.insert("",tk.END, values=("GrillSandwich","1","70"))
            self.txtReceit.insert(END,("GrillSandwich" +"\t\t\t" + "1" + "\t\t\t" + "70" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-70)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-70)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-70) + ((ItemCost-70)* Tax)/100))) 
        #=============row 2=============
        def Cappuccino():
            ItemCost = 200
            Tax = 1
            self.POS_record.insert("",tk.END, values=("Cappuccino","1","200"))
            self.txtReceit.insert(END,("Cappuccino" +"\t\t\t" + "1" + "\t\t\t" + "200" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-200)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-200)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-200) + ((ItemCost-200)* Tax)/100))) 
        
        def HotCoffee():
            ItemCost = 250
            Tax = 1
            self.POS_record.insert("",tk.END, values=("HotCoffee","1","250"))
            self.txtReceit.insert(END,("HotCoffee" +"\t\t\t" + "1" + "\t\t\t" + "250" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-250)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-250)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-250) + ((ItemCost-250)* Tax)/100))) 
        
        def ColdCoffee():
            ItemCost = 270
            Tax = 1
            self.POS_record.insert("",tk.END, values=("ColdCoffee","1","270"))
            self.txtReceit.insert(END,("ColdCoffee" +"\t\t\t" + "1" + "\t\t\t" + "270" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-270)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-270)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-270) + ((ItemCost-270)* Tax)/100))) 
                
        def Vanilla():
            ItemCost = 25
            Tax = 1
            self.POS_record.insert("",tk.END, values=("Vanilla","1","25"))
            self.txtReceit.insert(END,("Vanilla" +"\t\t\t" + "1" + "\t\t\t" + "25" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-25)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-25)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-25) + ((ItemCost-25)* Tax)/100))) 
        
        def Strawberry():
            ItemCost = 30
            Tax = 1
            self.POS_record.insert("",tk.END, values=("Strawberry","1","30"))
            self.txtReceit.insert(END,("Strawberry" +"\t\t\t" + "1" + "\t\t\t" + "30" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-30)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-30)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-30) + ((ItemCost-30)* Tax)/100))) 
        
        def Chocolate():
            ItemCost = 40
            Tax = 1
            self.POS_record.insert("",tk.END, values=("Chocolate","1","40"))
            self.txtReceit.insert(END,("Chocolate" +"\t\t\t" + "1" + "\t\t\t" + "40" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-40)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-40)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-40) + ((ItemCost-40)* Tax)/100))) 
                
        #==================row 1==============================
        def VegCrispy():
            ItemCost = 25
            Tax = 1
            self.POS_record.insert("",tk.END, values=("VegCrispy","1","25"))
            self.txtReceit.insert(END,("VegCrispy" +"\t\t\t" + "1" + "\t\t\t" + "25" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-25)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-25)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-25) + ((ItemCost-25)* Tax)/100))) 
        
        def AlooTikki():
            ItemCost = 39
            Tax = 1
            self.POS_record.insert("",tk.END, values=("AlooTikki","1","39"))
            self.txtReceit.insert(END,("AlooTikki" +"\t\t\t" + "1" + "\t\t\t" + "39" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-39)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-39)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-39) + ((ItemCost-39)* Tax)/100))) 
                
        def VegMexican():
            ItemCost = 79
            Tax = 1
            self.POS_record.insert("",tk.END, values=("VegMexican","1","79"))
            self.txtReceit.insert(END,("VegMexican" +"\t\t\t" + "1" + "\t\t\t" + "79" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-79)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-79)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-79) + ((ItemCost-79)* Tax)/100))) 
        
        def CheeseFries():
            ItemCost = 50
            Tax = 1
            self.POS_record.insert("",tk.END, values=("CheeseFries","1","50"))
            self.txtReceit.insert(END,("CheeseFries" +"\t\t\t" + "1" + "\t\t\t" + "50" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-50)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-50)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-50) + ((ItemCost-50)* Tax)/100))) 
                
        def CheesyFries():
            ItemCost = 99
            Tax = 1
            self.POS_record.insert("",tk.END, values=("CheesyFries","1","99"))
            self.txtReceit.insert(END,("CheesyFries" +"\t\t\t" + "1" + "\t\t\t" + "99" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-99)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-99)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-99) + ((ItemCost-99)* Tax)/100))) 
        
        def MasalaFries():
            ItemCost = 90
            Tax = 1
            self.POS_record.insert("",tk.END, values=("MasalaFries","1","90"))
            self.txtReceit.insert(END,("MasalaFries" +"\t\t\t" + "1" + "\t\t\t" + "90" + "\n"))
            for child in self.POS_record.get_children():
                ItemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_input.set(str('₹%.2f'%(ItemCost-90)))
                Tax_input.set(str('₹%.2f' %(((ItemCost-90)*Tax)/100))) 
                Total_input.set(str('₹%.2f' %((ItemCost-90) + ((ItemCost-90)* Tax)/100))) 
        
        
        
        
        
        def btnclick(numbers):
            global operator
            operator = operator + str(numbers)
            Cash_input.set(operator)
            
        #===========button,pay,print,remove=======
        self.btnPay = Button(RemoveFrame, padx=2, font=('arial',15,'bold'),text="Pay",width=10,height=1,bd=2,
                             command=giveChange)
        self.btnPay.grid(row=0,column=0,padx=4,pady=2)

        self.btnPrint = Button(RemoveFrame, padx=2, font=('arial',15,'bold'),text="Print",width=10,height=1,bd=2,
                               command=iprint)
        self.btnPrint.grid(row=1,column=1,padx=4,pady=2)

        self.btnReset = Button(RemoveFrame, padx=2, font=('arial',15,'bold'),text="Reset",width=10,height=1,bd=2,
                               command=btnClearDisplay)
        self.btnReset.grid(row=1,column=0,padx=4,pady=2)

        self.btnRemoveItem = Button(RemoveFrame, padx=2, font=('arial',15,'bold'),text="Remove Item",width=10,height=1,bd=2,
                                    command=delete)
        self.btnRemoveItem.grid(row=0,column=1,padx=4,pady=2)
        
        #=================Treeview=text widget=========
        scroll_y = Scrollbar(ReceitFrame, orient=VERTICAL)
        self.POS_record = ttk.Treeview(ReceitFrame, height=20, columns=("Item","QTY","Amount"),
                                       yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.POS_record.heading("Item", text="Item")
        self.POS_record.heading("QTY", text="QTY")
        self.POS_record.heading("Amount", text="Amount")
        
        self.POS_record['show'] = 'headings'
        
        self.POS_record.column("Item",width=120)
        self.POS_record.column("QTY", width=100)
        self.POS_record.column("Amount", width=100)
        
        self.POS_record.pack(fill=BOTH, expand=2)
        self.POS_record.bind("<ButtonRelease-1>")
        
        self.txtReceit = Text(ReceitFrame, width=80, height=1,font=('arial', 5, 'bold'))
        self.txtReceit.pack()
        
        self.txtReceit.insert(END, "Item\t\t\t\t QTY\t\t\t Amount\t\n")
        
        
        #============button calculate==========
        self.btn7 = Button(ChangeButtonFrame, padx=13,pady=22, font=('arial',20,'bold'),text="7",bd=8,
                           command=lambda:btnclick(7),bg='cadetblue').grid(row=0,column=0)
        self.btn8 = Button(ChangeButtonFrame, padx=13,pady=22, font=('arial',20,'bold'),text="8",bd=8,
                           command=lambda:btnclick(8),bg='cadetblue').grid(row=0,column=1)
        self.btn9 = Button(ChangeButtonFrame, padx=13,pady=22, font=('arial',20,'bold'),text="9",bd=8,
                           command=lambda:btnclick(9),bg='cadetblue').grid(row=0,column=2)
        #=========2 row=============
        self.btn4 = Button(ChangeButtonFrame, padx=13,pady=22, font=('arial',20,'bold'),text="4",bd=8,
                           command=lambda:btnclick(4),bg='cadetblue').grid(row=1,column=0)
        self.btn5 = Button(ChangeButtonFrame, padx=13,pady=22, font=('arial',20,'bold'),text="5",bd=8,
                           command=lambda:btnclick(5),bg='cadetblue').grid(row=1,column=1)
        self.btn6 = Button(ChangeButtonFrame, padx=13,pady=22, font=('arial',20,'bold'),text="6",bd=8,
                           command=lambda:btnclick(6),bg='cadetblue').grid(row=1,column=2)
        #===========3 row==========
        self.btn1 = Button(ChangeButtonFrame, padx=13,pady=22, font=('arial',20,'bold'),text="1",bd=8,
                           command=lambda:btnclick(1),bg='cadetblue').grid(row=2,column=0)
        self.btn2 = Button(ChangeButtonFrame, padx=13,pady=22, font=('arial',20,'bold'),text="2",bd=8,
                           command=lambda:btnclick(2),bg='cadetblue').grid(row=2,column=1)
        self.btn3 = Button(ChangeButtonFrame, padx=13,pady=22, font=('arial',20,'bold'),text="3",bd=8,
                           command=lambda:btnclick(3),bg='cadetblue').grid(row=2,column=2)
        #=========4 row=================
        self.btn0 = Button(ChangeButtonFrame, padx=13,pady=22, font=('arial',20,'bold'),text="0",bd=8,
                           command=lambda:btnclick(0),bg='cadetblue').grid(row=3,column=0)
        self.btnDot = Button(ChangeButtonFrame, padx=13,pady=22, font=('arial',20,'bold'),text=".",bd=8,
                           command=lambda:btnclick('.'),bg='cadetblue').grid(row=3,column=1)
        self.btnc = Button(ChangeButtonFrame, padx=13,pady=22, font=('arial',20,'bold'),text="c",bd=8,
                           bg='cadetblue',command=change).grid(row=3,column=2)
       
       
        #======================buttton,pay,print,remove=======
        self.btnburger1 = Button(FoodItemFrame,padx=2, image=self.burger1, width=104, height=104, bd=2,
                                 command=VegCrispy)
        self.btnburger1.grid(row=0,column=0,padx=4,pady=2)
       
        self.btnburger2 = Button(FoodItemFrame,padx=2, image=self.burger2, width=104, height=104, bd=2,
                                 command=AlooTikki)
        self.btnburger2.grid(row=0,column=1,padx=4,pady=2)
       
        self.btnburger3 = Button(FoodItemFrame,padx=2, image=self.burger3, width=104, bd=2,
                                 command=VegMexican)
        self.btnburger3.grid(row=0,column=2,padx=4,pady=2)
       
        self.btnfries1 = Button(FoodItemFrame,padx=2, image=self.fries1, width=104, bd=2,
                                command=CheeseFries)
        self.btnfries1.grid(row=0,column=3,padx=4,pady=2)
       
        self.btnfries2 = Button(FoodItemFrame,padx=2, image=self.fries2, width=104, bd=2,
                                command=CheesyFries)
        self.btnfries2.grid(row=0,column=4,padx=4,pady=2)
       
        self.btnfries3 = Button(FoodItemFrame,padx=2, image=self.fries3, width=104, bd=2,
                                command=MasalaFries)
        self.btnfries3.grid(row=0,column=5,padx=4,pady=2)
        #=======================================
        self.btncoffee1 = Button(FoodItemFrame,padx=2, image=self.coffee1, width=104, height=104, bd=2,
                                 command=Cappuccino)
        self.btncoffee1.grid(row=1,column=0,padx=4,pady=2)
       
        self.btncoffee2 = Button(FoodItemFrame,padx=2, image=self.coffee2, width=104, height=104, bd=2,
                                 command=HotCoffee)
        self.btncoffee2.grid(row=1,column=1,padx=4,pady=2)
       
        self.btncoffee3 = Button(FoodItemFrame,padx=2, image=self.coffee3, width=104, bd=2,
                                 command=ColdCoffee)
        self.btncoffee3.grid(row=1,column=2,padx=4,pady=2)
       
        self.btnicecream1 = Button(FoodItemFrame,padx=2, image=self.icecream1, width=104, bd=2,
                                   command=Vanilla)
        self.btnicecream1.grid(row=1,column=3,padx=4,pady=2)
       
        self.btnicecream2 = Button(FoodItemFrame,padx=2, image=self.icecream2, width=104, bd=2,
                                   command=Strawberry)
        self.btnicecream2.grid(row=1,column=4,padx=4,pady=2)
       
        self.btnicecream3 = Button(FoodItemFrame,padx=2, image=self.icecream3, width=104, bd=2,
                                   command=Chocolate)
        self.btnicecream3.grid(row=1,column=5,padx=4,pady=2)
        #=====================
        self.btnpizza1 = Button(FoodItemFrame,padx=2, image=self.pizza1, width=104, height=104, bd=2,
                                command=FreshVeggie)
        self.btnpizza1.grid(row=2,column=0,padx=4,pady=2)
       
        self.btnpizza2 = Button(FoodItemFrame,padx=2, image=self.pizza2, width=104, height=104, bd=2,
                                command=NonVeg)
        self.btnpizza2.grid(row=2,column=1,padx=4,pady=2)
       
        self.btnpizza3 = Button(FoodItemFrame,padx=2, image=self.pizza3, width=104, bd=2,
                                command=Margherita)
        self.btnpizza3.grid(row=2,column=2,padx=4,pady=2)
       
        self.btnsandwich1 = Button(FoodItemFrame,padx=2, image=self.sandwich1, width=104, bd=2,
                                   command=ChanaSandwich)
        self.btnsandwich1.grid(row=2,column=3,padx=4,pady=2)
       
        self.btnsandwich2 = Button(FoodItemFrame,padx=2, image=self.sandwich2, width=104, bd=2,
                                   command=Vegsandwich)
        self.btnsandwich2.grid(row=2,column=4,padx=4,pady=2)
       
        self.btnsandwich3 = Button(FoodItemFrame,padx=2, image=self.sandwich3, width=104, bd=2,
                                   command=GrillSandwich)
        self.btnsandwich3.grid(row=2,column=5,padx=4,pady=2)
       
        

    

if __name__=="__main__":    
   root=Tk()
   obj=POS(root)
   root.mainloop()


  