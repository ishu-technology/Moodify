from tkinter import *
from tkinter import Tk
from tkinter import font
import login_user
from PIL import Image,ImageTk
import tkinter as tk
Label, PhotoImage
import happy
import sad
import Romantic
import Calm
import Energetic
import Spiritual
import Work
import Angry

def selectmood():
    moodwin = Toplevel()
    moodwin.geometry('2000x2000')
    moodwin.title('Moodify Login')
    moodwin.state('zoomed')
    moodwin.config(bg='black')
    # Set fonts
    title_font = font.Font(family='Verdana', size=43, weight='bold', slant='italic')
    label_font = font.Font(family='Lucida Handwriting', size=40, underline=3)
    button_font = font.Font(family='Georgia', size=17, weight='bold')

    #Left frame
    left_frame=Frame(moodwin, width=500)
    left_frame.pack(side=LEFT, padx=0, pady=0,fill=Y)
    left_frame.pack_propagate(False)


    #frame_1 in left frame / Upper frame
    frame_1=Frame(left_frame, height=150,bg='hot pink')
    frame_1.pack(side=TOP,fill=X)
    frame_1.pack_propagate(False)

    label=Label(frame_1, text='Hello ' + login_user.logged_user, font=title_font,bg='hot pink' )
    label.pack(pady=(30,0))


    #frame_2 in left frame/ Lower frame
    frame_2=Frame(left_frame, height=650, bg='white')
    frame_2.pack(side=BOTTOM,fill=X)
    frame_2.pack_propagate(False)

    frame_2_img = Image.open("musicimg.jpg")  
    frame_2_img = frame_2_img.resize((400, 400)) 
    fg_photo = ImageTk.PhotoImage(frame_2_img)
    frame_2_img_lable = Label(frame_2, image=fg_photo, bg='white')
    frame_2_img_lable.pack(expand=True)


    #right frame
    right_frame=Frame(moodwin, bg='pink',width=1200,  height=1000)
    right_frame.pack(side=RIGHT, padx=0, pady=0, fill=Y)
    right_frame.pack_propagate(False)

    # frame_a=Frame(right_frame, bg='pink', height=100)
    # frame_a.pack(side=TOP,fill=X)
    # frame_a.pack_propagate(False)
    label=Label(right_frame, text="How's Your Mood Today??", font=label_font, bg='pink')
    label.pack(expand=True)

    frame_b=Frame(right_frame, bg='pink', height=900)
    frame_b.pack(side=BOTTOM,fill=X)
    frame_b.pack_propagate(False)

    # Mood data: (Emoji + Mood)
    moods = [("😊 Happy", "khaki",happy.happy_mood),("😢 Sad", "#3a3f51", sad.sad_mood ),("❤ Romantic", "#d62828", Romantic.romantic_mood),("🏋 Energetic", "#ff6b00", Energetic.energetic_mood),("😌 Calm", "#a3b18a", Calm.calm_mood),("😡 Angry", "#212121", Angry.angry_mood),("🌛 Work", "#9514c0", Work.work_mood),("🕊 Spiritual", "#4caf50", Spiritual.spiritual_mood)]

    # Create mood labels in grid (2 columns x 4 rows)
    for index, (mood, color, fn) in enumerate(moods):
        row = index // 2
        col = index % 2
        mood_button = Button(frame_b, text=mood, bg=color, font=button_font, width=20, height=3, relief=RAISED, bd=2,command=fn)
        mood_button.grid(row=row, column=col,padx=(95),pady=(10,50))

    moodwin.mainloop()