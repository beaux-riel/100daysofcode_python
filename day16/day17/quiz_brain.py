# Day 17 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - The Quiz Project and the Benefits of OOP - Quiz Brain

# This module contains the app logic
class QuizBrain:

    # Init + 1 input (question list)
    def __init__(self, q_list):
        # Question number and score both start at 0
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        
    # Kill switch
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

        # Below code was original solution to the problem.
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    # Next question logic
    def next_question(self):
        # Identify which question we're currently answering and...
        current_question = self.question_list[self.question_number]
        # Increment it.
        self.question_number += 1
        # Asks user a question and waits for a Boolean input
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # Compares answers
        self.check_answer(user_answer, current_question.answer)

    # Logic for checking answer
    def check_answer(self, user_answer, correct_answer):
        # If answers are equivalent
        if user_answer.lower() == correct_answer.lower():
            # Add 1 to score
            self.score += 1
            # Pat on the back
            print("You got it right!")
        else:
            # SLAP!
            print("That's wrong.")
        # Correct answer and current score provided.
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
