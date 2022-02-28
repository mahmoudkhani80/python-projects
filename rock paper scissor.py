player_1 = input("choose an action p1 :")
print(player_1)
player_2 = input("choose an action p2 :")
print(player_2)

if player_1 == "rock" and player_2 == "paper":
    print("player 2 wins")
elif player_1 == "rock" and player_2 == "scissors":
    print("player 1 wins")
elif player_1 == "rock" and player_2 == "rock":
    print("tie")
elif player_1 == "paper" and player_2 == "rock":
    print("player 1 wins")
elif player_1 == "paper" and player_2 == "paper":
    print("tie")
elif player_1 == "paper" and player_2 == "scissors":
    print("player 2 wins")
elif player_1 == "scissors" and player_2 == "rock":
    print("player 2 wins")
elif player_1 == "scissors" and player_2 == "paper":
    print("player 1 wins")
elif player_1 == "scissors" and player_2 == "scissors":
    print("tie")
else:
    print("invalid input")    
