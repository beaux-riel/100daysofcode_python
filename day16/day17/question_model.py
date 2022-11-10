# Day 17 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - The Quiz Project and the Benefits of OOP - Question Model Class 

# Question model - We need a question and a Boolean answer
class Question:
    def __init__(self, q_text,q_answer,):
        self.text = q_text
        self.answer = q_answer