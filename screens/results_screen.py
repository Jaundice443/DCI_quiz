import tkinter as tk


class ResultsScreen(tk.Frame):
    def __init__(self, master, on_main_menu, on_quiz_start):
        super().__init__(master, bg="#83a5e0")
        self.on_main_menu = on_main_menu
        self.on_quiz_start = on_quiz_start

        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        card = tk.Frame(self, bg="#ffffff", width=1250, height=550)
        card.place(relx=0.5, rely=0.5, anchor="center")

        title = tk.Label(
            card,
            text="RESULTS",
            font=("Comic Sans MS", 36, "bold"),
            bg="white",
            fg="#0E151C",
        )
        title.pack(padx=(200, 200), pady=(30, 24))

        self.score_label = tk.Label(
            card,
            text="Total Points Earned: 0",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="#0E151C",
        )
        self.score_label.pack(pady=(0, 12))

        self.detail_label = tk.Label(
            card,
            text="",
            font=("Arial", 13),
            bg="white",
            fg="#2E3B4E",
        )
        self.detail_label.pack(pady=(0, 28))

        self.completion_frame = tk.Frame(card, bg="white")
        self.completion_frame.pack(anchor="n")

        self.replay_button = tk.Button(
            self.completion_frame,
            text="⟲ Replay Quiz",
            font=("Helvetica", 13),
            width=20,
            height=2,
            command=self.on_quiz_start,
        )
        self.replay_button.pack(pady=(0, 12))

        self.menu_button = tk.Button(
            self.completion_frame,
            text="Back to Main Menu",
            font=("Helvetica", 13),
            width=20,
            height=2,
            command=self.on_main_menu,
        )
        self.menu_button.pack(pady=(0,20))

    def update_results(self, total_points, max_points):
        self.score_label.config(text=f"Total Points Earned: {total_points}")
        self.detail_label.config(text=f"Final Score: {total_points}/{max_points}")
