from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from tkinter import font

def energetic_mood():
    # Function to open a Spotify playlist in browser
    def open_spotify_playlist(url):
        webbrowser.open_new_tab(url)

    # Main window
    root = Toplevel()
    root.state('zoomed')
    root.configure(bg='#fff3e0')
    root.geometry("2000x2000")

    # Fonts
    title_font = font.Font(family='Verdana', size=37, weight='bold')
    label_font = font.Font(family='Lucida Handwriting', size=30, weight='bold')
    button_font = font.Font(family='Georgia', size=15, weight='bold')

    # Navbar
    navbar = Frame(root, height=320, bg="#ff6b00")
    navbar.pack(fill=X)
    navbar.pack_propagate(False)


    # Page title
    title_label = Label(navbar, text="Energetic", font=title_font, bg="#ff6b00", fg='black')
    title_label.grid(row=0, column=1, padx=(20,10), pady=(30,0))

    main_frame=Frame(root, height=720, bg='#fff3e0')
    main_frame.pack(fill=X)
    main_frame.pack_propagate(False)

    # === Section: Bollywood Playlists ===
    bollywood_heading = Label(main_frame, text="BOLLYWOOD PLAYLISTS", font=label_font, bg='#fff3e0', fg='black')
    bollywood_heading.pack(pady=(40, 10))

    bollywood_frame = Frame(main_frame, bg='#fff3e0')
    bollywood_frame.pack()

    bollywood_data = {
        "Energetic Bollywood Songs": (r"C:\Users\HP\Desktop\PYTHON\energy1.jpeg", "https://open.spotify.com/playlist/3mSm688yR6UeaAJNf93Ydr?si=a0b6b91baba14605"),
        "Full Energetic Songs ": (r"C:\Users\HP\Desktop\PYTHON\energy2.jpeg", "https://open.spotify.com/playlist/6UHDg40qRGVcuPq6hyeFr9?si=5a54bb3c0d514106"),
        "Dance Songs": (r"C:\Users\HP\Desktop\PYTHON\energy3.jpeg", "https://open.spotify.com/playlist/6ESPf8CVmQyYF4UnVAU6nO?si=293c75915cdc4488"),
        "Energy Hits": (r"C:\Users\HP\Desktop\PYTHON\energy4.jpeg", "https://open.spotify.com/playlist/2r79iyvrtYuYAVsJTxFEAq?si=0de4e9c1e8804d84")
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
                    bg='#fff3e0'
                )
                btn.image = photo
                btn.grid(row=row, column=col, padx=40, pady=(10, 5))

                # Playlist label
                lbl = Label(frame, text=title, width=20, anchor='center',
                            font=button_font, bg='#fff3e0')
                lbl.grid(row=row+1, column=col)

                col += 1
                if col == max_columns:
                    col = 0
                    row += 2

            except Exception as e:
                print(f"Error loading {img_path}: {e}")

    display_playlists(bollywood_data, bollywood_frame)

    # === Section: Hollywood Playlists ===
    hollywood_heading = Label(main_frame, text="HOLLYWOOD PLAYLISTS", font=label_font, bg='#fff3e0', fg='black')
    hollywood_heading.pack(pady=(60, 10))  # Extra space from the above section

    hollywood_frame = Frame(main_frame, bg='#fff3e0')
    hollywood_frame.pack()

    hollywood_data = {
        "Top Energetic Songs": (r"C:\Users\HP\Desktop\PYTHON\energy5.1.jpeg", "https://open.spotify.com/playlist/15frAGqH4sr6pMRzReGOq4?si=7be6a83daa0a4a6b"),
        "Energetic English Songs": (r"C:\Users\HP\Desktop\PYTHON\energy7.jpg", "https://open.spotify.com/playlist/3WYmyXrEqRL1UnV3ep13ie?si=e7f17421194f4528"),
        "Hollywood Dance Songs": (r"C:\Users\HP\Desktop\PYTHON\energy7.1.jpeg", "https://open.spotify.com/playlist/1Om3sf86Iicnw0e4urzBme?si=4d31a126b7e348b2"),
        "Party Songs": (r"C:\Users\HP\Desktop\PYTHON\energy8.1.jpeg", "https://open.spotify.com/playlist/3asnW8rKfPlhHH52D8rz7W?si=da275d595f1f4f03")
    }

    display_playlists(hollywood_data, hollywood_frame)

    root.mainloop()