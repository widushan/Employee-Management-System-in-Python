from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All fields are required')
    else:
        if usernameEntry.get()=='admin' and passwordEntry.get()=='1234':
            messagebox.showinfo('Success', 'Login Successful')
            root.destroy()
            import ems

root = CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('Login Page')

# Background image
image = CTkImage(Image.open('cover.png'), size=(930,478))
imageLabel = CTkLabel(root, image=image, text='')
imageLabel.place(x=0, y=0)

# Heading label
headinglabel = CTkLabel(
    root,
    text='Employment Management System',
    bg_color='#FAFAFA',
    font=('Times New Roman', 24, 'bold'),
    text_color='darkblue'
)
headinglabel.place(x=20, y=20)  # Position the label

usernameEntry = CTkEntry(
    root,
    fg_color="#FFFFFF",  # Background of the input area (entry field)
    bg_color="#FAFAFA",  # Background surrounding the entry (blends with image or frame)
    placeholder_text="Enter Your Username",
    text_color="black",  # Input text color
    placeholder_text_color="gray",
    width=180  # Optional: make placeholder lighter
)
usernameEntry.place(x=50, y=150)

passwordEntry = CTkEntry(
    root,
    fg_color="#FFFFFF",  # Background of the input area (entry field)
    bg_color="#FAFAFA",  # Background surrounding the entry (blends with image or frame)
    placeholder_text="Enter Your Password",
    text_color="black",  # Input text color
    placeholder_text_color="gray",
    width=180,  # Optional: make placeholder lighter
    show='*'
)
passwordEntry.place(x=50, y=200)

loginButton = CTkButton(root,text='Login', cursor='hand2', command=login)
loginButton.place(x=80, y=250)


root.mainloop()


