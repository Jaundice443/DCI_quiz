import tkinter as tk
from tkinter import ttk
from quiz_logic import *
import threading
import audio

quiz = QuizQuestion()

root = tk.Tk()
root.title("Drum Corps Quiz")
root.geometry("900x600")
root.resizable(True, True)
root.configure(bg="#83a5e0")

card = tk.Frame(root, bg="#ffffff", width= 825, height=550)
card.place(relx=0.5, rely=0.5, anchor="center")

title = tk.Label(card, text="DRUM CORPS QUIZ", font=("Comic Sans MS", 30, "bold"), bg="white", fg="#0E151C")
title.pack(pady=20)

header_row = tk.Frame(card, bg="white")
header_row.pack(fill="x", padx=40, pady=(0, 10))
header_row.grid_columnconfigure(0, weight=1)
header_row.grid_columnconfigure(1, weight=0)
header_row.grid_columnconfigure(2, weight=1)

question_label = tk.Label(
    header_row,
    text=f"Question {quiz.question_index}/{quiz.num_rounds}",
    font=("Arial", 12),
    bg="white",
    fg="#0E151C"
)
question_label.grid(row=0, column=1)

total_points_label = tk.Label(
    header_row,
    text=f"Total Points: {quiz.total_points}",
    font=("Arial", 12, "bold"),
    justify="left",
    fg="black",
    bg="white"
)
total_points_label.grid(row=0, column=2, sticky="w", padx=(10, 0))

content_row = tk.Frame(card, bg="white")
content_row.pack(pady=10, fill="x")

#Input side
left_frame = tk.Frame(content_row, bg="white")
left_frame.pack(side="left", padx=(50, 40), anchor="n")

#Results side
right_frame = tk.Frame(content_row, bg="white")
right_frame.pack(side="left", padx=(40, 60), anchor="n")

correct_img = tk.PhotoImage(file=r"C:\Users\Tyler\Projects\DCI_quiz\gui_files\images\correct.png")
incorrect_img = tk.PhotoImage(file=r"C:\Users\Tyler\Projects\DCI_quiz\gui_files\images\incorrect.png")
blank_img = tk.PhotoImage()

feedback_label = tk.Label(
    right_frame,
    text="",
    font=("Arial", 12),
    justify="left",
    wraplength=300,
    fg="black",
    bg="white"
)
feedback_label.pack(anchor="n")


tk.Label(left_frame, text="Enter Show Title:", justify="left", bg="white").grid(row=0, column=0, padx=(20, 5), sticky="w")

show_title_var = tk.StringVar()
title_entry = tk.Entry(
    left_frame,
    textvariable=show_title_var,
    width=43,
    relief="groove",       # style of border: solid, groove, ridge, sunken, raised
    highlightthickness=1, # outline thickness for focus
    highlightbackground="grey", # outline color when not focused
    # highlightcolor="blue" # outline color when focused
)

title_entry.grid(row=1, column=0, padx=(20, 5), pady=(0, 10), sticky="w")

title_mark = tk.Label(left_frame, image=blank_img, bg="white")
title_mark.grid(row=1, column=1, padx=(5, 20), pady=(0, 10))

title_entry.config(fg="black")

corps_var = tk.StringVar()
corps_dropdown = ttk.Combobox(
    left_frame,
    textvariable=corps_var,
    state="readonly",
    width=40
)
corps_dropdown.grid(row=2, column=0, padx=(20, 5), pady=10, sticky="w")

corps_mark = tk.Label(left_frame, image=blank_img, bg="white")
corps_mark.grid(row=2, column=1, padx=(5, 20))

corps_dropdown["values"] = get_corps_options()
corps_dropdown.set("Select Corps")

year_var = tk.StringVar()
year_dropdown = ttk.Combobox(
    left_frame,
    textvariable=year_var,
    state="readonly",
    width=40
)
year_dropdown.grid(row=3, column=0, padx=(20, 5), pady=10, sticky="w")

year_mark = tk.Label(left_frame, image=blank_img, bg="white")
year_mark.grid(row=3, column=1, padx=(5, 20))

year_dropdown.set("Select Year")
year_dropdown["values"] = get_year_options()


placement_var = tk.StringVar()
placement_dropdown = ttk.Combobox(
    left_frame,
    textvariable=placement_var,
    state="readonly",
    width=40
)
placement_dropdown.grid(row=4, column=0, padx=(20, 5), pady=10, sticky="w")

placement_mark = tk.Label(left_frame, image=blank_img, bg="white")
placement_mark.grid(row=4, column=1, padx=(5, 20))

placement_dropdown["values"] = get_placement_options()
placement_dropdown.set("Select Placement")



button_frame = tk.Frame(card, bg="white")
button_frame.pack(pady=20)

