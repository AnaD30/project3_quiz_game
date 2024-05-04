# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import os

def print_menu():

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
        try:
            choice = int(input("Please enter a choice (1-4): "))
            if choice == 1 or 2 or 3:
                break
            elif choice == 4:
                print("Exiting")
                exit()
            else:
                print("Invalid choice. Enter 1-4")
        except ValueError:
          print("It has to be number")

    if choice == 1:
        clear_terminal()
        quiz_game_one()
    elif choice == 2:
        clear_terminal()
        quiz_game_two()
    elif choice == 3:
        clear_terminal()
        play_again() 

def clear_terminal():
    """
    Wipes the terminal clean
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def quiz_game_one():
    """
    Input of the quiz game one
    """
    correct_guesses = 0
    question_num = 1
    sample_size = min(len(questions_one), 5)
    question_keys = random.sample(list(questions_one), sample_size)
    for key in question_keys:
        if question_num > 0:
            print("----")
            print(key)
        for i in options_quiz_one[list(questions_one.keys()).index(key)]:
            print(i)

        guesses = []
        guess = input("Enter(a,b,c,d): \n")
        guess = guess.lower()
        guesses.append(guess)
        
    correct_guesses += check_answer(questions_one.get(key), guess)
    question_num += 1

    questions_list = [questions_one, questions_two]
    correct_guesses_one =["c", "d", "b", "d"]
    correct_guesses = {questions_one: correct_guesses_one, questions_two: correct_guesses_two}
    display_score(correct_guesses, guesses, questions_list)

questions_one = {
        "The capital city of Croatia?":"c",
        "The capital city of Slovenia?":"d",
        "The capital city of China?":"b",
        "The capital city of Ukraine?":"d"
}

options_quiz_one = [
    ["a.Sarajevo","b.Beograd","c.Zagreb","d.Riga"],
    ["a.Tallin","b.Warsaw","c.Oslo","d.Ljubljana"],
    ["a.Shanghai","b.Beijing","c.Singapur","d.Hong Kong"],
    ["a.Prague","b.Dortmund","c.Brussels","d.Kiev"]
]

def quiz_game_two():

    """
    Input of the quiz game two
    """
    correct_guesses = 0
    question_num = 1
    sample_size = min(len(questions_one), 5)
    question_keys = random.sample(list(questions_one), sample_size)
    for key in question_keys:
        if question_num > 0:
            print("----")
            print(key)
        for i in options_quiz_two[list(questions_two.keys()).index(key)]:
            print(i)
        guesses = []
        guess = input("Enter(a,b,c,d): \n")
        guess = guess.lower()
        guesses.append(guess)
        correct_guesses_two = ["c", "a", "a", "d" ]
        if key in questions_two:
            correct_guesses_two += check_answer(questions_two.get(key), guess)
        else:
            correct_guesses_one += check_answer(questions_one.get(key), guess)
        question_num += 1
    questions_list = [questions_one, questions_two]
    correct_guesses = {questions_one: correct_guesses_one, questions_two: correct_guesses_two}
    display_score(correct_guesses, guesses, questions_list)

questions_two = {
     "The capital city of USA?":"c",
        "The capital city of Great Britain?":"a",
        "The capital city of Japan?":"a",
        "The capital city of France?":"d"
}

options_quiz_two = [
        ["a.Houston","b.Miami","c.Washington D.C","d.Texas"],
        ["a.London","b.Birninham","c.Sydney","d.Wales"],
        ["a.Tokyo","b.Osaka","c.Kyoto","d.Okinawa"],
        ["a.Nice","b.Köln","c.Brussels","d.Paris"]
]
def check_answer(answer,guess):
    """
    Check the answer for being correct
    """
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

def display_score(correct_guesses, guesses, questions_list):

    """
    Display user score overall
    """
    print("-----")
    print("Results: ")
    print("-----")
  
    print("Correct guesses:", correct_guesses)
    print("Guesses:", guesses)
    score = int(correct_guesses/len(questions_list)*100)
    print("You're score is:", score, "%")

def play_again():
    response = input("Do you want to play again?(yes or no): \n")
    if response == "yes":
        return True
    else:
        return False

print_menu()
quiz_game_one()
quiz_game_two()
while play_again():
    clear_terminal()
    quiz_game_one()
    quiz_game_two()