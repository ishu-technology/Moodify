from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from tkinter import font

def happy_mood():
# Function to open a Spotify playlist in browser
    def open_spotify_playlist(url):
        webbrowser.open_new_tab(url)

    # Main window
    root = Toplevel()
    root.state('zoomed')
    root.configure(bg='lemon chiffon')
    root.geometry("2000x2000")

    # Fonts
    title_font = font.Font(family='Verdana', size=37, weight='bold')
    label_font = font.Font(family='Lucida Handwriting', size=30, weight='bold')
    button_font = font.Font(family='Georgia', size=15, weight='bold')

    # Navbar
    navbar = Frame(root, height=320, bg="khaki")
    navbar.pack(fill=X)
    navbar.pack_propagate(False)


    # Page title
    title_label = Label(navbar, text="Happy", font=title_font, bg="khaki", fg='black')
    title_label.grid(row=0, column=1, padx=(20,10), pady=(30,0))

    main_frame=Frame(root, height=720, bg='lemon chiffon')
    main_frame.pack(fill=X)
    main_frame.pack_propagate(False)

    # === Section: Bollywood Playlists ===
    bollywood_heading = Label(main_frame, text="BOLLYWOOD PLAYLISTS", font=label_font, bg='lemon chiffon', fg='black')
    bollywood_heading.pack(pady=(40, 10))

    bollywood_frame = Frame(main_frame, bg='lemon chiffon')
    bollywood_frame.pack()

    bollywood_data = {
        "Happy Bollywood songs": (r"C:\Users\HP\Desktop\PYTHON\Happy Bollywood Songs.jpg", "https://open.spotify.com/playlist/4WDPg2iGfEQ5XyUi1Ag4Ih?si=26c2238b33fa48ff"),
        "Feel Good Vibes": (r"C:\Users\HP\Desktop\PYTHON\Happy Feel Good Vibes .jpg", "https://open.spotify.com/playlist/36IzPSaa309M1wiy9GbPrL?si=f471c217385e4c75"),
        "Happy Vibes": (r"C:\Users\HP\Desktop\PYTHON\Happy vibes.jpg", "https://open.spotify.com/playlist/37i9dQZF1DWTwbZHrJRIgD?si=a783868ebe87422f"),
        "2000s Happy hits": (r"C:\Users\HP\Desktop\PYTHON\2000s happy Hits.jpg", "https://open.spotify.com/playlist/6UVwQYZWhFzsVedlpvZdms?si=806a07dfd8124c50")
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
                    bg='lemon chiffon'
                )
                btn.image = photo
                btn.grid(row=row, column=col, padx=40, pady=(10, 5))

                # Playlist label
                lbl = Label(frame, text=title, width=20, anchor='center',
                            font=button_font, bg='lemon chiffon')
                lbl.grid(row=row+1, column=col)

                col += 1
                if col == max_columns:
                    col = 0
                    row += 2

            except Exception as e:
                print(f"Error loading {img_path}: {e}")

    display_playlists(bollywood_data, bollywood_frame)

    # === Section: Hollywood Playlists ===
    hollywood_heading = Label(main_frame, text="HOLLYWOOD PLAYLISTS", font=label_font, bg='lemon chiffon', fg='black')
    hollywood_heading.pack(pady=(60, 10))  # Extra space from the above section

    hollywood_frame = Frame(main_frame, bg='lemon chiffon')
    hollywood_frame.pack()

    hollywood_data = {
        "Happy English Songs": (r"C:\Users\HP\Desktop\PYTHON\happy english songs.jpg", "https://open.spotify.com/playlist/0jrlHA5UmxRxJjoykf7qRY?si=95607b145d1c452f"),
        "Happy Pop Hits": (r"C:\Users\HP\Desktop\PYTHON\Pop hits.jpg", "https://open.spotify.com/playlist/2eXyhdV1QLryeHEelWmgTd?si=03726b1cdf524211"),
        "Dance & Smile": (r"C:\Users\HP\Desktop\PYTHON\dance and smile.jpg", "https://open.spotify.com/playlist/3YVyKaJWI4u3L612UkimdV?si=17ec8e5f6a8f4280"),
        "Feel Good Songs": (r"C:\Users\HP\Desktop\PYTHON\feel good songs.jpg", "https://open.spotify.com/playlist/4WUzI80bEpc3mvB25ZmiGe?si=c0c481d61ed14b3a")
    }

    display_playlists(hollywood_data, hollywood_frame)

    root.mainloop()