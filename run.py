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
    guesses = []
    correct_guesses = 0
    question_num = 0
    for question_num in range(len(questions_one)):
        print("----")
        print(questions_one[question_num]("text"))
        for i in options[question_num]:
            print(i)
    guess = input("Enter your answer(a,b,c,d): ").lower()
    is_correct = check_answer(guess,questions_one[question_num]["answer"])
    question_num += 1

def quiz_game_two():
    """
    Input of the quiz game two
    """
    guesses = []
    correct_guesses = 0
    question_num = 0
    for question_num in range(len(questions_one)):
        print("----")
        print(questions_two[question_num]("text"))
        for i in options[question_num]:
            print(i)

    guess = input("Enter your answer(a,b,c,d): ").lower()
    is_correct = check_answer(guess,questions_two[question_num]["answer"])
    question_num += 1
    

def check_answer(user_guess,correct_answer):
    """
    Check the answer for being correct
    """
    score = 0
    if user_guess == correct_answer:
        return True
    else:
        return False

def display_score(is_correct):
    """
    Display user score overall
    """
    print("-----")
    print("Result: ")
    print("-----")

    if is_correct:
        print("Correct")
        score += 1
    else:
        print("Incorecct")
        print(f"The correct answer is {quiz_game_one,quiz_game_two[guestion_num]['answer"']}")
        print(f"Your current score is {score}/{question_num+1}")
    print(f"Your have given {score} correct answers")
    print("Your score is {(score/len(question_one,question_two))*100}%")

def play_again():
    response = input("Do you want to play again(yes or no): ")
    if response == "yes":
        return True
    else:
        return False

print_menu()
quiz_game_one()
quiz_game_two()
display_score()
play_again()