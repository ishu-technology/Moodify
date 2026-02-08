#GUI
#Tkinter
from tkinter import *
win = Tk()
win.geometry('500x500')
win.title('Ishu')
win.state('zoomed')
win.config(bg='lemon chiffon')

# Widgets
# 1)Label
# pack, place and grid

# l1=Label(win, text='EHHH AJAYY BABYY' , font=('Verdana', 24) , fg='white' , bg='green')
# l1.pack()
# l2=Label(win, text='KITHEEE AAA', font=('Verdana', 24) , fg='white' , bg='green')
# l2.place(x='100', y='100')
# l3=Label(win, text= 'sadeya jaaa', font=('Arial', 24) , fg='white', bg='green')
# l3.grid(row=8, column=8)
         

# MAKING A FORM

heading=Label(win, text="REGISTRATION FORM", font=("italic" , 30), bg="lemon chiffon")
heading.grid(row=1, column=1, columnspan=4)

username=Label(win, text="Username", font=("italic", 20), bg="lemon chiffon")
username.grid(row=2, column=2)
pentry=Entry(win)
pentry.grid(row=2, column=3)

password=Label(win, text="Password", font=("italic", 20), bg="lemon chiffon")
password.grid(row=3, column=2)
pentry=Entry(win)
pentry.grid(row=3, column=3)

I_agree=Checkbutton(win, text="I agree", font=("italic", 20), bg="lemon chiffon")
I_agree.grid(row=4, column=2)

Gender=Label(win, text="Gender", font=("italic", 20), bg="lemon chiffon")
Gender.grid(row=5, column=2)

gender_var=StringVar()
Male= Radiobutton(win, text="Male", font=("italic", 20), bg="lemon chiffon", )
Male.grid(row=5, column=3)
Female= Radiobutton(win, text="Female", font=("italic", 20), bg="lemon chiffon")
Female.grid(row=5, column=4)
Other= Radiobutton(win, text="Other", font=("italic", 20), bg="lemon chiffon")
Other.grid(row=5, column=5)

Country=Label(win, text="Country", font=("italic", 20), bg="lemon chiffon")
Country.grid(row=6, column=2)
spin= Spinbox(win, values=("India", "America", "Pakistan", "Nepal", "China" , "Vietnam"))
spin.grid(row=6, column=3)

Options=Label(win, text="Who is the best?", font=("italic", 20), bg="lemon chiffon")
Options.grid(row=7, column=2, padx= 50)
selected_option= StringVar(win)
selected_option.set("Select")
Options=["ISHUUU", "AJAYY", "4 LOG", "DUNIYAA"]
option_menu=OptionMenu(win, selected_option, *Options)
option_menu.grid(row=7, column=3)

feedback=Label(win, text="Feedback", font=("italic", 20), bg="lemon chiffon")
feedback.grid(row=8, column=2)
T= Text(win, width=20, height=5)
T.grid(row=8, column=3)

M= Message(win, text=r"PS C:\Users\HP\Desktop\PYTHON>  & 'c:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe' 'c:\Users\HP\.vscode\extensions\ms-python.debugpy-2025.8.0-win32-x64\undled\libs\debugpy\launcher' '51585' '--' 'c:\Users\HP\Desktop\PYTHON\day7.py'PS C:\Users\HP\Desktop\PYTHON> ^CPS C:\Users\HP\Desktop\PYTHON>", bg="lemon chiffon")
M.grid(row=2, column=6)

Font_Size=Label(win, text="Font Size", font=("italic", 20), bg="lemon chiffon")
Font_Size.grid(row=9 , column=2)
select= StringVar()
font_size= Scale(win, variable=StringVar, from_=0, to =120, orient=HORIZONTAL)
font_size.grid(row= 9, column=3)

tochoose=Label(win, text="Choose any", font=("italic", 20), bg="lemon chiffon")
tochoose.grid(row=10, column=2)
listbox=Listbox(win, selectmode=MULTIPLE, height=5)
listbox.insert(1, 'Mumma')
listbox.insert(2, 'papa')
listbox.insert(3, 'babyy')
listbox.insert(4, 'veera')
listbox.insert(5, 'saare')
listbox.grid(row=10, column=3)



submit=Button(win, text="submit", bg="indianred1")
submit.grid(row=11, column=2, pady=50)

reset=Button(win, text="reset", bg="indianred1")
reset.grid(row=11, column=3, pady=50)



win.mainloop()