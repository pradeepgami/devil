import random

def game():
    choices = ["rock", "paper", "scissors"]
    computer  = random.choice(choices)

    user = input ("Enter your choice (rock, paper, scissors): ").lower()
    while user not in choices:
        user = input("Invalid input. Please enter rock, paper or scissors: ").lower()

    print(f"\nYou chose {user},  random  chose { computer }.\n")

    if user == computer :
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if  computer  == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if  computer  == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

if __name__ == "__main__":
    game()