import tkinter as tk
from tkinter import messagebox
import os

class MenuScreen(tk.Frame): #Inheriting from tk frame
    def __init__(self, master, on_play, on_tutorial, on_quit):
        super().__init__(master, bg="#83a5e0")
        self.on_play = on_play
        self.on_tutorial = on_tutorial
        self.on_quit = on_quit

        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        trumpet_left_path = os.path.join(base_dir, "gui_files", "images", "trumpet_left.png")
        trumpet_right_path = os.path.join(base_dir, "gui_files", "images", "trumpet_right.png")

        self.trumpet_left_img = tk.PhotoImage(file=trumpet_left_path).subsample(8, 8)
        self.trumpet_right_img = tk.PhotoImage(file=trumpet_right_path).subsample(8, 8)

        card = tk.Frame(self, bg="#ffffff", width=1250, height=550)
        card.place(relx=0.5, rely=0.5, anchor="center")

        title_row = tk.Frame(card, bg="white")
        title_row.pack(pady=(80, 40))

        left_trumpet = tk.Label(title_row, image=self.trumpet_left_img, bg="white")
        left_trumpet.pack(side="left", padx=(0, 18))

        title = tk.Label(
            title_row,
            text="DRUM CORPS QUIZ",
            font=("Comic Sans MS", 36, "bold"),
            bg="white",
            fg="#0E151C",
        )
        title.pack(side="left")

        right_trumpet = tk.Label(title_row, image=self.trumpet_right_img, bg="white")
        right_trumpet.pack(side="left", padx=(18, 0))

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
