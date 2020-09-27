
import tkinter as tk
from tkinter import messagebox

def show_entry():
    #print("Full Name: %s" % (e1.get()+ " "+e2.get()))
    #e1.delete(0, tk.END)
    #e2.delete(0, tk.END)
    messagebox.showinfo('Xin chào:', (e1.get()+ " "+e2.get()+ "!"))    
master = tk.Tk()
#Title
master.title("App Crazy")
#create Label
tk.Label(master, text="First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)
#inter value #use entry
e1 = tk.Entry(master)
e2 = tk.Entry(master)
#insert default value if user don't enter value 
e1.insert(10, "Như")
e2.insert(10, "Phạm")
#postion
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
#create button
btn = tk.Button(master, text="Click Me", bg="orange", fg="red",command = show_entry)
btn.grid(column=3, row=1)
tk.mainloop()


