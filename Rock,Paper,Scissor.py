# Computers choice
import random
a=["Rock","Paper","Scissor"]
computer_choice=random.choice(a)

player_score=0
computer_score=0

while True:
    player_choice=input("Enter your choice:")
    if player_choice==computer_choice:
        print("tie")
        player_score+=1
        computer_score+=1
    elif player_choice=="Rock":
        if computer_choice=="Paper":
            computer_score+=1
        if computer_choice=="Scissor":
            player_score+=1

    elif player_choice=="Paper":
        if computer_choice=="Scissor":
            computer_score+=1
        if computer_choice=="Rock":
            player_score+=1

    elif player_choice=="Scissor":
        if computer_choice=="Rock":
            computer_score+=1
        if computer_choice=="Paper":
            player_score+=1

    else:
        print("Final Scores")
        print(player_score)
        print(computer_score)
        break