# Number Guessing Game
import random

print('Let\'s play a game!')
print('I\'m going to pick a number between 1 and 100')
print('Your job is to guess the number! You get 10 guesses!')
print('Ready? Guess the number!')

my_number = random.randint(1, 100)
guess_count = 0
answer = 'Y'

while answer == 'Y':
    while guess_count != 10:
        user_guess = int(input())
        if user_guess > my_number:
            print("Too high! Try again!")
            guess_count += 1
        elif user_guess < my_number:
            print("Too low! Try again!")
            guess_count += 1
        elif user_guess == my_number:
            print(f"You got it! My number was {my_number}!")
        elif guess_count == 10:
            print("You've run out of guesses and you didn't guess my number! Try again?!")
            print("Please enter Y or N!")
            answer = input().upper()

