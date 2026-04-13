import tkinter as tk 
from tkinter import *  
import random  
import json 
import os

def clear_window(): 
    for widget in screen.winfo_children(): 
        widget.destroy() 

def tournament_config(): 
    clear_window()
    screen.title("Sign up")
    tk.Label(screen, text="Sign up", font=("Times New Roman", 35)).pack(pady=20)  

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

    next_button = tk.Button(screen, text="Next", command=individual_or_team)
    next_button.pack(pady=10) 

def login_screen(): 
    clear_window()
    screen.title("Login")
    tk.Label(screen,font=("Times New Roman", 35)).pack(pady=20)

    tk.Label(screen, text="Student Number", font=("Times New Roman", 15)).pack(pady=20)
    studentnumber_box = tk.Entry(screen, bg="white", fg="black")
    studentnumber_box.insert(0, "Enter your student number")
    studentnumber_box.pack(pady=10)

    tk.Label(screen, text="Password", font=("Times New Roman", 15)).pack(pady=20)
    password = tk.Entry(screen, bg="white", fg="black")
    password.insert(0, "At least 8 characters long")
    password.pack(pady=10)

    next_button = tk.Button(screen, text="Next", command=individual_or_team)
    next_button.pack(pady=10)  

def individual_or_team(): 
    clear_window()
    screen.title("Hello", student_name)
    tk.Label(screen,font=("Times New Roman", 35)).pack(pady=20)

    individual_button = tk.Button(screen, text="individual", command=events) 
    individual_button.pack(pady=10)

    team_button = tk.Button(screen, text="team", command=None)
    team_button.pack(pady=10)

def events(): 
    "jfio"


screen = tk.Tk()
screen.geometry("800x600")
screen.title("Tournament App") 

title = tk.Label(screen, text="Tournament App", font=("Times New Roman", 35))
title.pack(padx=10, pady=20) 

button_frame = tk.Frame(screen)
button_frame.pack(pady=10)

login_button = tk.Button(button_frame, text="Log in", command=login_screen)
login_button.pack(padx=10,pady=10)   

firstname_box = "" 
secondname_box =  ""

student_name = firstname_box + secondname_box 

signup_button = tk.Button(button_frame, text="Sign up", command=tournament_config)
signup_button.pack(side="right",padx=10,pady=10) 

next_button = tk.Button(screen, text="Next", command=individual_or_team) 
next_button.pack(pady=10)

individual_button = tk.Button(screen, text="individual", command=events) 
individual_button.pack(pady=10)

team_button = tk.Button(screen,text="team", command=events)
team_button.pack(side="right",padx=10,pady=10)


screen.mainloop() 