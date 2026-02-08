from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from tkinter import font

def romantic_mood():
    # Function to open a Spotify playlist in browser
    def open_spotify_playlist(url):
        webbrowser.open_new_tab(url)

    # Main window
    root = Toplevel()
    root.state('zoomed')
    root.configure(bg='#fdf0f0')
    root.geometry("2000x2000")

    # Fonts
    title_font = font.Font(family='Verdana', size=37, weight='bold')
    label_font = font.Font(family='Lucida Handwriting', size=30, weight='bold')
    button_font = font.Font(family='Georgia', size=15, weight='bold')

    # Navbar
    navbar = Frame(root, height=320, bg="#d62828")
    navbar.pack(fill=X)
    navbar.pack_propagate(False)


    # Page title
    title_label = Label(navbar, text="Romantic", font=title_font, bg="#d62828", fg='black')
    title_label.grid(row=0, column=1, padx=(20,10), pady=(30,0))

    main_frame=Frame(root, height=720, bg="#fdf0f0")
    main_frame.pack(fill=X)
    main_frame.pack_propagate(False)

    # === Section: Bollywood Playlists ===
    bollywood_heading = Label(main_frame, text="BOLLYWOOD PLAYLISTS", font=label_font, bg="#fdf0f0", fg='black')
    bollywood_heading.pack(pady=(40, 10))

    bollywood_frame = Frame(main_frame, bg='#fdf0f0')
    bollywood_frame.pack()

    bollywood_data = {
        "Best Hindi Romantic Songs ": (r"C:\Users\HP\Desktop\PYTHON\Roman1.jpg", "https://open.spotify.com/playlist/0zc6Hq9OIAengtGG6a3lfs?si=bca65058967f4601"),
        "90s Romantic Hits": (r"C:\Users\HP\Desktop\PYTHON\Roman2.jpg", "https://open.spotify.com/playlist/6hjdzV2vocEMhUqkN9TL7h?si=937ac2db124d4ac4"),
        "Monsoon Romatics": (r"C:\Users\HP\Desktop\PYTHON\Roman3.jpg", "https://open.spotify.com/playlist/4Nzx9FED47snxQqBY85nis?si=ce6a17f63dcd476e"),
        "Late Night Romantic Vibes": (r"C:\Users\HP\Desktop\PYTHON\Roman4.jpg", "https://open.spotify.com/playlist/2VInJrpDJ67aiCIDDY7WQP?si=1ff6f41f78494fba")
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
                    bg='#fdf0f0'
                )
                btn.image = photo
                btn.grid(row=row, column=col, padx=40, pady=(10, 5))

                # Playlist label
                lbl = Label(frame, text=title, width=20, anchor='center',
                            font=button_font, bg='#fdf0f0')
                lbl.grid(row=row+1, column=col)

                col += 1
                if col == max_columns:
                    col = 0
                    row += 2

            except Exception as e:
                print(f"Error loading {img_path}: {e}")

    display_playlists(bollywood_data, bollywood_frame)

    # === Section: Hollywood Playlists ===
    hollywood_heading = Label(main_frame, text="HOLLYWOOD PLAYLISTS", font=label_font, bg='#fdf0f0', fg='black')
    hollywood_heading.pack(pady=(60, 10))  # Extra space from the above section

    hollywood_frame = Frame(main_frame, bg='#fdf0f0')
    hollywood_frame.pack()

    hollywood_data = {
        "Slow Soothing Romantics": (r"C:\Users\HP\Desktop\PYTHON\RomanH1.jpg", "https://open.spotify.com/playlist/4uRWiTswXyOJVgqoueqnkT?si=dde76e140aea4974"),
        "Old Romantic Songs": (r"C:\Users\HP\Desktop\PYTHON\RomanH2.jpg", "https://open.spotify.com/playlist/4uRWiTswXyOJVgqoueqnkT?si=dde76e140aea4974"),
        "Hollywood Romantic Songs": (r"C:\Users\HP\Desktop\PYTHON\RomanH3.jpg", "https://open.spotify.com/playlist/5QEFBVZZSjbaBLFda4DwGc?si=82c121c763f247de"),
        "Romantic English Songs": (r"C:\Users\HP\Desktop\PYTHON\RomanH4.jpg", "https://open.spotify.com/playlist/1jQQCX7rHfXT8dhZPyv5y4?si=983a58bd24af47d5")
    }

    display_playlists(hollywood_data, hollywood_frame)

    root.mainloop()