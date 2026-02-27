from audio import *
import random
from show_list import show_list


CLIP_LENGTH = 5
NUM_ROUNDS = 10
total_points = 0

if __name__ == "__main__":
    for i in range(NUM_ROUNDS):
        chosen_show = random.choice(show_list)

        path = chosen_show.get_path()

        input("Continue...")
        print()
        print(f"ROUND {i+1}")
        print()

        clip_start = create_random_clip(path, CLIP_LENGTH)
        play_clip(path, clip_start, CLIP_LENGTH)

        while input("Need help? (y) ") == "y":
            help_asked = input("1. Replay clip \n2. Extend clip \n3. Play different clip\n")
            if help_asked == "1":
                play_clip(path, clip_start, CLIP_LENGTH)
            elif help_asked == "2":
                play_clip(path, clip_start, CLIP_LENGTH * 2)
            else:
                play_random_clip(path, CLIP_LENGTH)
        
        print()
        print("********")
        corps_guess = input("What corps is this? ")

        year_guess = input("What year was this performed? ")

        title_guess = input("What is the title of the show? ")

        placement_guess = input("What place did this show get? ")

        earned_points = 0
        if(corps_guess == chosen_show.get_corps()):
            earned_points += 2
        if(year_guess == chosen_show.get_year()):
            earned_points += 2
        if(title_guess.lower() == chosen_show.get_title().lower()):
            earned_points += 2
        if(placement_guess == chosen_show.get_placement()):
            earned_points += 1

        total_points += earned_points

        print()
        print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
        print(f"You just heard {chosen_show.get_corps()} {chosen_show.get_year()}: {chosen_show.get_title()} ({chosen_show.get_placement()})")
        if earned_points == 7:
            print(f"Perfect! You earned {earned_points} points! (Total: {total_points})")
        else:
            print(f"You earned {earned_points} points! (Total: {total_points})")
        print()
