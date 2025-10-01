import random
import sys

print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n""")

secret_num = random.randint(1, 99)
count = 0
while True:
    guess = input("What's your guess between 1 and 99?\n>> ")
    if (guess == "exit"):
        print("Goodbye!")
        sys.exit()
    count += 1
    try:
        guess = int(guess)
    except ValueError:
        print("That's not a number.")
        continue
    if guess < secret_num:
        print("Too low!")
    elif guess > secret_num:
        print("Too high!")
    else:
        break
if (secret_num == 42):
    print("The answer to the ultimate question of life, the universe and everything is 42.")
else:
    print("Congratulations, you've got it!")
if (count == 1):
    print("Congratulations! You got it on your first try!")
else:
    print(f"You won in {count} attempts!")
    