play_btn = tk.Button(
    button_frame,
    text="▶ Play Clip",
    font=("Helvetica", 12),
    width=15,
    command= lambda: start_playback()
)
play_btn.grid(row=0, column=0, padx=10)


submit_btn = tk.Button(
    button_frame,
    text="✔ Submit",
    font=("Helvetica", 12),
    width=15,
    command=lambda: on_submit()
)
submit_btn.grid(row=0, column=1, padx=10)

hint_btn = tk.Button(
    button_frame,
    text="💡 Hint",
    font=("Helvetica", 12),
    width=15,
    command=lambda: on_hint()
)
hint_btn.grid(row=0, column=2, padx=10)

hint_menu = tk.Menu(root, tearoff=0)
hint_menu.add_command(label="Extend clip", command=lambda: extend_clip())
hint_menu.add_command(label="Play different clip", command=lambda: different_clip())

next_button = tk.Button(
    button_frame,
    text=">> Next Question",
    font=("Helvetica", 12),
    width=15,
    command= lambda: next_question(quiz)
)
next_button.grid(row=0, column=3, padx=10)

#_____________FUNCTIONS_____________________________

def on_clip_finished():
    play_btn.config(state="normal"),
    hint_btn.config(state="normal")

def check_clip_done():
    print(audio.ffplay_process)
    if audio.ffplay_process is None or audio.ffplay_process.poll() is not None:
        print("Clip finished")
        on_clip_finished()
    else:
        root.after(100, check_clip_done)

def start_playback(start=None, clip_length=None, disable_hint=False):
    # play_btn.config(state="disabled")
    # hint_btn.config(state="disabled")

    if start is None:
        start = quiz.clip_start
    if clip_length is None:
        clip_length = CLIP_LENGTH
    play_clip(quiz.path, start, clip_length)
    # check_clip_done()

def on_submit():
    results = quiz.submit_answer(
        show_title_var.get(),
        corps_var.get(),
        year_var.get(),
        placement_var.get()
    )

    if isinstance(results, str): #If not all fields filled out
        feedback_str = results
    else: 
        #Sucessful submit
        submit_btn.config(state="disabled")

        #Change Icons 
        title_mark.config(image=correct_img if results.get('is_title_correct') else incorrect_img)
        corps_mark.config(image=correct_img if results.get('is_corps_correct') else incorrect_img)
        year_mark.config(image=correct_img if results.get('is_year_correct') else incorrect_img)
        placement_mark.config(image=correct_img if results.get('is_placement_correct') else incorrect_img)

        feedback_str = (
            f"Correct Answer:\n\n"
            f"{quiz.current_show.get_corps()} {quiz.current_show.get_year()}: "
            f"{quiz.current_show.get_title()} "
            f"({quiz.current_show.get_placement()})\n\n"
            f"You earned {quiz.earned_points}/7 points!"
            )
        
        if(quiz.earned_points <= 1):
               fart_path = r"C:\Users\Tyler\Projects\DCI_quiz\gui_files\audio\fart2.m4a"
               play_clip(fart_path, 0, 1.30)
        total_points_label.config(text=f"Total Points: {quiz.total_points}")

    feedback_label.config(text=feedback_str)

def on_hint():
    hint_menu.tk_popup(hint_btn.winfo_rootx() + 4, hint_btn.winfo_rooty() - 48)
    hint_menu.grab_release()

def extend_clip():
    duration = get_duration(quiz.path)
    max_length = max(0, duration - quiz.clip_start)
    extended_length = min(CLIP_LENGTH * 2, max_length)
    start_playback(quiz.clip_start, extended_length, disable_hint=True)

def different_clip():
    quiz.clip_start = create_random_clip(quiz.path, CLIP_LENGTH)
    start_playback(quiz.clip_start, CLIP_LENGTH, disable_hint=True)
    
def next_question(quiz):
    stop_audio()
    if not quiz.advance_question():
        feedback_label.config(text=f"Quiz complete!\nTotal Points: {quiz.total_points}")
        submit_btn.config(state="disabled")
        next_button.config(state="disabled")
        total_points_label.config(text=f"Total Points: {quiz.total_points}")
        return

    show_title_var.set("")
    corps_var.set("Select Corps")
    year_var.set("Select Year")
    placement_var.set("Select Placement")

    submit_btn.config(state="normal")
    question_label.config(text=f"Question {quiz.question_index}/{quiz.num_rounds}")
    feedback_label.config(text="")
    total_points_label.config(text=f"Total Points: {quiz.total_points}")

    #Reset icons
    title_mark.config(image=blank_img)
    corps_mark.config(image=blank_img)
    year_mark.config(image=blank_img)
    placement_mark.config(image=blank_img)


def on_close():
    stop_audio()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
