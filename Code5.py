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
