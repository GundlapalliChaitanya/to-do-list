def delete_task():

 try:

 selected_task_index = listbox_tasks.curselection()[0]

 listbox_tasks.delete(selected_task_index)

 except IndexError:

 messagebox.showwarning('Warning', 'Please select a task to 

delete.')
