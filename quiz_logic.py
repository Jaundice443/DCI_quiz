from drumcorpsquiz import show_list
from audio import *
from DCIshow import DCIshow
import threading

CLIP_LENGTH = 5
NUM_ROUNDS = 5

def get_corps_options():
    return sorted(set(show.corps for show in show_list))

def get_year_options():
    return list(range(2025, 2009, -1))

def get_placement_options():
    return ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]


class QuizQuestion:
    def __init__(self):
        self.num_rounds = NUM_ROUNDS
        self.question_index = 1
        self.total_points = 0
        self._load_new_question()

    def _load_new_question(self):
        self.current_show = random.choice(show_list) #Picks random show
        self.path = self.current_show.get_path()
        self.clip_start = create_random_clip(self.path, CLIP_LENGTH)
        self.earned_points = 0

    def gui_play_clip(self, on_finished):

        play_clip(self.path, self.clip_start, CLIP_LENGTH)

        on_finished()

    def advance_question(self):
        if not self.question_index < self.num_rounds:
            return False
        self._load_new_question()
        self.question_index += 1
        return True
    
    def submit_answer(self, title_guess, corps_guess, year_guess, placement_guess):
        correct_title = self.current_show.get_title()
        correct_corps = self.current_show.get_corps()
        correct_year = self.current_show.get_year()
        correct_placement = self.current_show.get_placement()

        results_dict = {}

        if(corps_guess == "Select Corps" or year_guess == "Select Year" or placement_guess == "Select Placement"):
            return "Please fill out all fields"
        else:
            if(title_guess.lower().strip() == correct_title.lower().strip()):
                self.earned_points += 2
                results_dict["is_title_correct"] = True
            else:
                results_dict["is_title_correct"] = False
            
            if(corps_guess == correct_corps):
                self.earned_points += 2
                results_dict["is_corps_correct"] = True
            else:
                results_dict["is_corps_correct"] = False

            if(year_guess == correct_year):
                self.earned_points += 2
                results_dict["is_year_correct"] = True
            else:
                results_dict["is_year_correct"] = False

            if(placement_guess == correct_placement):
                self.earned_points += 1
                results_dict["is_placement_correct"] = True
            else:
                results_dict["is_placement_correct"] = False

            self.total_points += self.earned_points
            return results_dict
            

    
