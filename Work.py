from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from tkinter import font

def work_mood():
    # Function to open a Spotify playlist in browser
    def open_spotify_playlist(url):
        webbrowser.open_new_tab(url)

    # Main window
    root = Toplevel()
    root.state('zoomed')
    root.configure(bg="#ede7f6")
    root.geometry("2000x2000")

    # Fonts
    title_font = font.Font(family='Verdana', size=37, weight='bold')
    label_font = font.Font(family='Lucida Handwriting', size=30, weight='bold')
    button_font = font.Font(family='Georgia', size=15, weight='bold')

    # Navbar
    navbar = Frame(root, height=320, bg="#9514c0")
    navbar.pack(fill=X)
    navbar.pack_propagate(False)


    # Page title
    title_label = Label(navbar, text="Work", font=title_font, bg="#9514c0", fg="white")
    title_label.grid(row=0, column=1, padx=(20,10), pady=(30,0))

    main_frame=Frame(root, height=720, bg="#ede7f6")
    main_frame.pack(fill=X)
    main_frame.pack_propagate(False)

    # === Section: Bollywood Playlists ===
    bollywood_heading = Label(main_frame, text="BOLLYWOOD PLAYLISTS", font=label_font, bg="#ede7f6", fg='black')
    bollywood_heading.pack(pady=(40, 10))

    bollywood_frame = Frame(main_frame, bg='#ede7f6')
    bollywood_frame.pack()

    bollywood_data = {
        "Study Music(LOFI)": (r"C:\Users\HP\Desktop\PYTHON\work1.jpeg", "https://open.spotify.com/playlist/38mWQAGEylOPPcWfDpB6FO?si=ccd2b10397d84892"),
        "Bollywood (LOFI)": (r"C:\Users\HP\Desktop\PYTHON\work2.jpeg", "https://open.spotify.com/playlist/2PyXlxtxe02oC3iTO9Gnt0?si=31ab64a6d33e45fc"),
        "Focus- Binaural Beats": (r"C:\Users\HP\Desktop\PYTHON\binaural.jpeg", "https://open.spotify.com/playlist/2F6LyTRo99Hy7ayFFLso9t?si=cf6b86045dfc43f2"),
        "Gamma Waves- Study Music": (r"C:\Users\HP\Desktop\PYTHON\gamma.jpeg", "https://open.spotify.com/playlist/7MHZ2A5yvvqlqHZZlc5k86?si=deed2f63b71e478d")
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
                    bg='#ede7f6'
                )
                btn.image = photo
                btn.grid(row=row, column=col, padx=40, pady=(10, 5))

                # Playlist label
                lbl = Label(frame, text=title, width=20, anchor='center',
                            font=button_font, bg='#ede7f6')
                lbl.grid(row=row+1, column=col)

                col += 1
                if col == max_columns:
                    col = 0
                    row += 2

            except Exception as e:
                print(f"Error loading {img_path}: {e}")

    display_playlists(bollywood_data, bollywood_frame)

    # === Section: Hollywood Playlists ===
    hollywood_heading = Label(main_frame, text="HOLLYWOOD PLAYLISTS", font=label_font, bg='#ede7f6', fg='black')
    hollywood_heading.pack(pady=(60, 10))  # Extra space from the above section

    hollywood_frame = Frame(main_frame, bg='#ede7f6')
    hollywood_frame.pack()

    hollywood_data = {
        "Music for Work": (r"C:\Users\HP\Desktop\PYTHON\work3.jpeg", "https://open.spotify.com/playlist/0ys1ut3I2CwJoofncTft9k?si=e5f3d29078034e38"),
        "Work Music": (r"C:\Users\HP\Desktop\PYTHON\work4.jpeg", "https://open.spotify.com/playlist/6X185BlQApNN7mjiFFhPdi?si=9cd3dd8c6e914ead"),
        "Hollywood LOFI": (r"C:\Users\HP\Desktop\PYTHON\work5.jpeg", "https://open.spotify.com/playlist/5gZY9a5H7nOiOTyyNi8PC4?si=d3791f098ea64f41"),
        "Working Mood": (r"C:\Users\HP\Desktop\PYTHON\work6.jpeg", "https://open.spotify.com/playlist/2Y3C19yYZUze4MI2OIA2kK?si=bbf409a3878d49dd")
    }

    display_playlists(hollywood_data, hollywood_frame)

    root.mainloop()