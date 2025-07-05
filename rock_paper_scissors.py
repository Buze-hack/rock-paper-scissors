import random 

choices = ["rock", "paper", "scissors"]

def get_computer_choice() -> str:
    return random.choice(choices)

def get_user_choice() -> str:
    while True:
        choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please try again.")

def determine_winner(user: str, computer: str) -> str:
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
        return "draw"
    
    elif user == "rock":
        if computer == "scissors":
            print("You win! Rock crushes scissors.")
            return "user"
        else:
            print("You lose! Paper covers rock.")
            return "computer"
        
    elif user == "paper":
        if computer == "rock":
            print("You win! Paper covers rock.")
            return "user"
        else:
            print("You lose! Scissors cut paper.")
            return "computer"
        
    elif user == "scissors":
        if computer == "paper":
            print("You win! Scissors cut paper.")
            return "user"
        else:
            print("You lose! Rock crushes scissors.")
            return "computer"

def main():
    user_score = 0
    computer_score = 0
    rounds = 3

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score => You {user_score} | Computer: {computer_score}")
    
    print("\nFinal Scores:")
    if user_score > computer_score:
        print("Congratulations! You win the game!")
    elif computer_score > user_score:
        print("Computer wins the game")
    else:
        print("The game is a draw!")

if __name__ == "__main__":
    main()