from game_data import data
import random

#print out the game logo
from art import logo
from art import vs
print(logo)

#randomly choose the first two keys in the data dictionary print out as option A and B
    #chosen key need to print hints about the key, name, description, country

current = []
random.choices(data, k=2)
current += random.choices(data, k=2)

#player choose which one has more follower_count
    #compare the play choice with the correct choice
        #if player chose right, keep the first chosen answer and generate new B choice, make the other one A
            #if a choice shown twice, always show new choice as A next

#Using a new compare method, where the follower count is compared by math.
def play_game():
    keep_playing = True
    score = 0
    while keep_playing == True:
        print(f"Compare A: {current[0]["name"]}, {current[0]["description"]}, {current[0]["country"]}.")
        print(vs)
        print(f"Compare B: {current[1]["name"]}, {current[1]["description"]}, {current[1]["country"]}.")
        choice = input("Who has more followers? Type 'A' or 'B'    ")
        if current[0]["follower_count"] - current[1]["follower_count"] > 0:
            if choice == "A":
                score += 1
                print(f"You're right! Current score: {score}")
                print("\n" * 20)
                current.pop(0)
                current.append(random.choice(data))
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                keep_playing = False
        if current[0]["follower_count"] - current[1]["follower_count"] < 0:
            if choice == "B":
                score += 1
                print(f"You're right! Current score: {score}")
                print("\n" * 20)
                current.pop(0)
                current.append(random.choice(data))
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                keep_playing = False
        if current[0]["follower_count"] == current[1]["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}" + "\n")
            print("\n"*20)
            current.pop(0)
            current.append(random.choice(data))

play_game()
#keep count of the score += 1 if player guess right every time
    #if wrong print current score and end the game