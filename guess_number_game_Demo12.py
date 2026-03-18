import random

#choosing difficult levels
def difficult_level():
    level = 0
    if difficulty == "easy":
        level += 10
    if difficulty == "hard":
        level += 5
    return level

#guessing game
def play_guess():
    attempt = int(difficult_level())

    print(f"You have {difficult_level()} attempts remaining to guess the number")
    for a in range(difficult_level()):
        myguess = int(input("make a guess: "))
        if myguess == FINAL_CHOSEN:
            print(f"You won! The number is {FINAL_CHOSEN}")
            break
        elif myguess < FINAL_CHOSEN:
            attempt -= 1
            print(f"Too low.\nGuess again.\nYou have {attempt} attempts remaining to guess the number.")
        elif myguess > FINAL_CHOSEN:
            attempt -= 1
            print(f"Too high.\nGuess again.\nYou have {attempt} attempts remaining to guess the number.")

#combine code blocks into a game:
def play_game():
    difficult_level()
    print(FINAL_CHOSEN)
    play_guess()

is_game_over = False
while not is_game_over:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    #generate a random number
    FINAL_CHOSEN = random.randrange(1, 100)
    play_game()
    keep_playing = input("Do you want to continue playing? Type 'y' to continue, 'n' to stop. ")
    if keep_playing == "n":
        is_game_over = True
        print("Thanks for playing!")
    else:
        print("\n" * 20)

