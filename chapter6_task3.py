import random

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def main():
    the_number = random.randint(1, 100)
    guess = ask_number("Take a guess: ", 0, 101)
    tries = 1

    while guess != the_number:
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")
                
        guess = ask_number("Take a guess: ", 0, 101)
        tries += 1

    print("You guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")

main()
input("\n\nPress the enter key to exit.")
