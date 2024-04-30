# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import os
#from rich.console import Console
from rich.theme import Theme
custom_theme = Theme({
    "Correct":"bright_green"  ,
    "Wrong": "bright_red",
    "No, luck this time!": "bright_yellow"
})
#from ._palettes import  STANDARD_PALETTE

def menu():
    print("[1]quiz_options")
    print("[2]quiz_options")
    print("[3]play_again")
    print("[0]exit_the_quiz")

menu()
quiz_options = int(input("Enter your choice:"))

while quiz_options != 0:
    if option == 1:
        #start the quiz game one
        print("quiz_options one has been called.")
    elif game_options == 2:
        #start the quiz two
        print("quiz_options two has been called.")
    elif game_options == 3:
        print("Do you want to try again")
    else:
        print("Try again,something was wrong.")
    print()
    menu()
    quiz_options = int(input("Enter your choice:"))
print("Thanks for playing this quiz")

def clear_terminal():
    """
    Wipes the terminal clean
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def quiz_one(option[1]):
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in qustions :
        print("")
        print(key)

def quiz_two(option[2]):
    print("")

def play_again(option[3]):
#play again option

def check_answers():
    """
    Checks for the score of the player
    """
def display_score():
    #display

questions_one = {
    "What is the capital city of Croatia?"
    "What is the capital city of Poland?"
    "What is the capital city of China?"
    "What is the capital city of Slovakia?"
    "What is the capital city of Slovenia?"
}

questions_two = {
    "What is the capital city of USA?"
    "What is the capital city of Great Britain?"
    "What is the capital city of Norway?"
    "What is the capital city of Ukraine?"
    "What is the capital city of Germany?"
}

options_quiz_one = [["a.Sarajevo","b.Tallin","c.Zagreb","d.Riga"],
["a.Warsaw","b.Berlin","c.Köln","d.Wien"],
["a.Singapor","b.Hong Kong","c.","d.Beijing"],
["a.Sarajevo","b.Tallin","c.Zagreb","d.Riga"]]