from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from tkinter import font

def sad_mood():
    # Function to open a Spotify playlist in browser
    def open_spotify_playlist(url):
        webbrowser.open_new_tab(url)

    # Main window
    root = Toplevel()
    root.state('zoomed')
    root.configure(bg='#f2f2f7')
    root.geometry("2000x2000")

    # Fonts
    title_font = font.Font(family='Verdana', size=37, weight='bold')
    label_font = font.Font(family='Lucida Handwriting', size=30, weight='bold')
    button_font = font.Font(family='Georgia', size=15, weight='bold')

    # Navbar
    navbar = Frame(root, height=320, bg="#3a3f51")
    navbar.pack(fill=X)
    navbar.pack_propagate(False)


    # Page title
    title_label = Label(navbar, text="Sad", font=title_font, bg="#3a3f51", fg='white')
    title_label.grid(row=0, column=1, padx=(20,10), pady=(30,0))

    main_frame=Frame(root, height=720, bg="#f2f2f7")
    main_frame.pack(fill=X)
    main_frame.pack_propagate(False)

    # === Section: Bollywood Playlists ===
    bollywood_heading = Label(main_frame, text="BOLLYWOOD PLAYLISTS", font=label_font, bg="#f2f2f7", fg='black')
    bollywood_heading.pack(pady=(40, 10))

    bollywood_frame = Frame(main_frame, bg='#f2f2f7')
    bollywood_frame.pack()

    bollywood_data = {
        "Arijit Singh Sad Songs": (r"C:\Users\HP\Desktop\PYTHON\H sad1.jpg", "https://open.spotify.com/playlist/1MI8VpWOjBg7Jcv5CKensh?si=75a37f6000b34448"),
        "90s Sad Songs": (r"C:\Users\HP\Desktop\PYTHON\H sad2.jpg", "https://open.spotify.com/playlist/37i9dQZF1DWX7nMmBhSzhN?si=cde12b0fdb5b4b6d"),
        "Slow Sad Songs": (r"C:\Users\HP\Desktop\PYTHON\H sad3.jpg", "https://open.spotify.com/playlist/4rmMSaHl3t123Igxx8WXZc?si=956fe63c79784346"),
        "Mood Off Songs": (r"C:\Users\HP\Desktop\PYTHON\H sad4.jpg", "https://open.spotify.com/playlist/189Sow1xr7R94oSKs4kISc?si=5c51db7031ad491b")
    }

    # Display Bollywood playlists
    def display_playlists(data, frame):
        row = 0
        col = 0
        max_columns = 4
        for title, (img_path, url) in data.items():
            try:
                img = Image.open(img_path).resize((180, 180), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)

                # Image button
                btn = Button(
                    frame,
                    image=photo,
                    command=lambda u=url: open_spotify_playlist(u),
                    bd=0,
                    bg='#f2f2f7'
                )
                btn.image = photo
                btn.grid(row=row, column=col, padx=40, pady=(10, 5))

                # Playlist label
                lbl = Label(frame, text=title, width=20, anchor='center',
                            font=button_font, bg='#f2f2f7')
                lbl.grid(row=row+1, column=col)

                col += 1
                if col == max_columns:
                    col = 0
                    row += 2

            except Exception as e:
                print(f"Error loading {img_path}: {e}")

    display_playlists(bollywood_data, bollywood_frame)

    # === Section: Hollywood Playlists ===
    hollywood_heading = Label(main_frame, text="HOLLYWOOD PLAYLISTS", font=label_font, bg='#f2f2f7', fg='black')
    hollywood_heading.pack(pady=(60, 10))  # Extra space from the above section

    hollywood_frame = Frame(main_frame, bg='#f2f2f7')
    hollywood_frame.pack()

    hollywood_data = {
        "English Sad Songs": (r"C:\Users\HP\Desktop\PYTHON\E sad1.jpg", "https://open.spotify.com/playlist/1eRXF5lCwXzXArmtULo4Ji?si=f2a4ffdee3104114"),
        "Sad Melodies": (r"C:\Users\HP\Desktop\PYTHON\E sad2.jpg", "https://open.spotify.com/playlist/3XdEJhXoFpZKczSrEhutNB?si=8a1aa6a976284517"),
        "Sad Mix": (r"C:\Users\HP\Desktop\PYTHON\E sad 3.jpg", "https://open.spotify.com/playlist/4bRQf8bwAIVgCb6Lcoursx?si=5c82e9d53e884c30"),
        "Famous Sad Songs": (r"C:\Users\HP\Desktop\PYTHON\E sad4.jpg", "https://open.spotify.com/playlist/5qYMFV8EdILwgFbCwyG85Y?si=c0e2b0a2868a4e98")
    }

    display_playlists(hollywood_data, hollywood_frame)

    root.mainloop()