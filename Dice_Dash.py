#Dice Dash

import random

def roll():
    min = 1
    max = 6
    roll = random.randint(min, max)
    return roll

while True:
    players = (input("Enter the number of players (2-4): "))
    if players.isdigit():
        players = int(players)
        if(2 <= players <= 4):
            break
        else:
            print("Invalid...Enter a value between 2 and 4")
    else:
        print("Invalid")

max_score = 50
player_scores = [0 for _ in range(players)]

while(max(player_scores) < max_score):
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        curr_score = 0

        while True:
            should_roll = input("Would you like to roll (y):" )
            if(should_roll.lower() != "y"):
                break
            else:
                value = roll()
            if (value == 1):
                print("You rolled a 1...Turn finished !")
                curr_score = 0
                break
            else:
                curr_score += value
                print("You rolled a:", value)

            print("Your score is:", curr_score)

            player_scores[player_idx] += curr_score
            print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,"is the winner with a score of:", max_score)
