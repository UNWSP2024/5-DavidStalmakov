# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------
import random

def math_quiz():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    print(f"What is {num1} + {num2}?")
    answer = int(input("Your answer:"))

    if answer == num1 + num2:
        print("Congratulations that is correct!")
    else:
        print(f"Sorry, that's incorrect. The correct answer is {num1 + num2}.")
math_quiz()

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.