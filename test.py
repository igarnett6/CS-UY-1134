#Lance Peters
#CS1400
#ProfessorAbrahamTeng
#Project 7 - Payrole Shuffle

import tkinter as tk
from tkinter import *
from tkinter import filedialog

class Employees:

    class Erecord:

        def __init__(self, eId, eName, eAddress, eRate, eHour):

            self.id = eId
            self.name = eName
            self.address = eAddress
            self.rate = eRate
            self.hour = eHour
            self.salary = self.calc_salary()
        def __str__(self):

            return "ID: " + str(self.id) + " Name: " + self.name

        def calc_salary(self):

            if float(self.hour) <= 40:
                grossPay = float(self.rate) * float(self.hour)
            else:
                grossPay = float(self.rate)*40 + 1.5*float(self.rate)*(float(self.hour)-40)
            stateTax = grossPay * 0.075
            fedTax = grossPay * 0.2
            netPay = grossPay - stateTax - fedTax
            return netPay

    def __init__(self):

        self.curr_ind = -1
        self.employees = []
        self.root = Tk()
        self.menu = Menu(self.root)
        self.UIElements()
        self.FileMenu()
        self.root.mainloop()

    def FileMenu(self):

        self.root.config(menu = self.menu)
        filemenu = Menu(self.menu)
        self.menu.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "Open...", command = self.OpenFile)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = self.root.quit)

    def OpenFile(self):

        self.root.filename = filedialog.askopenfilename(initialdir = "C:/",
            title = "Choose your file",
            filetypes = (("Text files","*.txt"),("all files","*.*")))
        if self.root.filename is (''):
            print("ERROR: No File Selected")
            self.root.quit
        else:
            print(self.root.filename, " ...File Loaded")
            file = open(self.root.filename, "r")
            curr_line_number = 1
            for line in file:
                if(curr_line_number%4==1):
                    curr_id = line
                    curr_name = None
                    curr_addr = None
                    curr_rate = None
                    curr_hour = None
                    curr_line_number+=1
                elif(curr_line_number%4==2):
                    curr_name = line
                    curr_line_number+=1
                elif(curr_line_number%4==3):
                    curr_addr = line
                    curr_line_number+=1
                else:
                    line_lst = line.split()
                    curr_rate = line_lst[0]
                    curr_hour = line_lst[1]
                    #tuple(id, name, addr, pay, hour)
                    new_employee = self.Erecord(curr_id,
                        curr_name, curr_addr, curr_rate, curr_hour)
                    self.employees.append(new_employee)
                    curr_line_number+=1
            self.first_call = True
            self.select_next()


    def UIElements(self):

        Label(self.root, text="Employee ID").grid(row = 0)
        Label(self.root, text="Name").grid(row = 1)
        Label(self.root, text="Address").grid(row = 2)
        Label(self.root, text="Rate").grid(row = 3)
        Label(self.root, text="Hours").grid(row = 4)
        Label(self.root, text="Net Pay").grid(row = 5)

        self.eID = Entry(self.root)
        self.eName = Entry(self.root)
        self.eAddress = Entry(self.root)
        self.eRate = Entry(self.root)
        self.eHours = Entry(self.root)
        self.ePay = Entry(self.root)

        self.eID.grid(row = 0, column = 1)
        self.eName.grid(row = 1, column = 1)
        self.eAddress.grid(row = 2, column = 1)
        self.eRate.grid(row = 3, column = 1)
        self.eHours.grid(row = 4, column = 1)
        self.ePay.grid(row = 5, column = 1)

        nextbutton = tk.Button(self.root, text="Next",
            command = self.select_next).grid(row = 6, column = 1)
        backbutton = tk.Button(self.root, text="Back",
            command = self.select_back).grid(row = 6, column = 0)

    def delete_entry(self):

        if(self.first_call==False):
            self.eID.delete(0, END)
            self.eName.delete(0, END)
            self.eAddress.delete(0, END)
            self.eRate.delete(0, END)
            self.eHours.delete(0, END)
            self.ePay.delete(0, END)

    def select_next(self):

        self.delete_entry()
        self.curr_ind+=(1%len(self.employees))
        curr_employee = self.employees[self.curr_ind%len(self.employees)]
        self.eID.insert(10, curr_employee.id)
        self.eName.insert(10, curr_employee.name)
        self.eAddress.insert(10, curr_employee.address)
        self.eRate.insert(10, curr_employee.rate)
        self.eHours.insert(10, curr_employee.hour)
        self.ePay.insert(10, curr_employee.salary)
        self.first_call=False

    def select_back(self):

        self.delete_entry()
        self.curr_ind-=1
        curr_employee = self.employees[self.curr_ind%len(self.employees)]
        self.eID.insert(10, curr_employee.id)
        self.eName.insert(10, curr_employee.name)
        self.eAddress.insert(10, curr_employee.address)
        self.eRate.insert(10, curr_employee.rate)
        self.eHours.insert(10, curr_employee.hour)
        self.ePay.insert(10, curr_employee.salary) #ight, should be good

def main():

    e_obj = Employees()

main()
