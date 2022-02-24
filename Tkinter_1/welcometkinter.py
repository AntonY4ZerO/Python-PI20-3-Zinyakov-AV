from tkinter import *
from tkinter.filedialog import asksaveasfile

root = Tk()
root.title("Personal poll")
root.geometry("800x500")
root.maxsize(800, 500)
root.config(bg="grey")

name_variable = StringVar()
surname_variable = StringVar()
gender_variable = StringVar()


def submit():
    name = name_variable.get()
    surname = surname_variable.get()
    gender = gender_variable.get()
    yea = str(year.get())

    print("The name is : " + name)
    print("The surname is : " + surname)
    print("The gender is : " + gender)
    print("The year is : " + yea)


def reset():
    name_variable.set("")
    surname_variable.set("")
    gender_variable.set("")
    year.set('18')


def print_value(val):
    print(val)


my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Reset", command=reset)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Submit", command=submit)

enter_info = Label(root, text="Please enter your information: ", bg="lightgrey")
enter_info.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

name_info = Label(root, text='Name', bg='lightgrey')
name_info.grid(row=1, column=1, padx=5, pady=5)
name = Entry(root, textvariable=name_variable)
name.grid(row=1, column=2, padx=5, pady=5)

surname_info = Label(root, text='Surname', bg='lightgrey')
surname_info.grid(row=2, column=1, padx=5, pady=5)
surname = Entry(root, textvariable=surname_variable)
surname.grid(row=2, column=2, padx=5, pady=5)

gender_info = Label(root, text='Gender', bg='lightgrey')
gender_info.grid(row=3, column=1, padx=5, pady=5)
gender = Entry(root, textvariable=gender_variable)
gender.grid(row=3, column=2, padx=5, pady=5)

year_info = Label(root, text='Years', bg='lightgrey')
year_info.grid(row=4, column=1, padx=5, pady=5)
year = Scale(root, orient=HORIZONTAL, length=500, from_=18, to=50, tickinterval=2, resolution=1)
year.grid(row=4, column=2, columnspan=10, padx=5, pady=5)

submit_button = Button(root, text='Submit', command=submit)
submit_button.grid(row=5, column=1, padx=5, pady=5)


#def save_button():
#    files = [('All Files', '*.*'),
#             ('Python Files', '*.py'),
#             ('Text Document', '*.txt')]
#    file = asksaveasfile(filetypes=files, defaultextension=files)
#
#
#btn = Button(root, text='Save', command=lambda: save_button())
#btn.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()
