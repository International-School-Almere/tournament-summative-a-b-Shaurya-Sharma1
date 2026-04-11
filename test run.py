import tkinter as tk 
import random

root = tk.Tk
root.geometry("400x200")
root.title("Tournament App")

root.mainloop()
print("test") 

def choice_team(var1,var2):
    choice= input('team or individual')
    if choice == "team":
        print("okay")
        
    elif choice == "individual":
        #open team event form"
        print("welldone")
    return choice
choice = choice_team()  







root.mainloop()
