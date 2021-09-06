import sqlite3
from tkinter import *
import main


class CustomerInfo:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("GUEST INFO")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        self.bg = PhotoImage(file="images/back.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg_right = PhotoImage(file="images/2.png")
        bg1_lbl = Label(self.root, image=self.bg_right)
        bg1_lbl.place(x=1100,y=0,height=1000,width=500)
        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        left = Frame(self.root, relief="solid")
        left.pack(side="left")

        right = Frame(self.root, relief="solid")
        right.pack(side="left")

        # display message
        self.label = Label(top, font=('arial', 50, 'bold'), text="LIST OF GUESTS", fg="#15d3ba", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        # display message
        self.name_label = Label(left, font=('arial', 20, 'bold'), text="NAME", fg="#15d3ba", anchor="center")
        self.name_label.grid(row=0, column=1, padx=10, pady=10)

        # text enter field
        self.name_customer_entry = Text(left, height=30, width=70)
        self.name_customer_entry.grid(row=1, column=1, padx=10, pady=10)

        # display message
        self.room_no_label = Label(right, font=('arial', 20, 'bold'), text="ROOM NO", fg="#15d3ba", anchor="center")
        self.room_no_label.grid(row=0, column=1, padx=10, pady=10)

        # text enter field
        self.room_no_customer_entry = Text(right, height=30, width=70)
        self.room_no_customer_entry.grid(row=1, column=1, padx=10, pady=10)

        # create home button
        self.home_button = Button(top, text="HOME", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2, width=15,
                                  fg="black", anchor="center", command=lambda: self.root.destroy())
        self.home_button.grid(row=8, column=3, padx=10, pady=10)

        def display_info():

            conn = sqlite3.connect('Hostel.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Hostel (Fullname TEXT,Address TEXT,mobile_number TEXT,number_days TEXT,'
                'room_number NUMBER)')
            conn.commit()
            with conn:
                cursor.execute("SELECT Fullname FROM Hostel")
                ans = cursor.fetchall()
                for i in ans:
                    self.name_customer_entry.insert(INSERT, i[0] + '\n')

            with conn:
                cursor.execute("SELECT room_number FROM Hostel")
                ans = cursor.fetchall()
                for i in ans:
                    self.room_no_customer_entry.insert(INSERT, str(i[0]) + '\n')
        # create display button
        self.display_button = Button(top, text="DISPLAY", font=('', 15), bg="#15d3ba", relief=RIDGE, height=2, width=15,
                                     fg="black", anchor="center", command=display_info)
        self.display_button.grid(row=8, column=4, padx=10, pady=10)


def customer_info_ui():
    root = Toplevel()
    application = CustomerInfo(root)
    root.mainloop()
