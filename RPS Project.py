def game(user_pick, computer_pick, os, user_name, random, wins, losses):

    # Sets up responses for every result

    if user_pick.title() == "R":
        user_pick = "rock"

    elif user_pick.title() == "P":
        user_pick = "paper"

    elif user_pick.title() == "S":
        user_pick = "scissors"
    
    elif user_pick.title() == "Q":
        print("\nGoodbye!") 
        print("\nWins: " + str(wins) + "\nLosses: " + str(losses))
        exit()

	# Response for an unknown input
	
    else: 
        os.system('cls')
        print("Enter a real option, you fucking pussy.")
        input("\nPress enter to continue...")
        os.system('cls')
        user_pick = input("Exit with (Q)uit, or Enter (R)ock, (P)aper, or (S)cissors: ")
        game(user_pick, computer_pick, os, user_name, random, wins, losses)

	# Shows what the player chose
		
    print("\n" + user_name + " chose " + str(user_pick) + "!")
	
	# Sets the computer's number choice to rock, paper, or scissors 
	
    if computer_pick == 1:
        computer_pick = "rock"
        print("\nThe computer chose " + str(computer_pick) + "!")
        input("\nPress enter to continue...")

    if computer_pick == 2:
        computer_pick = "paper"
        print("\nThe computer chose " + str(computer_pick) + "!")
        input("\nPress enter to continue...")

    if computer_pick == 3:
        computer_pick = "scissors"
        print("\nThe computer chose: " + str(computer_pick) + "!")
        input("\nPress enter to continue...")

    # Rock responses
    
    if user_pick == "rock" and computer_pick == "rock":
        os.system('cls')
        print("Tie game!")
        print("\nTry another choice.")
        input("\nPress enter to continue...")
        os.system('cls')
        user_pick = input("Exit with (Q)uit, or Enter (R)ock, (P)aper, or (S)cissors: ")
        computer_pick = random.randint(1, 3)
        game(user_pick, computer_pick, os, user_name, random, wins, losses)

    if user_pick == "rock" and computer_pick == "paper":
        os.system('cls')
        print("The computer wins!")
        losses += 1
        print("\nWins: " + str(wins) + "\nLosses: " + str(losses))
        input("\nPress enter to continue...")
        os.system('cls')
        user_pick = input("Exit with (Q)uit, or Enter (R)ock, (P)aper, or (S)cissors: ")
        computer_pick = random.randint(1, 3)
        game(user_pick, computer_pick, os, user_name, random, wins, losses)
        
    if user_pick == "rock" and computer_pick == "scissors":
        os.system('cls')
        print(str(user_name) + " wins!")
        wins += 1
        print("\nWins: " + str(wins) + "\nLosses: " + str(losses))
        input("\nPress enter to continue...")
        os.system('cls')
        user_pick = input("Exit with (Q)uit, or Enter (R)ock, (P)aper, or (S)cissors: ")
        computer_pick = random.randint(1, 3)
        game(user_pick, computer_pick, os, user_name, random, wins, losses)
         
    # Paper responses
    
    if user_pick == "paper" and computer_pick == "rock":
        os.system('cls')
        print(str(user_name) + " wins!")
        wins += 1
        print("\nWins: " + str(wins) + "\nLosses: " + str(losses))
        input("\nPress enter to continue...")
        os.system('cls')
        user_pick = input("Exit with (Q)uit, or Enter (R)ock, (P)aper, or (S)cissors: ")
        computer_pick = random.randint(1, 3)
        game(user_pick, computer_pick, os, user_name, random, wins, losses)
        
    if user_pick == "paper" and computer_pick == "paper":
        os.system('cls')
        print("Tie game!")
        print("\nTry another choice.")
        input("\nPress enter to continue...")
        os.system('cls')
        user_pick = input("Exit with (Q)uit, or Enter (R)ock, (P)aper, or (S)cissors: ")
        computer_pick = random.randint(1, 3)
        game(user_pick, computer_pick, os, user_name, random, wins, losses)
        
    if user_pick == "paper" and computer_pick == "scissors":
        os.system('cls')
        print("The computer wins!")
        losses += 1        
        print("\nWins: " + str(wins) + "\nLosses: " + str(losses))
        input("\nPress enter to continue...")
        os.system('cls')
        user_pick = input("Exit with (Q)uit, or Enter (R)ock, (P)aper, or (S)cissors: ")
        computer_pick = random.randint(1, 3)
        game(user_pick, computer_pick, os, user_name, random, wins, losses)
        
    # Scissors responses
    
    if user_pick == "scissors" and computer_pick == "rock":
        os.system('cls')
        print("The computer wins!")
        losses += 1
        print("\nWins: " + str(wins) + "\nLosses: " + str(losses))
        input("\nPress enter to continue...")
        os.system('cls')
        user_pick = input("Exit with (Q)uit, or Enter (R)ock, (P)aper, or (S)cissors: ")
        computer_pick = random.randint(1, 3)
        game(user_pick, computer_pick, os, user_name, random, wins, losses)

    if user_pick == "scissors" and computer_pick == "paper":
        os.system('cls')
        print(str(user_name) + " wins!")
        wins += 1
        print("\nWins: " + str(wins) + "\nLosses: " + str(losses))
        input("\nPress enter to continue...")
        os.system('cls')
        user_pick = input("Exit with (Q)uit, or Enter (R)ock, (P)aper, or (S)cissors: ")
        computer_pick = random.randint(1, 3)
        game(user_pick, computer_pick, os, user_name, random, wins, losses)
        
    if user_pick == "scissors" and computer_pick == "scissors":
        os.system('cls')
        print("Tie game!")
        print("\nTry another choice.")
        input("\nPress enter to continue...")
        os.system('cls')
        user_pick = input("Exit with (Q)uit, or Enter (R)ock, (P)aper, or (S)cissors: ")
        computer_pick = random.randint(1, 3)
        game(user_pick, computer_pick, os, user_name, random, wins, losses)
    
def main():

    # Import libraries for random.randint and os.system('cls')

    import random, os

    # Program begins

    print("Rock, Paper, Scissors!")
    input("\nPress enter to continue...")
    os.system('cls')

    # Defines variables in game()
    user_name = input("Enter your name: ")
    user_pick = input("\nExit with (Q)uit, or Enter (R)ock, (P)aper, or (S)cissors: ")
    wins = 0
    losses = 0
    computer_pick = random.randint(1, 3) 
    user_pick = game(user_pick, computer_pick, os, user_name, random, wins, losses)

main()
game(user_pick, computer_pick, os, user_name, random, wins, losses)
