# Python Quiz Application
# Created by: SANDEEP KUMAR no

def ask_question(question, option1, option2, option3, option4, correct_answer):

    print("\n" + question)

    options = [option1, option2, option3, option4]

    for option in options:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ")

    if answer.upper() == correct_answer:
        print("Correct Answer!")
        return 1
    else:
        print("Wrong Answer!")
        print("Correct answer is:", correct_answer)
        return 0


def start_quiz():

    print("\n================================")
    print("       PYTHON QUIZ APPLICATION")
    print("================================")

    name = input("Enter your name: ")

    print("\nWelcome,", name)
    print("Let's start the quiz!")

    score = 0

    score += ask_question(
        "1. Which language is used for Python programming?",
        "A. Java",
        "B. Python",
        "C. C++",
        "D. HTML",
        "B"
    )

    score += ask_question(
        "2. Which keyword is used to define a function?",
        "A. function",
        "B. fun",
        "C. def",
        "D. define",
        "C"
    )

    score += ask_question(
        "3. Which loop is used to repeat a block of code?",
        "A. for",
        "B. print",
        "C. input",
        "D. return",
        "A"
    )

    score += ask_question(
        "4. Which function is used to display output?",
        "A. input()",
        "B. print()",
        "C. range()",
        "D. type()",
        "B"
    )

    score += ask_question(
        "5. Which statement is used for decision making?",
        "A. if",
        "B. for",
        "C. def",
        "D. return",
        "A"
    )

    print("\n================================")
    print("           QUIZ RESULT")
    print("================================")

    print("Student Name:", name)
    print("Total Questions: 5")
    print("Correct Answers:", score)
    print("Wrong Answers:", 5 - score)

    percentage = (score / 5) * 100

    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Result: Excellent Performance!")

    elif percentage >= 50:
        print("Result: Good Performance!")

    else:
        print("Result: Keep Practicing!")

    print("================================")


while True:

    start_quiz()

    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("\nThank you for playing!")
        print("Have a nice day!")
        break