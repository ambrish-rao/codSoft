import tkinter
from tkinter import *

# Initialize the main application window
root = Tk()
root.title("To-Do-List")  # Set the title of the application
root.geometry("400x650+400+100")  # Set the size and position of the window
root.resizable(False, False)  # Disable resizing

# List to hold tasks
task_list = []

# Function to add a new task̥
def addTask():
    task = task_entry.get()  # Get the task entered by the user
    task_entry.delete(0, END)  # Clear the input field after getting the task

    if task:  # Check if the task is not empty
        # Append the task to the file
        with open("codSoft/tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        
        task_list.append(task)  # Add the task to the in-memory list
        list_box.insert(END, task)  # Add the task to the ListBox
        list_box.itemconfig(END, {'fg': 'white'})  # Set the task text color to white

# Function to delete the selected task
def deleteTask():
    global task_list

    task = str(list_box.get(ANCHOR))  # Get the selected task from the ListBox
    if task in task_list:  # Check if the task exists in the list
        task_list.remove(task)  # Remove the task from the in-memory list
        
        # Update the task file after deletion
        with open("codSoft/tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        
        list_box.delete(ANCHOR)  # Remove the task from the ListBox

# Function to load tasks from the file on application start
def open_task():
    try:
        global task_list
        # Open the file and read all tasks
        with open("codSoft/tasklist.txt", 'r') as taskfile:
            tasks = taskfile.readlines()
        
        for task in tasks:
            if task.strip():  # Avoid adding empty lines
                task = task.strip()
                task_list.append(task)  # Add to the in-memory list
                list_box.insert(END, task)  # Add to the ListBox
    except FileNotFoundError:
        # Create the file if it doesn't exist
        with open("codSoft/tasklist.txt", 'w') as taskfile:
            pass

# Set application icon
Image_icon = PhotoImage(file="codSoft/images/task.png")
root.iconphoto(False, Image_icon)

# Top bar section
top_image = PhotoImage(file="codSoft/images/topbar.png")
Label(root, image=top_image).pack()

dock_image = PhotoImage(file="codSoft/images/dock.png")
Label(root, image=dock_image, bg='#32405b').place(x=30, y=25)

note_image = PhotoImage(file="codSoft/images/task.png")
Label(root, image=note_image, bg='#32405b').place(x=340, y=25)

heading = Label(root, text="ALL TASK", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# Input frame for adding tasks
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task_entry = Entry(frame, width=18, font="arial 20", bd=0)  # Input field for tasks
task_entry.place(x=10, y=7)

# Add button
button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

# Frame for the ListBox (task display)
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

# ListBox to display tasks
list_box = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white")
list_box.pack(side=LEFT, fill=BOTH, padx=2)

# Scrollbar for the ListBox
scroll_bar = Scrollbar(frame1)
scroll_bar.pack(side=RIGHT, fill=BOTH)

# Link the Scrollbar with the ListBox
list_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)

# Load tasks from the file
open_task()

# Delete button
delete_icon = PhotoImage(file="codSoft/images/delete.png")
Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

# Run the application
root.mainloop()
