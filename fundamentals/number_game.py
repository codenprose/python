import random

# define game method
def game():
    # generate a random # between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        # get a number from the user
        try:
            guess = int(input("Guess and number between 1 and 10: "))
        except ValueError:
            print("{} That isn't a number".format(guess))
        else:
            # compare guess to secret number
            if guess == secret_num:
                print("Nice! You picked the correct number! %s" % secret_num)
                break
            elif guess < secret_num:
                print("Too low, guess higher than %s." % guess)
            elif guess > secret_num:
                print("Too high, guess lower than %s" % guess)
            else:
                print('Wrong Number')
            guesses.append(guess)
    else:
        print("You didn't get it, the number was %s" % secret_num)
    # ask user if they want to play again
    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != "n":
        game()
    else:
        print("Bye!")
# run the game
game()
