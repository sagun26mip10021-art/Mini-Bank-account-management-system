#BANK MANAGEMENT SYSTEM 
import tkinter as tk
from tkinter import messagebox

name = ""
account_no = ""
balance = 0


def create_account():
    global name, account_no, balance

    name = name_entry.get()
    account_no = account_entry.get()
    balance = 0

    if name == "" or account_no == "":
        messagebox.showerror("Error", "Please enter all details")
    else:
        messagebox.showinfo("Success", "Account created successfully")


def deposit():
    global balance

    amount = amount_entry.get()

    if amount == "":
        messagebox.showerror("Error", "Enter amount")
    else:
        amount = float(amount)
        balance = balance + amount
        messagebox.showinfo("Success", "Amount deposited successfully")


def withdraw():
    global balance

    amount = amount_entry.get()

    if amount == "":
        messagebox.showerror("Error", "Enter amount")
    else:
        amount = float(amount)

        if amount > balance:
            messagebox.showerror("Error", "Insufficient balance")
        else:
            balance = balance - amount
            messagebox.showinfo("Success", "Amount withdrawn successfully")


def check_balance():
    messagebox.showinfo("Balance", "Your balance is ₹" + str(balance))


def account_details():
    messagebox.showinfo(
        "Account Details",
        "Name: " + name +
        "\nAccount Number: " + account_no +
        "\nBalance: ₹" + str(balance)
    )


# Main window
window = tk.Tk()
window.title("Mini Bank Account Management System")
window.geometry("400x500")


# Heading
heading = tk.Label(
    window,
    text="MINI BANK MANAGEMENT SYSTEM",
    font=("Arial", 16, "bold")
)
heading.pack(pady=20)


# Name
tk.Label(window, text="Enter Name").pack()
name_entry = tk.Entry(window)
name_entry.pack(pady=5)


# Account number
tk.Label(window, text="Enter Account Number").pack()
account_entry = tk.Entry(window)
account_entry.pack(pady=5)


# Amount
tk.Label(window, text="Enter Amount").pack()
amount_entry = tk.Entry(window)
amount_entry.pack(pady=5)


# Buttons
tk.Button(window, text="Create Account",
          width=25, command=create_account).pack(pady=10)

tk.Button(window, text="Deposit",
          width=25, command=deposit).pack(pady=5)

tk.Button(window, text="Withdraw",
          width=25, command=withdraw).pack(pady=5)

tk.Button(window, text="Check Balance",
          width=25, command=check_balance).pack(pady=5)

tk.Button(window, text="Account Details",
          width=25, command=account_details).pack(pady=5)

tk.Button(window, text="Exit",
          width=25, command=window.destroy).pack(pady=15)


window.mainloop()
