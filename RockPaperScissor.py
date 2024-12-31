import random
import os
import re

def check_play_status():
    valid_response = ['yes', 'no']
    while True:
        try:
            response  = input("Do you want to play again: ")
            if response.lower() not in valid_response:
                raise ValueError("Yes or No only")
            if response.lower()=='yes':
                return True
            else:
                os.system("cls" if os.name == 'nt' else 'clear')
                print("Thanks for Playing")
                exit()
        except ValueError as err:
            print(err)


def play_rps():
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print("Rock, Paper, Scissors - shoot!")

        user_choice = input("choose your weapon [R]ock, [P]aper or [S]cissors: ")
        if not re.match("[SsRrPp]", user_choice):
            print("Please choose a latter ")
            print("[R]ock, [P]aper or [S]cissors")
            continue
        print(f"You choose: {user_choice} ")

        choices = ['R', 'P', 'S']
        app_choice = random.choice(choices)

        print(f"Computer choose: {app_choice}")
        if app_choice == user_choice.upper():
            print("Tie")
            play = check_play_status()

        elif app_choice == 'R' and user_choice.upper() == 'S':
            print("Rock beats scissors, computer win")
            play = check_play_status()
        elif app_choice == 'S' and user_choice.upper() == 'P':
            print("Scissors beats paper! computer win")
            play = check_play_status()
        elif app_choice == 'P' and user_choice.upper() =='R':
            print("Paper beats rocks! computer win")
            play = check_play_status()
        else:
            print("You win!")
            play = check_play_status()

if __name__ == "__main__":
    play_rps()
