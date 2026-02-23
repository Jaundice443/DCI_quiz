import tkinter as tk

from audio import stop_audio
from screens.menu_screen import MenuScreen
from screens.quiz_screen import QuizScreen
from screens.results_screen import ResultsScreen
from screens.tutorial_screen import TutorialScreen


root = tk.Tk()
root.title("Drum Corps Quiz")
root.geometry("900x600")
root.resizable(True, True)
root.configure(bg="#83a5e0")


def on_close():
    stop_audio()
    root.destroy()


def show_menu():
    stop_audio()
    menu_screen.tkraise()


def show_quiz():
    quiz_screen.start_new_quiz()
    quiz_screen.tkraise()

def show_results(total_points, max_points):
    results_screen.update_results(total_points, max_points)
    results_screen.tkraise()
    
def show_tutorial():
    tutorial_screen.tkraise()

menu_screen = MenuScreen(root, on_play=show_quiz, on_tutorial=show_tutorial, on_quit=on_close)
tutorial_screen = TutorialScreen(root, on_main_menu=show_menu)
quiz_screen = QuizScreen(root, on_main_menu=show_menu, on_complete=show_results)
results_screen = ResultsScreen(root, on_main_menu=show_menu, on_quiz_start=show_quiz)

show_menu()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
