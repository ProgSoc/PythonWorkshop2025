import random
from colorama import Fore, Style, init

init()

emojiDict = {
    "rock": "🪨",
    "paper": "📝",
    "scissors": "✂️",
}

winnersDict = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock",
}

choices = ["rock", "paper", "scissors"]


def main():

    user_score = 0

    computer_score = 0

    while (True):
        result = play_round()

        if result == "You won!":
            print(Fore.GREEN + Style.BRIGHT + result + Style.RESET_ALL)
            user_score += 1
        elif result == "You lost!":
            print(Fore.RED + Style.BRIGHT + result + Style.RESET_ALL)
            computer_score += 1
        else:
            print(Fore.YELLOW + Style.BRIGHT + result + Style.RESET_ALL)

        print(
            f"User - {Fore.GREEN} {user_score} {Style.RESET_ALL} Computer - {Fore.RED} {computer_score} {Style.RESET_ALL}")

        play_again = input("Keep Playing? (y/n) : ")
        if play_again.strip() == "n":
            break


def play_round():
    print("Welcome to the game!")

    user_choice = get_user_choice()

    print("You selected " + emojiDict[user_choice])

    computer_choice = get_computer_choice()

    print("Computer selected " + emojiDict[computer_choice])

    result = determine_winner(user_choice, computer_choice)

    return result


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    if (winnersDict[computer_choice] == user_choice):
        return "You won!"
    else:
        return "You lost!"


def get_computer_choice():
    return random.choice(choices)


def get_user_choice():
    user_choice = input(
        "Enter 'rock', 'paper', or 'scissors': ").lower().strip()

    while user_choice not in choices:
        print(Fore.YELLOW + "Invalid choice. Please enter 'rock', 'paper', or 'scissors'." + Style.RESET_ALL)
        user_choice = input(
            "Enter 'rock', 'paper', or 'scissors': ").lower().strip()

    return user_choice


main()
