from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from tkinter import font

def angry_mood():
    # Function to open a Spotify playlist in browser
    def open_spotify_playlist(url):
        webbrowser.open_new_tab(url)

    # Main window
    root = Toplevel()
    root.state('zoomed')
    root.configure(bg="#ffe6e6")
    root.geometry("2000x2000")

    # Fonts
    title_font = font.Font(family='Verdana', size=37, weight='bold')
    label_font = font.Font(family='Lucida Handwriting', size=30, weight='bold')
    button_font = font.Font(family='Georgia', size=15, weight='bold')

    # Navbar
    navbar = Frame(root, height=320, bg="#212121")
    navbar.pack(fill=X)
    navbar.pack_propagate(False)


    # Page title
    title_label = Label(navbar, text="Angry", font=title_font, bg="#212121", fg="white")
    title_label.grid(row=0, column=1, padx=(20,10), pady=(30,0))

    main_frame=Frame(root, height=720, bg="#ffe6e6")
    main_frame.pack(fill=X)
    main_frame.pack_propagate(False)

    # === Section: Bollywood Playlists ===
    bollywood_heading = Label(main_frame, text="BOLLYWOOD PLAYLISTS", font=label_font, bg="#ffe6e6", fg='black')
    bollywood_heading.pack(pady=(40, 10))

    bollywood_frame = Frame(main_frame, bg='#ffe6e6')
    bollywood_frame.pack()

    bollywood_data = {
        "Angry Bollywood Mix": (r"C:\Users\HP\Desktop\PYTHON\anger1.jpeg", "https://open.spotify.com/playlist/37i9dQZF1EIfX5bt1426JC?si=51bb71d264db43cc"),
        "Angry Hindi": (r"C:\Users\HP\Desktop\PYTHON\anger2.jpeg", "https://open.spotify.com/playlist/5cwtgqs4L1fX8IKoQebfjJ?si=c38def940a2048cd"),
        "Angry Bollywood": (r"C:\Users\HP\Desktop\PYTHON\anger3.jpeg", "https://open.spotify.com/playlist/39CyPnN7DhlY6eyaj7mI9P?si=b522da41171e4cca"),
        "Angry Hits": (r"C:\Users\HP\Desktop\PYTHON\anger4.jpeg", "https://open.spotify.com/playlist/3JNWpteYvH3ynMcyPcvxfx?si=5f6c14040bbb4384")
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
                    bg='#ffe6e6'
                )
                btn.image = photo
                btn.grid(row=row, column=col, padx=40, pady=(10, 5))

                # Playlist label
                lbl = Label(frame, text=title, width=20, anchor='center',
                            font=button_font, bg='#ffe6e6')
                lbl.grid(row=row+1, column=col)

                col += 1
                if col == max_columns:
                    col = 0
                    row += 2

            except Exception as e:
                print(f"Error loading {img_path}: {e}")

    display_playlists(bollywood_data, bollywood_frame)

    # === Section: Hollywood Playlists ===
    hollywood_heading = Label(main_frame, text="HOLLYWOOD PLAYLISTS", font=label_font, bg='#ffe6e6', fg='black')
    hollywood_heading.pack(pady=(60, 10))  # Extra space from the above section

    hollywood_frame = Frame(main_frame, bg='#ffe6e6')
    hollywood_frame.pack()

    hollywood_data = {
        "Workout Hollywood": (r"C:\Users\HP\Desktop\PYTHON\anger5.jpeg", "https://open.spotify.com/playlist/2rKMuMpcl2n19fIUk8uLrD?si=c7aa7035e47647fb"),
        "Hollywood Attitude": (r"C:\Users\HP\Desktop\PYTHON\anger6.jpeg", "https://open.spotify.com/playlist/7EKxlcggWPLagSfwaLUn8G?si=a93de5618f8e4ee0"),
        "Gym BGMs": (r"C:\Users\HP\Desktop\PYTHON\anger7.jpeg", "https://open.spotify.com/playlist/0cutTwIrm9U5xZD6hJFI4S?si=fdeb3f77ea704fb1"),
        "Angry Hollywood Mix": (r"C:\Users\HP\Desktop\PYTHON\anger8.jpeg", "https://open.spotify.com/playlist/37i9dQZF1EId6LemDu4tIr?si=cdc9e053a9e94081")
    }

    display_playlists(hollywood_data, hollywood_frame)

    root.mainloop()