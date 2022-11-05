from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print("You got it! The answer was {answer}.")

# Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

#Choose a random number between 1 ands 100
print("Welcome to Beaux's Kick Ass Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)
print(f"Psst. The correct answer is: {answer}")

turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number.")

#Let the user guess a number
guess = int(input("Make a guess: "))


#Track the number of turns and reduce by 1 if they get it wrong



# Repeat the guessing functionality if they get it wrong




# game_in_progress = True
# target = (random.choice(range(100)))


# print("I'm thinking of a number between 1 and 100.")
# print(f"That number is: {target}")

# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# if difficulty == "hard":
#     guesses_remaining = 5
#     print(f"You have {guesses_remaining} guesses")
# else:
#     guesses_remaining = 10
#     print(f"You have {guesses_remaining} guesses")

# def guess():
#     global game_in_progress


    

# while game_in_progress:
#     guess()
#     guesses_remaining -= 1
    
#     if guesses_remaining == 0:
#         game_in_progress = False
#     else:
#         print(f"You have {guesses_remaining} guesses left.")

