# Rock Paper Scissors

import random
options = ["r", "p", "s"]
player_wins = 0
comp_wins = 0
no_of_games = 5
rounds_left = 5
print(f'Rounds left = {rounds_left}')


while no_of_games > 0:
    comp = random.choice(options)
    player = input("enter your choice: r for rock,p for paper and s for scissors: ").lower()

    if player == "r" and comp == "s" or player == "s" and comp == "p" or player == "p" and comp == "s":
        print("You win this round.")
        player_wins = player_wins +1
        no_of_games = no_of_games - 1
        rounds_left = rounds_left - 1

    else:
        print("Computer wins this round.")
        comp_wins = comp_wins +1
        no_of_games = no_of_games - 1
        rounds_left = rounds_left - 1

    print(f"Rounds left = {rounds_left}")

if player_wins == comp_wins:
    print("Its a draw.")
elif player_wins < comp_wins:
    print("Computer is the winner.")
else:
    print("You win !!!")

print(f"Computer won {comp_wins} times.")
print(f"And, You won {player_wins} times.")