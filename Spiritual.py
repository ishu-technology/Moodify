from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from tkinter import font

def spiritual_mood():
    # Function to open a Spotify playlist in browser
    def open_spotify_playlist(url):
        webbrowser.open_new_tab(url)

    # Main window
    root = Toplevel()
    root.state('zoomed')
    root.configure(bg="#f1f8e9")
    root.geometry("2000x2000")

    # Fonts
    title_font = font.Font(family='Verdana', size=37, weight='bold')
    label_font = font.Font(family='Lucida Handwriting', size=30, weight='bold')
    button_font = font.Font(family='Georgia', size=15, weight='bold')

    # Navbar
    navbar = Frame(root, height=320, bg="#4caf50")
    navbar.pack(fill=X)
    navbar.pack_propagate(False)


    # Page title
    title_label = Label(navbar, text="Spiritual", font=title_font, bg="#4caf50", fg="white")
    title_label.grid(row=0, column=1, padx=(20,10), pady=(30,0))

    main_frame=Frame(root, height=720, bg="#f1f8e9")
    main_frame.pack(fill=X)
    main_frame.pack_propagate(False)

    # === Section: Bollywood Playlists ===
    bollywood_heading = Label(main_frame, text="BOLLYWOOD PLAYLISTS", font=label_font, bg="#f1f8e9", fg='black')
    bollywood_heading.pack(pady=(40, 10))

    bollywood_frame = Frame(main_frame, bg='#f1f8e9')
    bollywood_frame.pack()

    bollywood_data = {
        "Spiritual Hindi Songs": (r"C:\Users\HP\Desktop\PYTHON\Spirit1.jpg", "https://open.spotify.com/playlist/2Se01pTkJoo41myYBBikPd?si=23090f02051447bc"),
        "Bollywood Spiritual": (r"C:\Users\HP\Desktop\PYTHON\Spirit2.jpg", "https://open.spotify.com/playlist/2UjDkx6qO5QvvvUFQeKV2N?si=d3d14d79aaa04bc5"),
        "Spiritual Sounds": (r"C:\Users\HP\Desktop\PYTHON\Spirit3.jpeg", "https://open.spotify.com/playlist/0cELuDbnKCAK4rM0TwAFIM?si=e3370814e7b14030"),
        "Binaural Beats": (r"C:\Users\HP\Desktop\PYTHON\Spirit4.jpeg", "https://open.spotify.com/playlist/37i9dQZF1DX5Tgh3tlyc3X?si=4964575166d94279")
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
                    bg='#f1f8e9'
                )
                btn.image = photo
                btn.grid(row=row, column=col, padx=40, pady=(10, 5))

                # Playlist label
                lbl = Label(frame, text=title, width=20, anchor='center',
                            font=button_font, bg='#f1f8e9')
                lbl.grid(row=row+1, column=col)

                col += 1
                if col == max_columns:
                    col = 0
                    row += 2

            except Exception as e:
                print(f"Error loading {img_path}: {e}")

    display_playlists(bollywood_data, bollywood_frame)

    # === Section: Hollywood Playlists ===
    hollywood_heading = Label(main_frame, text="HOLLYWOOD PLAYLISTS", font=label_font, bg='#f1f8e9', fg='black')
    hollywood_heading.pack(pady=(60, 10))  # Extra space from the above section

    hollywood_frame = Frame(main_frame, bg='#f1f8e9')
    hollywood_frame.pack()

    hollywood_data = {
        "English Spiritual Songs": (r"C:\Users\HP\Desktop\PYTHON\spirit5.jpeg", "https://open.spotify.com/playlist/5BmLQniq0BDkdSD6VDB2Mn?si=15767db39c824cc2"),
        "Christian Spiritual Songs": (r"C:\Users\HP\Desktop\PYTHON\spirit6.jpg", "https://open.spotify.com/playlist/5JkA3jxSvQ7bS7Ua45I1QE?si=42212d1ea4ac4e84"),
        "Spiritual Mix": (r"C:\Users\HP\Desktop\PYTHON\spirit7.1.jpg", "https://open.spotify.com/playlist/0cmYCUP8kX2sUAVjPGdrOS?si=2bebbbad4e3c4e86"),
        "Spiritual Devotional Mix": (r"C:\Users\HP\Desktop\PYTHON\spirit8.1.jpg", "https://open.spotify.com/playlist/2wkV1jk8JP8iwRWZOzzBy5?si=95ada3ade7224f89")
    }

    display_playlists(hollywood_data, hollywood_frame)

    root.mainloop()