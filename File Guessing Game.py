import random

print("Logan's Number Guessing Game\n"
      "If you guess the correct number between 1 and 100, you win!\n"
      "You have 10 attempts to guess the number.\n"
      "Let's get started!")

random_number = random.randint(1, 100)
Attempts = 10
last_Guess = None
Attempts_left = Attempts
Past_Guesses = []

while Attempts > 0:
    Guess = input ("Enter your guess (1-100): ")
    try: 
        Guess = int(Guess)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    if Guess < 1 or Guess > 100:
        print("Your guess is out of bounds. Please choose a number between 1 and 100.")
        continue
    if Guess == random_number:
        print("You won Logan's Guessing Game!")
        break
    elif Guess in Past_Guesses:
        print("You've already guessed that number. Try a different one.")
        continue
    elif Guess < random_number:
        last_Guess = Guess
        Attempts_left -= 1
        print(f"You have {Attempts_left} attempts left.")
        print(f"Last guess was: {last_Guess}")
        print("Too low! Try again.")
        Past_Guesses.append(Guess)
    else:
        last_Guess = Guess
        Attempts_left -= 1
        print(f"You have {Attempts_left} attempts left.")
        print(f"Last guess was: {last_Guess}")
        print("Too high! Try again.")
        Past_Guesses.append(Guess)
    Attempts -= 1

if Attempts == 0:
    print(f"Sorry, you've run out of attempts. The number was {random_number}.")
    print("Game Over!")