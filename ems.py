from customtkinter import *
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
import database





# fUNCTIONS

def delete_all():
    result = messagebox.askyesno('Delete All', 'Are you sure you want to delete all records?')
    if result:
        database.deleteall_records()
        tree.delete(*tree.get_children())
        clear()
        messagebox.showinfo('Success', 'All records deleted successfully')
    else:
        messagebox.showinfo('Cancelled', 'Deletion cancelled')

def show_all():
    searchEntry.delete(0, 'end')
    searchBox.set('Search by')
    treeview_data()
    clear()



def search_employee():
    if searchEntry.get() == '':
        messagebox.showerror('Error', 'Enter a value to search')
    elif searchBox.get() == 'Search by':
        messagebox.showerror('Error', 'Select a search option')
    else:
        searched_data = database.search(searchBox.get(), searchEntry.get())
        tree.delete(*tree.get_children())  
        for employee in searched_data:
            tree.insert('', 'end', values=employee)


def delete_employee():
    tree.selection()
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select an employee to delete')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror('Success', 'Data deleted successfully')


def update_employee():
    tree.selection()
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select an employee to update')
    else:
        database.update(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Data updated successfully')

    
    



def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0, row[5])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, 'end')
    nameEntry.delete(0, 'end')
    phoneEntry.delete(0, 'end')
    roleBox.set(role_options[0])
    genderBox.set(gender_options[0])
    salaryEntry.delete(0, 'end')
    

def treeview_data():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())  
    for employee in employees:
        tree.insert('', 'end', values=employee)


def add_employee():
    if idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get() == '' or salaryEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error', 'ID already exists')
    elif not idEntry.get().startswith('E'):
        messagebox.showerror('Error', 'ID must start with "E"')
    else:
        database.insert(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
        treeview_data()
        messagebox.showinfo('Success', 'Data inserted successfully')
        
        # clear the inputs after inserting data click add employee button
        clear()





# GUI Design


window=CTk()
window.geometry('1024x650+100+100')
window.resizable(0,0)
window.title('Employment Management System')
window.configure(fg_color='#161C30')

logo = CTkImage(Image.open('bg2.jpg'), size=(900,230))
logoLabel = CTkLabel(window, image=logo, text='')
logoLabel.grid(row=0, column=0, columnspan=2)

leftFrame = CTkFrame(window, fg_color='#161C30')
leftFrame.grid(row=1, column=0)


idLabel = CTkLabel(leftFrame, text='Employee ID', text_color='white' , font=('Arial', 18, 'bold'))
idLabel.grid(row=0, column=0, padx=10, pady=10, stick='w')
idEntry = CTkEntry(leftFrame, width=200, placeholder_text='Enter Employee ID' , font=('Arial', 15, 'bold'))
idEntry.grid(row=0, column=1, padx=10, pady=10)


nameLabel = CTkLabel(leftFrame, text='Employee Name', text_color='white' , font=('Arial', 18, 'bold'))
nameLabel.grid(row=1, column=0, padx=10, pady=10, stick='w')
nameEntry = CTkEntry(leftFrame, width=200, placeholder_text='Enter Employee Name' , font=('Arial', 15, 'bold'))
nameEntry.grid(row=1, column=1, padx=10, pady=10)


phoneLabel = CTkLabel(leftFrame, text='Contact No', text_color='white' , font=('Arial', 18, 'bold'))
phoneLabel.grid(row=2, column=0, padx=10, pady=10, stick='w')
phoneEntry = CTkEntry(leftFrame, width=200, placeholder_text='Enter Contact No' , font=('Arial', 15, 'bold'))
phoneEntry.grid(row=2, column=1, padx=10, pady=10)


roleLabel = CTkLabel(leftFrame, text='Role', text_color='white' , font=('Arial', 18, 'bold'))
roleLabel.grid(row=3, column=0, padx=10, pady=10, stick='w')
role_options = ["Web Developer", "Cloud Architect", "Technical Writer", "Network Engineer", "DevOps Engineer", "Data Scientist", "Business Analyst", "IT Consultant", "UX/UI Designer"]
roleBox = CTkOptionMenu(leftFrame, values=role_options, text_color='white', font=('Arial', 15, 'bold'), state='readonly')
roleBox.grid(row=3, column=1, padx=10, pady=10)
roleBox.set(role_options[0])


genderLabel = CTkLabel(leftFrame, text='Gender', text_color='white' , font=('Arial', 18, 'bold'))
genderLabel.grid(row=4, column=0, padx=10, pady=10, stick='w')
gender_options = ["Male", "Female"]
genderBox = CTkOptionMenu(leftFrame, values=gender_options, text_color='white', font=('Arial', 15, 'bold'), state='readonly')
genderBox.grid(row=4, column=1, padx=10, pady=10)
genderBox.set(gender_options[0])


salaryLabel = CTkLabel(leftFrame, text='Salary', text_color='white' , font=('Arial', 18, 'bold'))
salaryLabel.grid(row=5, column=0, padx=10, pady=10, stick='w')
salaryEntry = CTkEntry(leftFrame, width=200, placeholder_text='Enter Salary' , font=('Arial', 15, 'bold'))
salaryEntry.grid(row=5, column=1, padx=10, pady=10)





rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=1)


