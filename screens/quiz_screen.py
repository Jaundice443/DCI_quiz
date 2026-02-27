import os
import tkinter as tk
from tkinter import ttk

from audio import create_random_clip, get_duration, play_clip, stop_audio
from quiz_logic import (
    CLIP_LENGTH,
    QuizQuestion,
    get_corps_options,
    get_placement_options,
    get_year_options,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class QuizScreen(tk.Frame):
    def __init__(self, master, on_main_menu, on_complete):
        super().__init__(master, bg="#83a5e0")
        self.on_main_menu = on_main_menu
        self.on_complete = on_complete
        self.quiz = QuizQuestion()

        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        self.correct_img = tk.PhotoImage(
            file=os.path.join(BASE_DIR, "gui_files", "images", "correct.png")
        )
        self.incorrect_img = tk.PhotoImage(
            file=os.path.join(BASE_DIR, "gui_files", "images", "incorrect.png")
        )
        self.blank_img = tk.PhotoImage()

        self._build_ui()
        self.start_new_quiz()

    def _build_ui(self):
        card = tk.Frame(self, bg="#ffffff", width=825, height=550)
        card.place(relx=0.5, rely=0.5, anchor="center")

        title = tk.Label(
            card,
            text="DRUM CORPS QUIZ",
            font=("Comic Sans MS", 30, "bold"),
            bg="white",
            fg="#0E151C",
        )
        title.pack(pady=20)

        header_row = tk.Frame(card, bg="white")
        header_row.pack(fill="x", padx=40, pady=(0, 10))
        header_row.grid_columnconfigure(0, weight=1)
        header_row.grid_columnconfigure(1, weight=0)
        header_row.grid_columnconfigure(2, weight=1)

        self.question_label = tk.Label(
            header_row,
            text="Question",
            font=("Arial", 12),
            bg="white",
            fg="#0E151C",
        )
        self.question_label.grid(row=0, column=1)

        self.total_points_label = tk.Label(
            header_row,
            text="Total Points: 0",
            font=("Arial", 12, "bold"),
            justify="left",
            fg="black",
            bg="white",
        )
        self.total_points_label.grid(row=0, column=2, sticky="w", padx=(10, 0))

        content_row = tk.Frame(card, bg="white")
        content_row.pack(pady=10, fill="x")

        # Input side
        left_frame = tk.Frame(content_row, bg="white")
        left_frame.pack(side="left", padx=(50, 40), anchor="n")

        # Results side
        right_frame = tk.Frame(content_row, bg="white")
        right_frame.pack(side="left", padx=(40, 60), anchor="n")

        self.feedback_label = tk.Label(
            right_frame,
            text="",
            font=("Arial", 12),
            justify="left",
            wraplength=300,
            fg="black",
            bg="white",
        )
        self.feedback_label.pack(anchor="n")

        tk.Label(
            left_frame,
            text="Enter Show Title:",
            justify="left",
            bg="white",
        ).grid(row=0, column=0, padx=(20, 5), sticky="w")

        self.show_title_var = tk.StringVar()
        self.title_entry = tk.Entry(
            left_frame,
            textvariable=self.show_title_var,
            width=43,
            relief="groove",  # style of border: solid, groove, ridge, sunken, raised
            highlightthickness=1,  # outline thickness for focus
            highlightbackground="grey",  # outline color when not focused
            # highlightcolor="blue" # outline color when focused
        )
        self.title_entry.grid(row=1, column=0, padx=(20, 5), pady=(0, 10), sticky="w")
        self.title_entry.config(fg="black")

        self.title_mark = tk.Label(left_frame, image=self.blank_img, bg="white")
        self.title_mark.grid(row=1, column=1, padx=(5, 20), pady=(0, 10))

        self.corps_var = tk.StringVar()
        self.corps_dropdown = ttk.Combobox(
            left_frame,
            textvariable=self.corps_var,
            state="readonly",
            width=40,
            values=get_corps_options(),
        )
        self.corps_dropdown.grid(row=2, column=0, padx=(20, 5), pady=10, sticky="w")

        self.corps_mark = tk.Label(left_frame, image=self.blank_img, bg="white")
        self.corps_mark.grid(row=2, column=1, padx=(5, 20))

        self.year_var = tk.StringVar()
        self.year_dropdown = ttk.Combobox(
            left_frame,
            textvariable=self.year_var,
            state="readonly",
            width=40,
            values=get_year_options(),
        )
        self.year_dropdown.grid(row=3, column=0, padx=(20, 5), pady=10, sticky="w")

        self.year_mark = tk.Label(left_frame, image=self.blank_img, bg="white")
        self.year_mark.grid(row=3, column=1, padx=(5, 20))

        self.placement_var = tk.StringVar()
        self.placement_dropdown = ttk.Combobox(
            left_frame,
            textvariable=self.placement_var,
            state="readonly",
            width=40,
            values=get_placement_options(),
        )
        self.placement_dropdown.grid(row=4, column=0, padx=(20, 5), pady=10, sticky="w")

        self.placement_mark = tk.Label(left_frame, image=self.blank_img, bg="white")
        self.placement_mark.grid(row=4, column=1, padx=(5, 20))

        button_frame = tk.Frame(card, bg="white")
        button_frame.pack(pady=20)

        self.play_btn = tk.Button(
            button_frame,
            text="▶ Play Clip",
            font=("Helvetica", 12),
            width=15,
            command=self.start_playback,
        )
        self.play_btn.grid(row=0, column=0, padx=10)

        self.submit_btn = tk.Button(
            button_frame,
            text="✔ Submit",
            font=("Helvetica", 12),
            width=15,
            command=self.on_submit,
        )
        self.submit_btn.grid(row=0, column=1, padx=10)

        self.hint_btn = tk.Button(
            button_frame,
            text="💡 Hint",
            font=("Helvetica", 12),
            width=15,
            command=self.on_hint,
        )
        self.hint_btn.grid(row=0, column=2, padx=10)

        self.next_button = tk.Button(
            button_frame,
            text=">> Next Question",
            font=("Helvetica", 12),
            width=15,
            command=self.next_question,
        )
        self.next_button.grid(row=0, column=3, padx=10)

        self.hint_menu = tk.Menu(self, tearoff=0)
        self.hint_menu.add_command(label="Extend clip", command=self.extend_clip)
        self.hint_menu.add_command(label="Play different clip", command=self.different_clip)

    # ___________________FUNCTIONS_______________________

    def _reset_answer_inputs(self):
        self.show_title_var.set("")
        self.corps_var.set("Select Corps")
        self.year_var.set("Select Year")
        self.placement_var.set("Select Placement")

        # Reset icons
        self.title_mark.config(image=self.blank_img)
        self.corps_mark.config(image=self.blank_img)
        self.year_mark.config(image=self.blank_img)
        self.placement_mark.config(image=self.blank_img)

    def start_new_quiz(self):
        stop_audio()
        self.quiz = QuizQuestion()

        self._reset_answer_inputs()
        self.feedback_label.config(text="")
        self.question_label.config(
            text=f"Question {self.quiz.question_index}/{self.quiz.num_rounds}"
        )
        self.total_points_label.config(text=f"Total Points: {self.quiz.total_points}")

        self.submit_btn.config(state="normal")
        self.play_btn.config(state="normal")
        self.hint_btn.config(state="normal")
        self.next_button.config(state="normal")

        # self._hide_completion_actions()

    def start_playback(self, start=None, clip_length=None):
        # self.play_btn.config(state="disabled")
        # self.hint_btn.config(state="disabled")

        if start is None:
            start = self.quiz.clip_start
        if clip_length is None:
            clip_length = CLIP_LENGTH
        play_clip(self.quiz.path, start, clip_length)

    def on_submit(self):
        results = self.quiz.submit_answer(
            self.show_title_var.get(),
            self.corps_var.get(),
            self.year_var.get(),
            self.placement_var.get(),
        )

        if isinstance(results, str):  # If not all fields filled out
            feedback_text = results
        else:
            # Successful submit
            self.submit_btn.config(state="disabled")

            # Change Icons
            self.title_mark.config(
                image=self.correct_img if results.get("is_title_correct") else self.incorrect_img
            )
            self.corps_mark.config(
                image=self.correct_img if results.get("is_corps_correct") else self.incorrect_img
            )
            self.year_mark.config(
                image=self.correct_img if results.get("is_year_correct") else self.incorrect_img
            )
            self.placement_mark.config(
                image=self.correct_img
                if results.get("is_placement_correct")
                else self.incorrect_img
            )

            feedback_text = (
                "Correct Answer:\n\n"
                f"{self.quiz.current_show.get_corps()} {self.quiz.current_show.get_year()}: "
                f"{self.quiz.current_show.get_title()} "
                f"({self.quiz.current_show.get_placement()})\n\n"
                f"You earned {self.quiz.earned_points}/7 points!"
            )

            if self.quiz.earned_points <= 1:
                fart_path = os.path.join(BASE_DIR, "gui_files", "audio", "fart2.m4a")
                play_clip(fart_path, 0, 1.30)

            self.total_points_label.config(text=f"Total Points: {self.quiz.total_points}")

        self.feedback_label.config(text=feedback_text)

    def on_hint(self):
        self.hint_menu.tk_popup(self.hint_btn.winfo_rootx() + 4, self.hint_btn.winfo_rooty() - 48)
        self.hint_menu.grab_release()

    def extend_clip(self):
        duration = get_duration(self.quiz.path)
        max_length = max(0, duration - self.quiz.clip_start)
        extended_length = min(CLIP_LENGTH * 2, max_length)
        self.start_playback(self.quiz.clip_start, extended_length)

    def different_clip(self):
        self.quiz.clip_start = create_random_clip(self.quiz.path, CLIP_LENGTH)
        self.start_playback(self.quiz.clip_start, CLIP_LENGTH)

    def next_question(self):
        stop_audio()
        if not self.quiz.advance_question():
            self.feedback_label.config(text="Quiz complete!")
            self.submit_btn.config(state="disabled")
            self.play_btn.config(state="disabled")
            self.hint_btn.config(state="disabled")
            self.next_button.config(state="disabled")
            self.total_points_label.config(text=f"Total Points: {self.quiz.total_points}")
            self.on_complete(self.quiz.total_points, self.quiz.num_rounds * 7)
            return #Quiz is finished

        self._reset_answer_inputs()
        self.submit_btn.config(state="normal")
        self.question_label.config(
            text=f"Question {self.quiz.question_index}/{self.quiz.num_rounds}"
        )
        self.feedback_label.config(text="")
        self.total_points_label.config(text=f"Total Points: {self.quiz.total_points}")
