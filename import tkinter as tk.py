import tkinter as tk 
from tkinter import *  
import random  
import json 
import os
with open("user_data.json", "r") as file: 
    data = json.load(file)

def clear_window(): 
    for widget in screen.winfo_children(): 
        widget.destroy() 

def tournament_config(): 
    clear_window()
    screen.title("Login")
    tk.Label(screen, text="Login", font=("Times New Roman", 35)).pack(pady=20)  

    tk.Label(screen, text="First name", font=("Times New Roman", 15)).pack(pady=20)
    firstname_box = tk.Entry(screen, bg="white", fg="black")
    firstname_box.insert(0, "Enter first name")
    firstname_box.pack(pady=10)

    tk.Label(screen, text="Last name", font=("Times New Roman", 15)).pack(pady=20)
    lastname_box = tk.Entry(screen, bg="white", fg="black")
    lastname_box.insert(0, "Enter last name")
    lastname_box.pack(pady=10) 

    tk.Label(screen, text="Student Number", font=("Times New Roman", 15)).pack(pady=20)
    studentnumber_box = tk.Entry(screen, bg="white", fg="black")
    studentnumber_box.insert(0, "Enter your student number")
    studentnumber_box.pack(pady=10)

    tk.Label(screen, text="Password", font=("Times New Roman", 15)).pack(pady=20)
    password = tk.Entry(screen, bg="white", fg="black")
    password.insert(0, "At least 8 characters long")
    password.pack(pady=10) 

screen = tk.Tk()
screen.geometry("800x600")
screen.title("Tournament App")

title = tk.Label(screen, text="Tournament App", font=("Times New Roman", 35))
title.pack(padx=10, pady=20) 

login_button = tk.Button(screen, text="Log in", command=tournament_config)
login_button.pack(pady=10)  

next_button = tk.Button(screen, text="Next", command=tournament_config)
next_button.pack(pady=10) 




screen.mainloop() 