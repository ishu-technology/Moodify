from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from tkinter import font

def calm_mood():
    # Function to open a Spotify playlist in browser
    def open_spotify_playlist(url):
        webbrowser.open_new_tab(url)

    # Main window
    root = Toplevel()
    root.state('zoomed')
    root.configure(bg="#fefae0")
    root.geometry("2000x2000")

    # Fonts
    title_font = font.Font(family='Verdana', size=37, weight='bold')
    label_font = font.Font(family='Lucida Handwriting', size=30, weight='bold')
    button_font = font.Font(family='Georgia', size=15, weight='bold')

    # Navbar
    navbar = Frame(root, height=320, bg="#a3b18a")
    navbar.pack(fill=X)
    navbar.pack_propagate(False)


    # Page title
    title_label = Label(navbar, text="Calm", font=title_font, bg="#a3b18a", fg="#344e41")
    title_label.grid(row=0, column=1, padx=(20,10), pady=(30,0))

    main_frame=Frame(root, height=720, bg="#fefae0")
    main_frame.pack(fill=X)
    main_frame.pack_propagate(False)

    # === Section: Bollywood Playlists ===
    bollywood_heading = Label(main_frame, text="BOLLYWOOD PLAYLISTS", font=label_font, bg="#fefae0", fg='black')
    bollywood_heading.pack(pady=(40, 10))

    bollywood_frame = Frame(main_frame, bg='#fefae0')
    bollywood_frame.pack()

    bollywood_data = {
        "Calming Hindi Songs": (r"C:\Users\HP\Desktop\PYTHON\calm1.jpeg", "https://open.spotify.com/playlist/1Dk9SeguLL5qTnjfyX5VnZ?si=c8af11f0e1b44661"),
        "Peaceful Hindi Songs": (r"C:\Users\HP\Desktop\PYTHON\calm2.jpeg", "https://open.spotify.com/playlist/02uXGKglrYZD67gcyxkvTd?si=7065abc866fc46e3"),
        "Chill Songs": (r"C:\Users\HP\Desktop\PYTHON\calm3.jpeg", "https://open.spotify.com/playlist/6hQSibEcPYWfiQ3pTxfXCK?si=aebf0698e37e4d43"),
        "Soothing Songs": (r"C:\Users\HP\Desktop\PYTHON\calm4.jpg", "https://open.spotify.com/playlist/5ZbrCXwZktrc69OuUWXnvp?si=5d7e9d12321a4a19")
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
                    bg='#fefae0'
                )
                btn.image = photo
                btn.grid(row=row, column=col, padx=40, pady=(10, 5))

                # Playlist label
                lbl = Label(frame, text=title, width=20, anchor='center',
                            font=button_font, bg='#fefae0')
                lbl.grid(row=row+1, column=col)

                col += 1
                if col == max_columns:
                    col = 0
                    row += 2

            except Exception as e:
                print(f"Error loading {img_path}: {e}")

    display_playlists(bollywood_data, bollywood_frame)

    # === Section: Hollywood Playlists ===
    hollywood_heading = Label(main_frame, text="HOLLYWOOD PLAYLISTS", font=label_font, bg='#fefae0', fg='black')
    hollywood_heading.pack(pady=(60, 10))  # Extra space from the above section

    hollywood_frame = Frame(main_frame, bg='#fefae0')
    hollywood_frame.pack()

    hollywood_data = {
        "Calming English Songs": (r"C:\Users\HP\Desktop\PYTHON\calm5.jpeg", "https://open.spotify.com/playlist/4kOdiP5gbzocwxQ8s2UTOF?si=5a21766f31234a5a"),
        "Calm Mood Songs": (r"C:\Users\HP\Desktop\PYTHON\calm6.1.jpg", "https://open.spotify.com/playlist/0cj48sijCRDJ3Hatx1k1vJ?si=3e7b4fbde70749dd"),
        "3AM Calm Mood Songs ": (r"C:\Users\HP\Desktop\PYTHON\calm6.jpg", "https://open.spotify.com/playlist/1tzweQpB1UBhnNKMwvv6cs?si=814ad975db62409a"),
        "Soft Songs": (r"C:\Users\HP\Desktop\PYTHON\calm8.jpeg", "https://open.spotify.com/playlist/1NIlouPwHi81SPIfHf213T?si=37c5898655c84a59")
    }

    display_playlists(hollywood_data, hollywood_frame)

    root.mainloop()