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
})
#from ._palettes import  STANDARD_PALETTE



def print_menu(options_quiz_one):
    """
    Create a menu
    """
print("-------")
print("Select an choice:")
print("1.Quiz One")
print("2.Quiz Two")
print("3.Play Again")
print("4.Exit the Quiz")
print("-------")


while True:
    print_menu()   
    choice = input("Please enter a choice:")
if choice == 1:
    print("quiz_game_one")
elif choice == 2:
    print("quiz_game_two")
elif choice == 3:
    print("Display_score")
else:
    input("Do you want to quit(yes or no)? ")


def clear_terminal(print_menu,quiz_game_one,options_quiz_two):
    """
    Wipes the terminal clean
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def quiz_game_one():
    """
    Input of the quiz game one
    """
    
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print(key)
        for i in options_quiz_one[question_num -1]:
            print(i)

    guesses = input("Enter answer: ")
    guesses = guesses.lower()
    guesses.append(guesses)
    check_answer(question.get(key))
    question_num += 1

questions_one = {
    "What is the capital city of Croatia?"
    "What is the capital city of Poland?"
    "What is the capital city of China?"
    "What is the capital city of Slovakia?"
    "What is the capital city of Slovenia?"
}

options_quiz_one = [["a.Sarajevo","b.Tallin","c.Zagreb","d.Riga"],
                    ["a.Warsaw","b.Berlin","c.Köln","d.Wien"],
                    ["a.Singapor","b.Hong Kong","c.Shanghai","d.Beijing"],
                    ["a.Tokyo","b.Bratislava","c.Valetta","d.Dortmund"],
                    ["a.Ljubljana","b.Rome","c.Zagreb","d.Beograd"]]

def quiz_game_two():
    """
    Input of the quiz game two
    """
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print(key)
        for i in options_quiz_one[question_num -1]:
            print(i)

    guesses = input("Enter answer: ")
    guesses = guesses.lower()
    guesses.append(guesses)
    correct_guesses += check_answer(question.get(key))
    question_num += 1     

questions_two = {
    "What is the capital city of USA?"
    "What is the capital city of Great Britain?"
    "What is the capital city of Norway?"
    "What is the capital city of Ukraine?"
    "What is the capital city of Germany?"
}

options_quiz_two = [["a.WashingtWashington D.C.","b.Houston","c.Texas","d.Miami"],
                    ["a.Walles","b.Birmingham","c.London","d.Kiew"],
                    ["a.Oslo","b.Seoul","c.Prague","d.Brussels"],
                    ["a.Kiew","b.Lisbon","c.Trieste","d.Milan"],
                    ["a.Bremen","b.Stuttgart","c.Berlin","d.Ankarra"]]


def check_answer(answer):
    if answer == guess:
        print("Correct!")
    else:
        print("Wrong")
        return 0

def display_score(correct_guesses):
    print("-----")
    print("Result: ")
    print("-----")

    print("Answers,end=")
    for i in questions_two:
        print(question.get(i),end=" ")
    print()

    print("Answers,end=")
    for i in questions_one:
        print(question.get(i),end=" ")
    print()

    score = int((correct_guesses/len(questions_one,questions_two))*100)
    print("Your score is:"+str(score)+"%")
def play_again():
    response = input("Do you want to play again(yes or no): ")
    if response == "yes":
        return True
    else:
        return False


def main():
    """
    Runs main function
    """
    while play_again():
        quiz_game_one()
        quiz_game_two()
print("Thank you for playing!")