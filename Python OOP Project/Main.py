#import tkinter app, messagebox and import class Persona
import tkinter as tk
from tkinter import messagebox, filedialog
from Persona import *
from Database import *

#Profile Window:
def profileWindow(user):
    profile_window = tk.Tk()
    profile_window.title("Profile Page")
    profile_window.geometry("400x300")

    tk.Label(profile_window, text="Profile").grid(row=0, column=0,columnspan=2)

    #
    tk.Label(profile_window, text="Name: ").grid(row=1, column=0)
    tk.Label(profile_window, text="Surname: ").grid(row=2, column=0)

    #Log Out function
    def logOutFunction():
        profile_window.destroy()

    #log out button
    tk.Button(profile_window, text="Log Out", command=logOutFunction)

    profile_window.mainloop()

#Login Window

def loginWindow():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("300x200")

#crear widgets primero
    tk.Label(login_window, text="Log In").grid(row=0, column=2, columnspan=2)

    tk.Label(login_window, text="Email: ").grid(row=1, column=0)
    tk.Label(login_window, text="Password: ").grid(row=2, column=0)

#email and password field
    entry__email = tk.Entry(login_window)
    entry__email.grid(row=1, column=1) 

    entry__password = tk.Entry(login_window, show="*")
    entry__password.grid(row=2, column=1)

#validate login:
    def validateLogin():
        email = entry__email.get()
        password = entry__password.get()

    users = read_database()
#calling static method:
    email = entry__email.get()
    password = entry__password.get()
    msg, user = Persona.log_in(email=email, password=password, users=users)

    if user:
        messagebox.showinfo("Login", msg)
        login_window.destroy()  #closing the login window
        profileWindow(user)  #calling the third window
    else:
        messagebox.showerror("Login Failed", msg)
#button
    tk.Button(login_window, text="Login",command=validateLogin).grid(row=4, column=2,columnspan=2)
    
    login_window.deiconify()

    login_window.mainloop()

#Register Window:
register = tk.Tk()
register.title("Register")
register.geometry("400x300")
tk.Label(register, text="Registration").grid(row=0, column=0,columnspan=2)

entry__name = tk.Entry(register)
entry__surname = tk.Entry(register)
entry__ide = tk.Entry(register)
entry__email = tk.Entry(register)
entry__password = tk.Entry(register, show="*")
entry__age = tk.Entry(register)

tk.Label(register, text="Name: ").grid(row=1, column=0)
entry__name.grid(row=1, column=1)

tk.Label(register, text="Surname: ").grid(row=2, column=0)
entry__surname.grid(row=2, column=1)

tk.Label(register, text="ide: ").grid(row=3, column=0)
entry__ide.grid(row=3, column=1)

tk.Label(register, text="Email: ").grid(row=4, column=0)
entry__email.grid(row=4, column=1)

tk.Label(register, text="Password: ").grid(row=5, column=0)
entry__password.grid(row=5, column=1)

tk.Label(register, text="Age: ").grid(row=6, column=0)
entry__age.grid(row=6, column=1)

'''Login instead of sign up'''
tk.Label(register, text="Do you have an account?").grid(row=8, column=0)

'''button element'''
tk.Button(register, text="Sign Up").grid(row=7, column=0, columnspan=2)

#function to go to the second window:
def goLogin():
    register.destroy()
    loginWindow()

#button to go direclty to the login page and close the current page
tk.Button(register, text="Go to Login", command=goLogin).grid(row=8, column=3, columnspan=2)

'''line to run the app'''
register.mainloop()