search_options = ["Id" , "Name" , "Phone" , "Role" , "Gender" , "Salary"]
searchBox = CTkOptionMenu(rightFrame, values=search_options, text_color='white', font=('Arial', 15, 'bold'), state='readonly')
searchBox.grid(row=0, column=0, padx=10, pady=10)
searchBox.set('Search by')
searchEntry = CTkEntry(rightFrame, width=200, placeholder_text='Type Your Search' , font=('Arial', 15, 'bold'))
searchEntry.grid(row=0, column=1, padx=10, pady=10)

searchButton = CTkButton(rightFrame, text='Search', width=100, cursor='hand2', font=('Arial', 15, 'bold'), text_color='white', command=search_employee)
searchButton.grid(row=0, column=2, padx=10, pady=10)

showallButton = CTkButton(rightFrame, text='Show All', width=100, cursor='hand2', font=('Arial', 15, 'bold'), text_color='white', command=show_all)
showallButton.grid(row=0, column=3, padx=10, pady=10)


tree = ttk.Treeview(rightFrame, height=13)
tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

tree['columns'] = ('Id' , 'Name' , 'Phone' , 'Role' , 'Gender' , 'Salary')

tree.heading('Id', text='Id')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Salary', text='Salary')

tree.configure(show='headings')
tree.column('Id', width=60, anchor='center')
tree.column('Name', width=150, anchor='center')
tree.column('Phone', width=90, anchor='center')
tree.column('Role', width=150, anchor='center')
tree.column('Gender', width=70, anchor='center')
tree.column('Salary', width=75, anchor='center')

style  = ttk.Style()
style.configure('Treeview.Heading', rowheight=30, font=('Arial', 10, 'bold'))
style.configure('Treeview', font=('Arial', 10, 'bold') , background='#161C30', foreground='white')

scrollbar = ttk.Scrollbar(rightFrame, orient='vertical', command=tree.yview)
scrollbar.grid(row=1, column=4, sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame = CTkFrame(window, fg_color='#161C30')
buttonFrame.grid(row=2, column=0, columnspan=2, pady=10)

newButton = CTkButton(buttonFrame, text='New Employee', width=100, cursor='hand2', font=('Arial', 15, 'bold'), text_color='white', corner_radius=10, command=lambda: clear(True))
newButton.grid(row=0, column=0, padx=10, pady=10)

addButton = CTkButton(buttonFrame, text='Add Employee', width=100, cursor='hand2', font=('Arial', 15, 'bold'), text_color='white', corner_radius=10, command=add_employee)
addButton.grid(row=0, column=1, padx=10, pady=10)

updateButton = CTkButton(buttonFrame, text='Update Employee', width=100, cursor='hand2', font=('Arial', 15, 'bold'), text_color='white', corner_radius=10, command=update_employee)
updateButton.grid(row=0, column=2, padx=10, pady=10)

deleteButton = CTkButton(buttonFrame, text='Delete Employee', width=100, cursor='hand2', font=('Arial', 15, 'bold'), text_color='white', corner_radius=10, command=delete_employee)
deleteButton.grid(row=0, column=3, padx=10, pady=10)

deleteallButton = CTkButton(buttonFrame, text='Delete All', width=100, cursor='hand2', font=('Arial', 15, 'bold'), text_color='white', corner_radius=10, command=delete_all)
deleteallButton.grid(row=0, column=4, padx=10, pady=10)



treeview_data()

window.bind('<ButtonRelease>', selection)

window.mainloop()