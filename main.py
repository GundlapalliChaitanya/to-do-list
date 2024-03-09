import tkinter as tk

from tkinter import messagebox

def add_task():

 task = entry_task.get()
if task:

 listbox_tasks.insert(tk.END, task)

 entry_task.delete(0, tk.END)

 else:

 messagebox.showwarning('Warning', 'Please enter a task.')

def delete_task():

 try:

 selected_task_index = listbox_tasks.curselection()[0]

 listbox_tasks.delete(selected_task_index)

 except IndexError:

 messagebox.showwarning('Warning', 'Please select a task to 

delete.')

def display_tasks():

 tasks = listbox_tasks.get(0, tk.END)

 if not tasks:

 messagebox.showinfo('To-Do List', 'The to-do list is empty.')

 else:

 messagebox.showinfo('To-Do List', '\n'.join(tasks))

def mark_complete():

 try:

 selected_task_index = listbox_tasks.curselection()[0]
listbox_tasks.itemconfig(selected_task_index, {'bg': 'light 

green'})

 except IndexError:

 messagebox.showwarning('Warning', 'Please select a task to 

mark as complete.')

app = tk.Tk()

app.title('To-Do List App')

frame = tk.Frame(app)

frame.pack(pady=10)

entry_task = tk.Entry(frame, width=30)

entry_task.grid(row=0, column=0, padx=5)

btn_add_task = tk.Button(frame, text='Add Task', 

command=add_task)

btn_add_task.grid(row=0, column=1, padx=5)

btn_delete_task = tk.Button(frame, text='Delete Task', 

command=delete_task)

btn_delete_task.grid(row=0, column=2, padx=5)

btn_display_tasks = tk.Button(frame, text='Display Tasks', 

command=display_tasks)
btn_display_tasks.grid(row=0, column=3, padx=5)

btn_mark_complete = tk.Button(frame, text='Mark Complete', 

command=mark_complete)

btn_mark_complete.grid(row=0, column=4, padx=5)

listbox_tasks = tk.Listbox(app, selectmode=tk.SINGLE, 

bg='white', selectbackground='light blue', 

selectforeground='black')

listbox_tasks.pack(padx=10, pady=10)

app.mainloop()
