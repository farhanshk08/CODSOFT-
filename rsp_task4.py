import random #import random module in python

def determine_winner(player_choice, computer_choice): #takes players and random computer generated choice
    if player_choice== computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissor') or \
         (player_choice == 'scissor' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "you win!"
    else:
        return "you lose!"

def play(): #main game loop
    user_score, computer_score = 0, 0
    choices = ['rock','paper','scissor']

    while True:
        print("\nRock,Paper,Scissor game!") 
        player_input = input("Enter your choice or type 'exit' to quit: ").lower() #take user input

        if player_input=='exit': #check if user wants to quit
            break
        
        if player_input not in choices: #check if user input is valid
            print("Please enter valid innput:")
            continue
        
        computer_choice=random.choice(choices) #randomly choose from choices list
        print("\nYou chose: ",player_input)
        print("Computer chose:",computer_choice)

        result =determine_winner(player_input, computer_choice) #determine winner
        print(result)

        user_score += result== "you win!" #increment user score if user wins
        computer_score += result== "you lose!" #increment computer score if computer wins

        print(f"Your Score:",user_score," Computer Score: ",computer_score) #print score

    print("Thanks for playing!")

play() #call play() function