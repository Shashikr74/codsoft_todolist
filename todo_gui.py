# file: todo_gui.py
import tkinter as tk
from tkinter import messagebox
from todo_backend import *

def refresh_list():
    listbox.delete(0, tk.END)
    tasks = get_tasks()
    for i, t in enumerate(tasks):
        listbox.insert(tk.END, f"{i}. {t['task']} [{t['status']}]")

def add():
    task = entry.get()
    if task:
        add_task(task)
        entry.delete(0, tk.END)
        refresh_list()

def delete():
    try:
        index = listbox.curselection()[0]
        delete_task(index)
        refresh_list()
    except:
        messagebox.showerror("Error", "Select a task")

def complete():
    try:
        index = listbox.curselection()[0]
        mark_complete(index)
        refresh_list()
    except:
        messagebox.showerror("Error", "Select a task")

def update():
    try:
        index = listbox.curselection()[0]
        new_task = entry.get()
        update_task(index, new_task)
        entry.delete(0, tk.END)
        refresh_list()
    except:
        messagebox.showerror("Error", "Select a task")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", command=add).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", command=update).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", command=delete).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Complete", command=complete).grid(row=0, column=3, padx=5)

refresh_list()
root.mainloop()
