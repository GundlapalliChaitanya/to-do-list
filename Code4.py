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
