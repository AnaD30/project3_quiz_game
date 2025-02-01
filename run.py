# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


def check_answer(correct_answer, guess):

    """Check if the guess is correct."""

    return 1 if correct_answer == guess else 0


def display_score(correct_guesses, total_questions):

    """Display the score of the quiz."""

    score = sum(correct_guesses)

    print(f"\nYour score is: {score}/{total_questions}")


def quiz_game(questions, options):

    """

    Input of the quiz game

    """

    correct_guesses = []

    question_num = 1

    sample_size = min(len(questions), 5)

    question_keys = random.sample(list(questions), sample_size)


    for key in question_keys:

        print("----")

        print(key)

        for option in options[list(questions.keys()).index(key)]:

            print(option)


        guess = input("Enter (a, b, c, d): \n").lower()

        correct_guesses.append(check_answer(questions[key], guess))

        question_num += 1


    return correct_guesses


def main():

    questions_one = {

        "The capital city of Croatia?": "c",

        "The capital city of Slovenia?": "d",

        "The capital city of China?": "b",

        "The capital city of Ukraine?": "d"

    }


    options_quiz_one = [

        ["a. Sarajevo", "b. Beograd", "c. Zagreb", "d. Riga"],

        ["a. Tallin", "b. Warsaw", "c. Oslo", "d. Ljubljana"],

        ["a. Shanghai", "b. Beijing", "c. Singapur", "d. Hong Kong"],

        ["a. Prague", "b. Dortmund", "c. Brussels", "d. Kiev"]

    ]


    questions_two = {

        "What is the capital city Japan ?": "b",

        "What is the capital city USA ?": "a",

        "What is the capital city India?": "c",

        "What is the capital city of Peru?": "c",

        "What the capital city Austria ": "a"

    }


    options_quiz_two = [

        ["a. Osaka", "b. Tokyo", "c. Kyoto", "d. Nara", "e. Sapporo"],

        ["a. Washington D.C.", "b. Texsas", "c. Florida", "d.New York", "e. Houston"],

        ["a.Kalkuta", "b. Mumbay", "c. New Delhi", "d.Banglalore", "e.Pune"],

        ["a.Cusco", "b. Huaraz", "c. Lima", "d. Cajamarca", "e. Ayacucho"],

        ["a. Vienna", "b. Graz", "c. Linz", "d.Salzburg", "e. Klagenfurt"]

    ]


    while True:

        print("\n--- Quiz Game Menu ---")

        print("1. Start Quiz 1")

        print("2. Start Quiz 2")

        print("3. Exit")

        choice = input("Enter your choice: ")


        if choice == '1':

            print("\n--- Starting Quiz 1 ---")

            correct_guesses = quiz_game(questions_one, options_quiz_one)

            display_score(correct_guesses, len(questions_one))

        elif choice == '2':

            print("\n--- Starting Quiz 2 ---")

            correct_guesses = quiz_game(questions_two, options_quiz_two)

            display_score(correct_guesses, len(questions_two))

        elif choice == '3':

            print("Thank you for playing! Goodbye!")

            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":

    main()