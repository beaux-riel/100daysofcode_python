# Day 17 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - The Quiz Project and the Benefits of OOP - Main 

# Import ya' business
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Creat empty question_bank to populate.
question_bank = []

# Goes through data(.py), formats them for the empty question_bank above, and then appends them to that list.
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initializing our quiz
quiz = QuizBrain(question_bank)

# While loop to keep our game going
while quiz.still_has_questions():
    quiz.next_question()

# Final hooray!
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")