import tkinter as tk

class TutorialScreen(tk.Frame):
    def __init__(self, master, on_main_menu):
        super().__init__(master, bg="#83a5e0")
        self.on_main_menu = on_main_menu

        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        card = tk.Frame(self, bg="#ffffff", width=1250, height=550)
        card.place(relx=0.5, rely=0.5, anchor="center")

        title = tk.Label(
            card,
            text="How to Play",
            font=("Comic Sans MS", 36, "bold"),
            bg="white",
            fg="#0E151C",
        )
        title.pack(padx=(150, 150), pady=(40, 24))

        instructions = (
            "1. Press Play Clip to hear a random segment from a drum corps show\n"
            "2. Enter the show title, then select corps, year, and placement\n"
            "3. Press Submit to score your answer\n"
            "4. Use Hint to extend the clip or hear a different segment\n"
            "5. Press Next Question to continue"
        )

        body = tk.Label(
            card,
            text=instructions,
            font=("Arial", 16),
            justify="left",
            bg="white",
            fg="#2E3B4E",
            wraplength=900,
        )
        body.pack(padx=80, pady=(0, 36), anchor="w")

        back_button = tk.Button(
            card,
            text="Back to Main Menu",
            font=("Helvetica", 14),
            width=22,
            height=2,
            command=self.on_main_menu,
        )
        back_button.pack(pady=(0, 24))
