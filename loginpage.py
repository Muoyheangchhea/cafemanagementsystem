from tkinter import *
from Window2 import Window2

class LoginPage:
    def __init__(self, win):
        self.win = win
        self.win.geometry("1320x750+0+0")
        self.win.title("Sunshine Cafe Management System")

        self.title_label = Label(self.win, text= "Sunshine Cafe Management System", font = ("Arial", 35, "bold"), bg = "lightpink", bd= 8, relief = GROOVE)
        self.title_label.pack(side = TOP, fill = X)

        self.main_frame = Frame(self.win, bg = "lightpink", bd = 6, relief = GROOVE)
        self.main_frame.place(x = 300, y = 150, width = 680, height = 350)

        self.login_lbl = Label(self.main_frame, text = "Login", bd = 5, relief = GROOVE, anchor = CENTER, bg = "lightpink", font = ("sans-serif", 23, "bold"))
        self.login_lbl.pack(side = TOP, fill = X)

        self.entry_frame = LabelFrame(self.main_frame, bd = 6, relief = GROOVE, bg = "lightpink", font = ("sans-serif", 12))
        self.entry_frame.pack(fill = BOTH, expand = TRUE)

        self.entus_lbl = Label(self.entry_frame, text = "Username: ", bg = "lightpink", font = ("sans-serif", 15))
        self.entus_lbl.grid(row = 0, column = 0, padx = 2, pady =2 )
        #===================== variables ==========================================

        username = StringVar()
        password = StringVar()


        #==============================Intro===================================
        self.entus_ent = Entry(self.entry_frame, font = ("sans-serif", 15), bd = 6, textvariable = username)
        self.entus_ent.grid(row = 0, column = 1, padx = 2, pady = 2)

        self.entpass_lbl = Label(self.entry_frame, text = "Password: ", bg = "lightpink", font = ("sans-serif", 15))
        self.entpass_lbl.grid(row = 1, column = 0, padx =2, pady = 2 )


        self.entpass_ent = Entry(self.entry_frame, font = ("sans-serif", 15), bd = 6, textvariable = password, show = "*")
        self.entpass_ent.grid(row = 1, column = 1, padx = 2, pady = 2)

        #=========================functions=========================

        def check_login():
            ''' This function will check login'''
            if username.get() == "heang" and password.get() == "1212":
                self.billing_btn.config(state = "normal")
            else:
                pass
        def reset():
            username.set("")
            password.set("")
            
        def billing_sec():
            self.newWindow = Toplevel(self.win)
            self.app = Window2(self.newWindow)

        #==============================================================


        #=====================buttons=============================


        self.button_frame = LabelFrame(self.entry_frame, text = 'Options', font = ("Arial", 15, "bold"), bg = "lightpink", bd = 7, relief = GROOVE)
        self.button_frame.place(x= 20, y = 130, width = 619, height = 88)

        self.login_btn = Button(self.button_frame, text = "Login", font= ("Arial", 15), bd = 5, width = 15, command = check_login, bg = 'lightblue')
        self.login_btn.grid(row = 0, column = 0, padx = 10, pady = 2) 

        self.billing_btn = Button(self.button_frame, text = "Go to Bill", font= ("Arial", 15), bd = 5, width = 15, command = billing_sec, bg = "lightblue")
        self.billing_btn.grid(row = 0, column = 1, padx = 10, pady = 2)
        self.billing_btn.config(state = "disabled") 

        self.reset_btn = Button(self.button_frame, text = "Reset", font= ("Arial", 15), bd = 5, width = 15, command = reset, bg = "lightblue")
        self.reset_btn.grid(row = 0, column = 2, padx = 10, pady = 2) 

        #=============================================================
