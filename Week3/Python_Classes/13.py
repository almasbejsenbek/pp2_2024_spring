import random
def Numbers():
    secret_number = random.randint(1, 20)
    attempts = 0

    print("Hello! What is your name?")
    Name = input()

    print(f"Well, {Name}, I am thinking of a number between 1 and 20.")
    print("Take a guess.")

    while True:
        guess = int(input())
        attempts += 1

        if guess == secret_number:
            print(f"Good job, {Name}! You guessed my number in {attempts} guesses!")
            break
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

Numbers()