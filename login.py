#Moodify app

from tkinter import *
from tkinter import Tk
from tkinter import font
from PIL import Image,ImageTk
Label, PhotoImage
import createaccount
import login_user
import db_connect
import Mood_selector
from tkinter import messagebox

loginwin = Tk()
loginwin.geometry('1000x1000')
loginwin.title('Moodify Login')
loginwin.state('zoomed')
loginwin.config(bg='light pink')


main_frame= Frame(loginwin, bg='white', width=900, height=500)
main_frame.place(relx=0.5, rely=0.5, anchor= CENTER)

left_frame=Frame(main_frame, width=500, height=500, bg='snow3')
left_frame.pack(side=LEFT, padx=0, pady=0)
left_frame.pack_propagate(False)

left_frame_img = Image.open(r"C:\Users\HP\Desktop\PYTHON\welcomeback edited.jpg")  # Replace with your background image
left_frame_img = left_frame_img.resize((500, 500))   # Match loginwindow size
bg_photo = ImageTk.PhotoImage(left_frame_img)
left_frame_img_lable = Label(left_frame, image=bg_photo, bg='white')
left_frame_img_lable.place(x=0, y=0, relwidth=1, relheight=1)


right_frame=Frame(main_frame, width=450, height=500, bg='White')
right_frame.pack(side=RIGHT, padx=0, pady=0)
right_frame.pack_propagate(False)

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_button.config(text='🔒')  
    else:
        password_entry.config(show='')
        toggle_button.config(text='👁') 
     
#db function
def logini():
    username=username_entry.get()
    password=password_entry.get()
    data=(username,password)
    try:
        q="select * from createacc where username=? and password=?"
        result=db_connect.cur.execute(q, data)
        res=result.fetchone()
        if res:
            messagebox.showinfo("Success","Login Succesfull",parent=loginwin)
            login_user.logged_user=username
            Mood_selector.selectmood()
            
        else:
            messagebox.showwarning("Error","Invaild Username or Password",parent=loginwin)
    except Exception as e:
        messagebox.showerror("Error","Error",parent=loginwin)

# Set fonts
title_font = font.Font(family='Times New Romans', size=24, weight='bold')
label_font = font.Font(family='Arial', size=12)
button_font = font.Font(family='Arial', size=14, weight='bold')
small_font = font.Font(family='Arial', size=10)

# Title Label
title_label = Label(right_frame, text="Login", font=title_font, bg='white')
title_label.pack(pady=(30,30))

# Username/email Entry
username_frame=Frame(right_frame,bg='white')
username_frame.pack(pady=10)
usericon=Label(username_frame, text="👤",bg='white')
usericon.pack(side=LEFT,padx=(0,7))
username_entry = Entry(username_frame, width=28, font=label_font, relief='flat')
username_entry.pack()
underline_username=Frame(right_frame, height=2, bg='black')
underline_username.pack(fill='x',padx=87,pady=(0,10))
username_entry.insert(0, 'Username or email')
# Remove placeholder on focus
username_entry.bind('<FocusIn>', lambda e: username_entry.delete(0, 'end') if username_entry.get() == 'Username or email' else None)
username_entry.bind('<FocusIn>', lambda e: username_entry.config(fg='black'), add='+')
# Add placeholder back on focus out
username_entry.bind('<FocusOut>', lambda e: (username_entry.insert(0, 'Username or email'), username_entry.config(fg='grey')) if username_entry.get() == '' else None)

# Password Entry
password_frame = Frame(right_frame,bg="white")
password_frame.pack(pady=(10,3))
passicon=Label(password_frame, text="🔑",bg='white')
passicon.pack(side=LEFT,padx=(0,7))
password_entry = Entry(password_frame, width=26, font=label_font, relief='flat')
password_entry.insert(0,'Password')
password_entry.pack(side=LEFT)
toggle_button = Button(password_frame, text="🔒",command=toggle_password, bd=0, bg="white")
toggle_button.pack(side=LEFT)
underline_password=Frame(right_frame, height=2, bg='black',width=30)
underline_password.pack(fill='x',pady=(5,0),padx=87)

# Remove placeholder on focus
password_entry.bind('<FocusIn>', lambda e: password_entry.delete(0, 'end') if password_entry.get() == 'Password' else None)
password_entry.bind('<FocusIn>', lambda e: password_entry.config(show='*',fg='black'), add='+')

# Add placeholder back on focus out
password_entry.bind('<FocusOut>', lambda e: (password_entry.insert(0, 'Password'), password_entry.config(show='',fg='grey')) if password_entry.get() == '' else None)

# Remember me checkbox
remember_var = IntVar()
remember_check = Checkbutton(right_frame, text="Remember me", variable=remember_var, font=label_font, bg='white')
remember_check.pack( anchor='w',padx=82,pady=(20,0))

# Forgot password label
forgot_frame = Frame(right_frame, bg='white')
forgot_frame.pack()
forgot_label = Label(forgot_frame, text="Forgot password?", fg="blue", cursor="hand2", font=small_font, bg='White')
forgot_label.pack(anchor='e',pady=(70,0))
#sign in button
sign_in_button = Button(right_frame, text="Sign in", bg="#ff4b9e", fg="white", font=button_font, width=20, command=logini)
sign_in_button.pack(pady=(10,15))

# Create an account link
bottom_frame =Frame(right_frame, bg='white')
bottom_frame.pack(pady=10)
no_account_label = Label(bottom_frame, text="Not have an account?", font=small_font, bg='white')
no_account_label.pack(side='left')


create_account_label = Button(bottom_frame, relief="flat", command=createaccount.signup, text="Create an Account", fg="orange", cursor="hand2", font=small_font, bg='white')
create_account_label.pack(side='left', padx=5)



loginwin.mainloop()