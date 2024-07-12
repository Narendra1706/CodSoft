# Task - 1 Todo List Application

import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List Application")
        
        self.tasks = []
        
        self.create_widgets()
    
    def create_widgets(self):
        self.task_entry = tk.Entry(self.master, width=50)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.task_listbox = tk.Listbox(self.master, width=50, height=10)
        self.task_listbox.pack(pady=10)
        
        self.complete_button = tk.Button(self.master, text="Mark as Completed", command=self.mark_task_completed)
        self.complete_button.pack(pady=5)
        
        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task['completed'] else "Pending"
            self.task_listbox.insert(tk.END, f"{task['task']} [{status}]")
    
    def mark_task_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]['completed'] = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")
    
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()