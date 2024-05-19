from random import choice
import random 


while True:

    list = ["rock","paper","scissor"]

    computer_choice= random.choice(list)
    

    user_choice= input("Enter your choice between rock/paper/scissor ")
    print("Computer have choose",computer_choice)  
    print("You have choose",user_choice)

    if user_choice=="rock" and computer_choice== "paper":
            print ("Oops! Computer have won")

    elif user_choice=="paper" and computer_choice== "rock":
            print ("You  have won")

    elif user_choice=="scissor" and computer_choice== "paper":
            print ("You have won")

    elif user_choice=="paper" and computer_choice== "scissor":
        print ("Oops! Computer have won")

    elif user_choice=="rock" and computer_choice== "scissor":
        print ("You have won")

    elif user_choice=="scissor" and computer_choice== "rock":
        print ("Oops! Computer have won")

    elif user_choice==computer_choice:
         print("It's a tie")

    else:
        print("You have entered a wrong input")

    continuation=input("Do you want to play more? Yes/no")

    if continuation.lower() == 'no':
        print("Thank you for the game")
        break

