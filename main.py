import random

print("Welcome to the Number Guessing Game")

print("thinking of a number between 1 and 100")

random_number = random.randint(1,100)

#print(random_number)

game_attempts = 0

game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if game_level == "easy":
    game_attempts = 10
    print("You have 10 attempts to guess the number")
elif game_level == "hard":
    print("You have 5 attempts to guess the number")
    game_attempts = 5



while game_attempts > 0:
    user_guess = int(input("Make a guess: "))
        
    if user_guess == random_number:
        print("Your guess is match")
        break
    elif user_guess > random_number:
        game_attempts -= 1
        print("Too High")
    elif user_guess < random_number:
        game_attempts -= 1
        print("Too low")