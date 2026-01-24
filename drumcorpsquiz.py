from audio import *
from DCIshow import DCIshow
import random

show_list = [
    DCIshow("Bluecoats", "2014", "TILT", "2nd", "bluecoats_2014.mp3"),
    DCIshow("Bluecoats", "2015", "Kinetic Noise", "3rd", "bluecoats_2015.mp3"),
    DCIshow("Bluecoats", "2016", "Downside Up", "1st", "bluecoats_2016.mp3"),
    DCIshow("Bluecoats", "2017", "Jagged Line", "5th", "bluecoats_2017.mp3"),
    DCIshow("Bluecoats", "2018", "Session 44", "3rd", "bluecoats_2018.mp3"),
    DCIshow("Bluecoats", "2019", "The Bluecoats", "2nd", "bluecoats_2019.mp3"),
    DCIshow("Bluecoats", "2022", "Riffs and Revelations", "2nd", "bluecoats_2022.mp3"),
    DCIshow("Bluecoats", "2023", "Garden of Love", "2nd", "bluecoats_2023.mp3"),
    DCIshow("Bluecoats", "2024", "Change is Everything", "1st", "bluecoats_2024.mp3"),
    DCIshow("Bluecoats", "2025", "The Observer Effect", "2nd", "bluecoats_2025.mp3"),

    DCIshow("Santa Clara Vanguard", "2017", "Ouroboros", "2nd", "scv_2017.mp3"),
    DCIshow("Santa Clara Vanguard", "2018", "Babylon", "1st", "scv_2018.mp3"),
    DCIshow("Santa Clara Vanguard", "2019", "Vox Eversio", "3rd", "scv_2019.mp3"),
    DCIshow("Santa Clara Vanguard", "2024", "Vagabond", "6th", "scv_2024.mp3"),
    DCIshow("Santa Clara Vanguard", "2025", "aVANt GUARD", "3rd", "scv_2025.mp3"),

    DCIshow("Blue Devils", "2014", "Felliniesque", "1st", "bluedevils_2014.mp3"),
    DCIshow("Blue Devils", "2017", "Metamorph", "1st", "bluedevils_2017.mp3"),
    DCIshow("Blue Devils", "2022", "Tempus Blue", "1st", "bluedevils_2022.mp3"),
    DCIshow("Blue Devils", "2023", "The Cutouts", "1st", "bluedevils_2023.mp3"),
    DCIshow("Blue Devils", "2024", "The Romantics", "3rd", "bluedevils_2024.mp3"),
    DCIshow("Blue Devils", "2025", "Variations on a Gathering", "4th", "bluedevils_2025.mp3"),

    DCIshow("Boston Crusaders", "2022", "Paradise Lost", "2nd", "bostoncrusaders_2022.mp3"),
    DCIshow("Boston Crusaders", "2024", "Glitch", "2nd", "bostoncrusaders_2024.mp3"),
    DCIshow("Boston Crusaders", "2025", "BOOM", "1st", "bostoncrusaders_2025.mp3"),

    DCIshow("Carolina Crown", "2013", "E = mc^2", "1st", "carolinacrown_2013.mp3"),
    DCIshow("Carolina Crown", "2014", "Out of this world", "5th", "carolinacrown_2014.mp3"),
    DCIshow("Carolina Crown", "2015", "Inferno", "2nd", "carolinacrown_2015.mp3"),
    DCIshow("Carolina Crown", "2016", "Relentless", "3rd", "carolinacrown_2016.mp3"),
    DCIshow("Carolina Crown", "2017", "It is", "3rd", "carolinacrown_2017.mp3"),
    DCIshow("Carolina Crown", "2023", "The Round Table: Echoes of Camelot", "3rd", "carolinacrown_2023.mp3"),
    DCIshow("Carolina Crown", "2024", "Promethean", "4th", "carolinacrown_2024.mp3"),
    DCIshow("Carolina Crown", "2025", "The Point of No Return", "5th", "carolinacrown_2025.mp3"),

    DCIshow("Phantom Regiment", "2024", "Mynd", "4th", "phantomregiment_2024.mp3"),
    DCIshow("Phantom Regiment", "2025", "", "6th", "phantomregiment_2025.mp3"),

    DCIshow("Cadets", "2011", "Between Angels and Demons", "1st", "cadets_2011.mp3"),
    DCIshow("Cadets", "2015", "The Power of 10", "4th", "cadets_2015.mp3"),
]

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
