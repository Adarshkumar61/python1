#guessing game
import random
def guess():
    no_guess = random.randint(1, 100)
    guess = None
    while guess != no_guess:
        guess = int(input("Enter a no bw 1 and 100: "))
        if guess < no_guess:
            print("Too low...")
        elif guess > no_guess:
            print("too high....")
        else:
            print("Congratulation you guessed the number", no_guess)
guess()
