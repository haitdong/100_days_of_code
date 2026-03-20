from game_data import data
import random

#print out the game logo
from art import logo
from art import vs
print(logo)

#randomly choose the first two keys in the data dictionary print out as option A and B
    #chosen key need to print hints about the key, name, description, country

current_choices = []
random.choices(data, k=2)
current_choices += random.choices(data, k=2)

#player choose which one has more follower_count
    #compare the play choice with the correct choice
        #if player chose right, keep the first chosen answer and generate new B choice, make the other one A
            #if a choice shown twice, always show new choice as A next
def play_game():
    keep_playing = True
    score = 0
    while keep_playing == True:
        print(
            f"Compare A: {current_choices[0]["name"]}, {current_choices[0]["description"]}, {current_choices[0]["country"]}.")
        print(vs)
        print(
            f"Compare B: {current_choices[1]["name"]}, {current_choices[1]["description"]}, {current_choices[1]["country"]}.")
        choice = input("Who has more followers? Type 'A' or 'B'    ")
        if choice == "A" and current_choices[0]["follower_count"] >= current_choices[1]["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            current_choices.pop(0)
            current_choices.append(random.choice(data))
        elif choice == "A" and current_choices[0]["follower_count"] < current_choices[1]["follower_count"]:
            print(f"Sorry, that's wrong. Final score: {score}")
            keep_playing = False
        elif choice == "B" and current_choices[1]["follower_count"] >= current_choices[0]["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            current_choices.pop(0)
            current_choices.append(random.choice(data))
        elif choice == "B" and current_choices[1]["follower_count"] < current_choices[0]["follower_count"]:
            print(f"Sorry, that's wrong. Final score: {score}")
            keep_playing = False

play_game()
#keep count of the score += 1 if player guess right every time
    #if wrong print current score and end the game