import tkinter as tk
from tkinter import messagebox


class MenuScreen(tk.Frame): #Inheriting from tk frame
    def __init__(self, master, on_play, on_tutorial, on_quit):
        super().__init__(master, bg="#83a5e0")
        self.on_play = on_play
        self.on_tutorial = on_tutorial
        self.on_quit = on_quit

        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        card = tk.Frame(self, bg="#ffffff", width=1250, height=550)
        card.place(relx=0.5, rely=0.5, anchor="center")

        title = tk.Label(
            card,
            text="DRUM CORPS QUIZ",
            font=("Comic Sans MS", 36, "bold"),
            bg="white",
            fg="#0E151C",
        )
        title.pack(padx=(100, 100), pady=(80, 40))

        button_frame = tk.Frame(card, bg="white")
        button_frame.pack()

        play_btn = tk.Button(
            button_frame,
            text="Play",
            font=("Helvetica", 14),
            width=20,
            height=2,
            command=self.on_play,
        )
        play_btn.pack(pady=8)

        how_to_play_btn = tk.Button(
            button_frame,
            text="How to Play",
            font=("Helvetica", 14),
            width=20,
            height=2,
            command=self.show_how_to_play,
        )
        how_to_play_btn.pack(pady=8)

        quit_btn = tk.Button(
            button_frame,
            text="Quit",
            font=("Helvetica", 14),
            width=20,
            height=2,
            command=self.on_quit,
        )
        quit_btn.pack(pady=(8, 100))

    def show_how_to_play(self):
        # messagebox.showinfo(
        #     "How to Play",
        #     "Listen to the clip and fill out all fields.\n"
        #     "Submit to score points.\n"
        #     "Hints let you extend the clip or play a different clip.",
        # )
        self.on_tutorial()
