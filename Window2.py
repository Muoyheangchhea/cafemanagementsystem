
from tkinter import *
import random
from datetime import datetime
from tkinter import messagebox
import sys
import mysql.connector
#==========connect to mysql database==========
mydb = mysql.connector.connect(
    host = "localhost", 
    user = 'root',
    password = "Heang@345", 
    database = "sunshine_cafe"
)
#===========================================
#==========set up window=====================
class Window2:
    def __init__(self, win):
        self.win = win
        self.win.geometry("1320x750+0+0")
        self.win.title("Sunshine Cafe Management System")

        self.title_label = Label(self.win, text= "Sunshine Cafe Management System", font = ("Arial", 35, "bold"), bg = "lightpink", bd= 8, relief = GROOVE)
        self.title_label.pack(side = TOP, fill = X)


        #================ Variables ===================
        bill_no = random.randint(100, 9999)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)

        calc_var = StringVar()
        cust_nm = StringVar()
        cust_cot = StringVar()
        date_pr = StringVar()
        date_pr.set(datetime.now())
        #==============================================


        #=================Entry======================================

        self.entry_frame = LabelFrame(self.win, text ="Customer Info", background = "lightpink", font = ("Arial", 15, "bold"), bd = 7, relief = GROOVE)
        self.entry_frame.place(x = 20, y = 95, width = 450, height = 542)

        self.bill_no_lbl= Label(self.entry_frame, text = "Bill Number", font =("Arial", 15), bg = "lightpink")
        self.bill_no_lbl.grid(row= 0, column = 0, padx = 2, pady = 2)

        self.bill_no_ent = Entry(self.entry_frame,bd = 5, font= ("Arial", 15), textvariable = bill_no_tk)
        self.bill_no_ent.grid(row = 0, column = 1, padx = 2, pady = 2)
        self.bill_no_ent.config(state = "disabled")

        self.cust_nm_lbl = Label(self.entry_frame, text = "Customer name", font =("Arial", 15), bg = "lightpink")
        self.cust_nm_lbl.grid(row= 1, column = 0, padx = 2, pady = 2)

        self.cust_nm_ent = Entry(self.entry_frame,bd = 5, textvariable = cust_nm, font= ("Arial", 15))
        self.cust_nm_ent.grid(row = 1, column =1, padx = 2, pady = 2)

        self.cust_cot_lbl = Label(self.entry_frame, text = "Customer contact", font =("Arial", 15), bg = "lightpink")
        self.cust_cot_lbl.grid(row= 2, column = 0, padx = 2, pady = 2)

        self.cust_cot_ent = Entry(self.entry_frame,bd = 5, textvariable =cust_cot , font= ("Arial", 15))
        self.cust_cot_ent.grid(row = 2, column =1, padx = 2, pady = 2)

        self.date_lbl = Label(self.entry_frame, text = "Date", font =("Arial", 15), bg = "lightpink")
        self.date_lbl.grid(row= 3, column = 0, padx = 2, pady = 2)

        self.date_ent = Entry(self.entry_frame,bd = 5, textvariable = date_pr, font= ("Arial", 15))
        self.date_ent.grid(row = 3, column =1, padx = 2, pady = 2)
        self.date_ent.config(state = "disabled")
     
        #========================Menu Variable=========================

        e_latte = IntVar()
        e_expresso = IntVar()
        e_iceamericano = IntVar()
        e_hotchoco= IntVar()
        e_straw = IntVar()
        e_greentea = IntVar()
        e_lemontea = IntVar()

        #===========================Menu label===================================


        food_frame = LabelFrame(self.win, background = "lightpink", text = "Menu", font = ("Arial", 15, "bold"), bd = 8, relief = GROOVE)
        food_frame.place(x = 575, y = 95, width = 280, height = 295)

        latte = Label(food_frame, text = "Latte", font = ("Arial", 15), bg = "lightpink")
        latte.grid(row =0, column = 0, sticky = W)
        text_latte = Entry(food_frame, font = ("Arial", 15), bd = 5, width = 8, textvariable = e_latte)
        text_latte.grid(row = 0, column = 1)

        expresso = Label(food_frame, text = "Expresso", font = ("Arial", 15), bg = "lightpink")
        expresso.grid(row =1, column = 0, sticky = W)
        text_expresso = Entry(food_frame, font = ("Arial", 15), bd = 5, width = 8, textvariable = e_expresso)
        text_expresso.grid(row = 1, column = 1)

        iceamericano = Label(food_frame, text = "Ice Americano", font = ("Arial", 15), bg = "lightpink")
        iceamericano.grid(row =2, column = 0, sticky = W)
        text_iceamericano = Entry(food_frame, font = ("Arial", 15), bd = 5, width = 8, textvariable = e_iceamericano)
        text_iceamericano.grid(row = 2, column = 1)

        hotchoco = Label(food_frame, text = "Hot Chocolate", font = ("Arial", 15), bg = "lightpink")
        hotchoco.grid(row =3, column = 0, sticky = W)
        text_hotchoco = Entry(food_frame, font = ("Arial", 15), bd = 5, width = 8, textvariable = e_hotchoco)
        text_hotchoco.grid(row = 3, column = 1)

        straw = Label(food_frame, text = "Strawberry Milk", font = ("Arial", 15), bg = "lightpink")
        straw.grid(row =4, column = 0, sticky = W)
        text_straw = Entry(food_frame, font = ("Arial", 15), bd = 5, width = 8, textvariable = e_straw)
        text_straw.grid(row = 4, column = 1)

        greentea = Label(food_frame, text = "Green Tea", font = ("Arial", 15), bg = "lightpink")
        greentea.grid(row =5, column = 0, sticky = W)
        text_greentea = Entry(food_frame, font = ("Arial", 15), bd = 5, width = 8, textvariable = e_greentea)
        text_greentea.grid(row = 5, column = 1)

        
        lemontea = Label(food_frame, text = "Lemon Tea", font = ("Arial", 15), bg = "lightpink")
        lemontea.grid(row =6, column = 0, sticky = W)
        text_lemontea = Entry(food_frame, font = ("Arial", 15), bd = 5, width = 8, textvariable = e_lemontea)
        text_lemontea.grid(row = 6, column = 1)


        #=============================================================
 
        #=====================functions=================
        

        def default_bill():
            self.bill_txt.insert(END, "\t\t\t\tSunshine Cafe")
            self.bill_txt.insert(END, "\nStreet 201R, Sangkat Kilometer 6, Khan Russey Keo, Phnom Penh, Cambodia")
            self.bill_txt.insert(END, "\n\t\t\tContact- +85577847664")
            self.bill_txt.insert(END, "\n============================================================================")
            self.bill_txt.insert(END, f"\nBill Number {bill_no_tk.get()}")
            self.total_btn.config(state = "disabled")
            self.save_btn.config(state = "disabled")

        def genbill():
            if cust_nm.get() == "" or cust_cot.get() == "":
                messagebox.showerror("Error!", "Please enter all the fields correctly!")
            else:
                self.total_btn.config(state = "normal")
                
                self.bill_txt.insert(END, f"\nCustomer Name: {cust_nm.get()} ")
                self.bill_txt.insert(END, f"\nCustomer Contact: {cust_cot.get()}")
                self.bill_txt.insert(END, f"\nDate: {date_pr.get()}")
                self.bill_txt.insert(END, "\n============================================================================")
                self.bill_txt.insert(END, "\nProduct Name\t\t    Quantity\t\t    Per Cost\t\t    Total")
                self.bill_txt.insert(END, "\n============================================================================")
                
                if e_latte.get() != 0:
                    self.bill_txt.insert(END, f"\nLatte\t\t    {e_latte.get()}\t\t    2$\t\t     {int(e_latte.get()) * 2}")
                if e_expresso.get() != 0:
                    self.bill_txt.insert(END, f"\nExpresso\t\t    {e_expresso.get()}\t\t    2$\t\t     {int(e_expresso.get()) * 2}")
                if e_iceamericano.get() != 0:
                    self.bill_txt.insert(END, f"\nIce Americano\t\t    {e_iceamericano.get()}\t\t    2$\t\t     {int(e_iceamericano.get()) * 2}")
                if e_hotchoco.get() != 0:
                    self.bill_txt.insert(END, f"\nHot Chocolate\t\t    {e_hotchoco.get()}\t\t    2$\t\t     {int(e_hotchoco.get()) * 2}")
                if e_straw.get() != 0:
                    self.bill_txt.insert(END, f"\nStrawberry Milk\t\t    {e_straw.get()}\t\t    3$\t\t     {int(e_straw.get()) * 3}")
                if e_greentea.get() != 0:
                    self.bill_txt.insert(END, f"\nGreen Tea\t\t    {e_greentea.get()}\t\t    3$\t\t     {int(e_greentea.get()) * 3}")
                if e_lemontea.get() != 0:
                    self.bill_txt.insert(END, f"\nLemon Tea\t\t    {e_lemontea.get()}\t\t    2$\t\t     {int(e_lemontea.get()) * 2}")
                else:
                    return None
                
        
        def total_func():
                self.save_btn.config(state = "normal")
                total_price = (e_latte.get()* 2) + ((e_expresso.get()) * 2) + ((e_iceamericano.get()) * 2) + ((e_hotchoco.get()) * 2) + ((e_greentea.get()) * 3) + ((e_straw.get()) * 3) + ((e_lemontea.get()) *2)
                self.bill_txt.insert(END, "\n============================================================================")
                self.bill_txt.insert(END, f"\t\t\t\t\t\tGrand Total: {total_price}$")
                self.bill_txt.insert(END, "\n============================================================================")
        
        def reset_func():
            cust_nm.set("")
            cust_cot.set("")
            e_latte.set("")
            e_expresso.set("")
            e_greentea.set("")
            e_hotchoco.set("")
            e_iceamericano.set("")
            e_lemontea.set("")
            e_straw.set("")
            self.bill_txt.delete("1.0", END)
            bill_no = random.randint(100, 9999)
            bill_no_tk = IntVar()
            bill_no_tk.set(bill_no)

            default_bill()

        def save_func():
            user_choice = messagebox.askyesno("Confirm?", f"Do you want to save the bill {bill_no_tk.get()}?", parent = self.win)
            if user_choice > 0:
                self.bill_content = self.bill_txt.get("1.0", END)
                if e_latte.get() != 0:
                        pd_name = "Latte"
                        qty = e_latte.get()
                        per = 2
                        price = e_latte.get() * 2

                if e_iceamericano.get() != 0:
                        pd_name = "Ice Americano"
                        qty = e_iceamericano.get()
                        per = 2
                        price = e_iceamericano.get() * 2
                if e_hotchoco.get() != 0:
                        pd_name = "Hot chocolate"
                        qty = e_hotchoco.get()
                        per = 2
                        price = e_hotchoco.get() * 2
                if e_expresso.get() != 0:
                        pd_name = "Expresso"
                        qty = e_expresso.get()
                        per = 2
                        price = e_expresso.get() * 2
                if e_straw.get() != 0:
                        pd_name = "Strawberry Milk"
                        qty = e_straw.get()
                        per = 3
                        price = e_straw.get() * 3
                if e_greentea.get() != 0:
                        pd_name = "Green Tea"
                        qty = e_greentea.get()
                        per = 3
                        price = e_greentea.get() * 3
                if e_lemontea.get() != 0:
                        pd_name = "Lemon Tea"
                        qty = e_lemontea.get()
                        per = 2
                        price = e_lemontea.get() * 2
                else:
                     None
                Num = bill_no_tk.get()
                name = cust_nm.get()
                date = date_pr.get()
                contact = cust_cot.get()
                total_price = (e_latte.get()* 2) + ((e_expresso.get()) * 2) + ((e_iceamericano.get()) * 2) + ((e_hotchoco.get()) * 2) + ((e_greentea.get()) * 3) + ((e_straw.get()) * 3) + ((e_lemontea.get()) *2)
                my_cursor = mydb.cursor()
                my_cursor.execute("""INSERT INTO customer_list(ID, name, contact, date, product, quantity, per_cost, price, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (Num, name, contact, date, pd_name, qty, per, price, total_price))
                mydb.commit()
                try:
                    con = open(f"{sys.path[0]}/customer invoice/" + str(bill_no_tk.get()) + ".txt", "w")
                except Exception as e:
                    messagebox.showerror("Error!", f"Error due to {e}", parent = self.win)
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Successful", f"Bill {bill_no_tk.get()} has been saved successfully!", parent = self.win)
                reset_func()
            else:
                return



        #==========================Function Button=================

        self.button_frame = LabelFrame(self.entry_frame,bd = 8, text = "Options", bg = "lightpink", font = ("Arial", 15,"bold"))
        self.button_frame.place(x = 10, y = 200, width = 350, height = 215)

        self.generate_btn = Button(self.button_frame, bd = 5, text = "Generate", font = ("Arial", 12), width = 15, height = 3, bg = "lightblue", command = genbill)
        self.generate_btn.grid(row = 0, column = 0, padx = 4, pady = 4)
        
        self.total_btn = Button(self.button_frame, bd = 5, text = "Total", font = ("Arial", 12), width = 15, height = 3, bg = "lightblue",command = total_func)
        self.total_btn.grid(row = 1, column = 0, padx = 4, pady = 4)

        self.reset_btn = Button(self.button_frame, bd = 5, text = "Reset",font = ("Arial", 12), width = 15, height = 3, bg = "lightblue", command = reset_func)
        self.reset_btn.grid(row = 0, column = 1, padx = 4, pady = 4)
        
        self.save_btn = Button(self.button_frame, bd = 5, text = "Save", font = ("Arial", 12), width = 15, height = 3, bg = "lightblue", command = save_func)
        self.save_btn.grid(row = 1, column = 1, padx = 4, pady = 4)


        #==============================================

        

        #=================Calculator Frame ============

        self.calc_frame = Frame(self.win, bd = 8, background = "lightpink", relief = GROOVE)
        self.calc_frame.place(x = 900, y = 95, width = 328, height = 295)

        self.num_ent = Entry(self.calc_frame, bd = 15, background = "lightpink", textvariable = calc_var, font = ("Arial", 15), width = 25, justify = "right")
        self.num_ent.grid(row = 0, column = 0, columnspan = 5)
        #======================================================


        #====================Calculator function================
        def press_btn(event):
            text = event.widget.cget("text")
            if text == "=":
                if calc_var.get().isdigit():
                    value = int(calc_var.get())
                else: 
                    try:
                        value = eval(self.num_ent.get())
                    except:
                        print("Error")
                calc_var.set(value)
                self.num_ent.update()
            elif text == "C":
                calc_var.set("")
            elif text == "DEL":
                self.num_ent.delete(len(calc_var.get())-1, "end")
            else:
                calc_var.set(calc_var.get() + text)
                self.num_ent.update()
        #=======================================================

        #=============calculator button=======================
        self.btn7 = Button(self.calc_frame, bg = 'lightblue', text = "7",bd = 8, width = 3, height = 1, font = ("Arial", 15) )
        self.btn7.grid(row = 1, column = 0, padx = 1, pady = 1)
        self.btn7.bind("<Button-1>", press_btn)
        
        self.btn8 = Button(self.calc_frame, bg = 'lightblue', text = "8",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btn8.grid(row = 1, column = 1, padx = 1, pady = 1)
        self.btn8.bind("<Button-1>", press_btn)

        self.btn9 = Button(self.calc_frame, bg = 'lightblue', text = "9",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btn9.grid(row = 1, column = 2, padx = 1, pady = 1)
        self.btn9.bind("<Button-1>", press_btn)

        self.btnmulti = Button(self.calc_frame, bg = 'lightblue', text = "*",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btnmulti.grid(row = 3, column = 3, padx = 1, pady = 1)
        self.btnmulti.bind("<Button-1>", press_btn)

        self.btn4 = Button(self.calc_frame, bg = 'lightblue', text = "4",bd = 8, width = 3, height = 1, font = ("Arial", 15) )
        self.btn4.grid(row = 2, column = 0, padx = 1, pady = 1)
        self.btn4.bind("<Button-1>", press_btn)

        self.btn5 = Button(self.calc_frame, bg = 'lightblue', text = "5",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btn5.grid(row = 2, column = 1, padx = 1, pady = 1)
        self.btn5.bind("<Button-1>", press_btn)

        self.btn6 = Button(self.calc_frame, bg = 'lightblue', text = "6",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btn6.grid(row = 2, column = 2, padx = 1, pady = 1)
        self.btn6.bind("<Button-1>", press_btn)

        self.btnsubs = Button(self.calc_frame, bg = 'lightblue', text = "-",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btnsubs.grid(row = 2, column = 3, padx = 1, pady = 1)
        self.btnsubs.bind("<Button-1>", press_btn)

        self.btn1= Button(self.calc_frame, bg = 'lightblue', text = "1",bd = 8, width = 3, height = 1, font = ("Arial", 15) )
        self.btn1.grid(row = 3, column = 0, padx = 1, pady = 1)
        self.btn1.bind("<Button-1>", press_btn)

        self.btn2 = Button(self.calc_frame, bg = 'lightblue', text = "2",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btn2.grid(row = 3, column = 1, padx = 1, pady =1)
        self.btn2.bind("<Button-1>", press_btn)

        self.btn3 = Button(self.calc_frame, bg = 'lightblue', text = "3",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btn3.grid(row = 3, column = 2, padx = 1, pady = 1)
        self.btn3.bind("<Button-1>", press_btn)

        self.btnadd = Button(self.calc_frame, bg = 'lightblue', text = "+",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btnadd.grid(row = 1, column = 3, padx = 1, pady = 1)
        self.btnadd.bind("<Button-1>", press_btn)

        self.btn0 = Button(self.calc_frame, bg = 'lightblue', text = "0",bd = 8, width = 3, height = 1, font = ("Arial", 15) )
        self.btn0.grid(row = 4, column = 1, padx = 1, pady = 1)
        self.btn0.bind("<Button-1>", press_btn)

        self.btnpoint = Button(self.calc_frame, bg = 'lightblue', text = ".",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btnpoint.grid(row = 3, column = 4, padx = 1, pady = 1)
        self.btnpoint.bind("<Button-1>", press_btn)

        self.btn_equal= Button(self.calc_frame, bg = 'lightblue', text = "=",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btn_equal.grid(row = 4, column = 4, padx = 1, pady = 1)
        self.btn_equal.bind("<Button-1>", press_btn)

        self.btndiv = Button(self.calc_frame, bg = 'lightblue', text = "/",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btndiv.grid(row = 4, column = 3, padx = 1, pady = 1)
        self.btndiv.bind("<Button-1>", press_btn)

        self.btndelete = Button(self.calc_frame, bg = 'lightblue', text = "DEL",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btndelete.grid(row = 2, column = 4, padx = 1, pady = 1)
        self.btndelete.bind("<Button-1>", press_btn)

        
        self.btn2zero = Button(self.calc_frame, bg = 'lightblue', text = "00",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btn2zero.grid(row = 4, column = 0, padx = 1, pady = 1)
        self.btn2zero.bind("<Button-1>", press_btn)

        
        self.btn3zero = Button(self.calc_frame, bg = 'lightblue', text = "000",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btn3zero.grid(row = 4, column = 2, padx = 1, pady = 1)
        self.btn3zero.bind("<Button-1>", press_btn)

        
        self.btnclear = Button(self.calc_frame, bg = 'lightblue', text = "C",bd = 8, width = 3, height = 1, font = ("Arial", 15))
        self.btnclear.grid(row = 1, column = 4, padx = 1, pady = 1)
        self.btnclear.bind("<Button-1>", press_btn)
        
        #==============================================
        
        #================Invoice=========================

        self.bill_frame = LabelFrame(self.win, text = "Invoice", font = ("Arial", 15, "bold"), background = "lightpink", bd = 8, relief = GROOVE)
        self.bill_frame.place(x = 575, y = 400, width = 651, height = 240)

        self.y_scroll = Scrollbar(self.bill_frame, orient = "vertical")
        self.bill_txt = Text(self.bill_frame, bg = "white", yscrollcommand = self.y_scroll.set)
        self.y_scroll.config(command = self.bill_txt.yview)
        self.y_scroll.pack(side = RIGHT, fill = Y)
        self.bill_txt.pack(fill = BOTH, expand = TRUE)


        default_bill()

        #====================================================

