# Number Guessing Game
import random

print('Let\'s play a game!')
print('I\'m going to pick a number between 1 and 100')
print('Your job is to guess the number! You get 10 guesses!')
print('Ready? Guess the number!')

my_number = random.randint(1, 100)
guess_count = 0
user_guess = int(input())
# answer = input()

# while answer != 'N':
while 0 <= guess_count <= 10:
    if guess_count == 10:
        print("You've run out of guesses and you didn't guess my number! Try again?!")
        print("Please enter Y or N!")
        answer = input().upper()
        if answer == 'Y':
            guess_count = 0
        else:
            print("Goodbye!")
    elif user_guess > my_number:
        print("Too high! Try again!")
        guess_count += 1
        print("You have ", 10 - guess_count, " guesses remaining!")
        user_guess = int(input())
    elif user_guess < my_number:
        print("Too low! Try again!")
        guess_count += 1
        print("You have ", 10 - guess_count, " guesses remaining!")
        user_guess = int(input())
    elif user_guess == my_number:
        print(f"You got it in {guess_count} guesses! My number was {my_number}!")
        print("Would you like to play again? Please enter Y or N!")
        answer = input().upper()
        if answer == 'Y':
            guess_count = 0

        else:
            print("Goodbye!")


