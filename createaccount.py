#Moodift app
from tkinter import *
from tkinter import Tk
from tkinter import font
import os
from PIL import Image,ImageTk
import tkinter as tk
Label, PhotoImage
import db_connect
from tkinter import messagebox

def signup():
    createacc = Toplevel()
    createacc.geometry('1000x1000')
    createacc.title('Moodify Login')
    createacc.state('zoomed')
    createacc.config(bg='light pink')


    main_frame= Frame(createacc, bg='white', width=900, height=500)
    main_frame.place(relx=0.5, rely=0.5, anchor= CENTER)

    left_frame=Frame(main_frame, width=500, height=500, bg='snow3')
    left_frame.pack(side=LEFT, padx=0, pady=0)
    left_frame.pack_propagate(False)

    left_frame_img = Image.open(r"C:\Users\HP\Desktop\PYTHON\create account img.jpg")  # Replace with your background image
    left_frame_img = left_frame_img.resize((500, 500))   # Match window size
    bg_photo = ImageTk.PhotoImage(left_frame_img)
    left_frame_img_lable = Label(left_frame, image=bg_photo, bg='white')
    left_frame_img_lable.place(x=0, y=0, relwidth=1, relheight=1)


    right_frame=Frame(main_frame, width=450, height=500, bg='White')
    right_frame.pack(side=RIGHT, padx=0, pady=0)
    right_frame.pack_propagate(False)

    # Set fonts
    title_font = font.Font(family='Arial', size=24, weight='bold')
    label_font = font.Font(family='Arial', size=12)
    button_font = font.Font(family='Arial', size=14, weight='bold')
    small_font = font.Font(family='Arial', size=10)

    #db function 
    def register():
        Fullname=name_entry.get()
        Username=username_entry.get()
        Email=email_entry.get()
        Password=password_entry.get()
        ConfirmPassword=confirm_password_entry.get()
        data=(Fullname,Username,Email,Password,ConfirmPassword)
        print(data)
        try:
            q="insert into createacc(fullname, username, email, password, confirmpassword) values(?,?,?,?,?)"
            db_connect.cur.execute(q, data)
            db_connect.conn.commit()
            messagebox.showinfo("Success","Sign up is succesfull")

        except Exception as e:
            print(e)
            messagebox.showerror('Error',"Error in insertion")


    # Title Label
    title_label = Label(right_frame, text="Create Account", font=title_font, bg='white')
    title_label.pack(pady=(30,30))

    # Full name /entry
    name=Frame(right_frame)
    name.pack(pady=10)
    name_entry = Entry(name, width=30, font=label_font, relief='flat')
    name_entry.pack()
    underline_name=Frame(name, height=2, bg='black')
    underline_name.pack(fill='x')
    name_entry.insert(0,'Full Name')
    # Remove placeholder on focus
    name_entry.bind('<FocusIn>', lambda e: name_entry.delete(0, 'end') if name_entry.get() == 'Full Name' else None)
    name_entry.bind('<FocusIn>', lambda e: name_entry.config(fg='black'), add='+')
    # Add placeholder back on focus out
    name_entry.bind('<FocusOut>', lambda e: (name_entry.insert(0, 'Full Name'), name_entry.config(fg='grey')) if name_entry.get() == '' else None)

    # Username Entry
    username_frame=Frame(right_frame)
    username_frame.pack(pady=10)
    username_entry = Entry(username_frame, width=30, font=label_font, relief='flat')
    username_entry.pack()
    underline_username=Frame(username_frame, height=2, bg='black')
    underline_username.pack(fill='x')
    username_entry.insert(0, 'Username')
    # Remove placeholder on focus
    username_entry.bind('<FocusIn>', lambda e: username_entry.delete(0, 'end') if username_entry.get() == 'Username' else None)
    username_entry.bind('<FocusIn>', lambda e: username_entry.config(fg='black'), add='+')
    # Add placeholder back on focus out
    username_entry.bind('<FocusOut>', lambda e: (username_entry.insert(0, 'Username'), username_entry.config(fg='grey')) if username_entry.get() == '' else None)

    # Username/email Entry
    email_frame=Frame(right_frame)
    email_frame.pack(pady=10)
    email_entry = Entry(email_frame, width=30, font=label_font, relief='flat')
    email_entry.pack()
    underline_email=Frame(email_frame, height=2, bg='black')
    underline_email.pack(fill='x')
    email_entry.insert(0, 'Email')
    # Remove placeholder on focus
    email_entry.bind('<FocusIn>', lambda e: email_entry.delete(0, 'end') if email_entry.get() == 'Email' else None)
    email_entry.bind('<FocusIn>', lambda e: email_entry.config(fg='black'), add='+')
    # Add placeholder back on focus out
    email_entry.bind('<FocusOut>', lambda e: (email_entry.insert(0, 'Email'), email_entry.config(fg='grey')) if email_entry.get() == '' else None)

    # Password Entry
    password_frame = Frame(right_frame)
    password_frame.pack(pady=10)
    password_entry = Entry(password_frame, width=30, font=label_font, relief='flat')
    password_entry.insert(0,'Password')
    password_entry.pack()
    underline_password=Frame(password_frame, height=2, bg='black')
    underline_password.pack(fill='x')
    # Remove placeholder on focus
    password_entry.bind('<FocusIn>', lambda e: password_entry.delete(0, 'end') if password_entry.get() == 'Password' else None)
    password_entry.bind('<FocusIn>', lambda e: password_entry.config(fg='black'), add='+')
    # Add placeholder back on focus out
    password_entry.bind('<FocusOut>', lambda e: (password_entry.insert(0, 'Password'), password_entry.config(fg='grey')) if password_entry.get() == '' else None)

    # Confirm Password Entry
    confirm_password_frame = Frame(right_frame)
    confirm_password_frame.pack(pady=10)
    confirm_password_entry = Entry(confirm_password_frame, width=30, font=label_font, relief='flat')
    confirm_password_entry.insert(0,'Confirm Password')
    confirm_password_entry.pack()
    underline_confirm_password=Frame(confirm_password_frame, height=2, bg='black')
    underline_confirm_password.pack(fill='x')
    # Remove placeholder on focus
    confirm_password_entry.bind('<FocusIn>', lambda e: confirm_password_entry.delete(0, 'end') if confirm_password_entry.get() == 'Confirm Password' else None)
    confirm_password_entry.bind('<FocusIn>', lambda e: confirm_password_entry.config(fg='black'), add='+')
    # Add placeholder back on focus out
    confirm_password_entry.bind('<FocusOut>', lambda e: (confirm_password_entry.insert(0, 'Confirm Password'), confirm_password_entry.config(fg='grey')) if confirm_password_entry.get() == '' else None)


    #sign in button
    sign_in_button = Button(right_frame, text="Sign up", bg="#ff4b9e", fg="white", font=button_font, width=20, command=register)
    sign_in_button.pack(pady=(60,10))

    # Create an account link
    bottom_frame =Frame(right_frame, bg='white')
    bottom_frame.pack(pady=10)
    already_account_label= Label(bottom_frame, text="Already have an account?", font=small_font, bg='white')
    already_account_label.pack(side='left')

    already_account_label = Label(bottom_frame, text="Log in", fg="orange", cursor="hand2", font=small_font, bg='white')
    already_account_label.pack(side='left', padx=5)


    createacc.mainloop()