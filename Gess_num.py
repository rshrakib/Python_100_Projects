import random

attempts_lists = []

def show_score():
    if not attempts_lists:
        print("There are no high score it is all yours!!!")
    else:
        print(f"The current high score is {max(attempts_lists)} attempts.")

def start_game():
    attempts = 0
    rand_num = random.randint(1,10)
    print("Hello Travel! Welcome to the game of number guessing")
    player_name =  input("What is your name: ")
    wanna_play = input(f"Hi {player_name} would you like to play the guessing game? (enter y or n): ")

    if wanna_play.lower() !='y':
        print("That's cool. Thank you")
        exit()
    else:
        show_score()
    while wanna_play.lower() == 'y':
        try:
            guess = int(input("Pick a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                raise ValueError ("Please guess the number within the given range!!")
            attempts+=1
            attempts_lists.append(attempts)
            if guess == rand_num:
                print("You are correct!! You got right number..")
                print(f"It took you {attempts} attempts..")
                wanna_play = input("would you like to play again? ")
                if wanna_play.lower() !='y':
                    print("That's cool. Thank you")
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1,10)
                    show_score()
                    continue

            else:
                if guess > rand_num:
                    print("It is lower!")
                elif guess < rand_num:
                    print("It is higher!")
        except ValueError as err:
            print("Oh no! that is not a valid value!! Try again....")
            print(err)

if __name__ == "__main__":
    start_game()




