from random import choice

# Global variables to track stats across games
user_wins = 0
user_losses = 0
user_ties = 0

def play_rps():
    global user_wins, user_losses, user_ties
    
    # Get user input and validate
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    valid_choices = ["rock", "paper", "scissors"]
    
    if user_choice not in valid_choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return play_rps()  # Ask again for valid input
    
    # Computer makes choice
    computer_choice = choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
    
    # Determine winner and update stats
    if user_choice == computer_choice:
        print("It's a tie!")
        user_ties += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_wins += 1
    else:
        print("You lose!")
        user_losses += 1
    
    # Ask if player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_rps()
    else:
        # Display final stats when game ends
        print("Game Over")
        print(f"Wins: {user_wins}, Losses: {user_losses}, Ties: {user_ties}")
        total_games = user_wins + user_losses + user_ties
        if total_games > 0:
            win_percentage = (user_wins / total_games) * 100
            print(f"Win percentage: {win_percentage:.1f}%")

# Start the game
if __name__ == "__main__":
    print("Welcome to Rock Paper Scissors!")
    play_rps()