
def check_guess(guess, answer):
    global score
    still_geussing = True
    attempt = 0
    while still_geussing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer!!")
            score +=1
            still_geussing = False

        else:
            if attempt < 2:
                guess  = input("Sorry wrong answer. try again.  : " )
            attempt+=1

        if attempt == 3:
            print(f"Correct ans is {answer}")


score = 0
print("Guess the animal: ")
guess1 = input("Which bear is lives at the north pole? ")
check_guess(guess1, 'polar bear')
guess2 = input("Which is the fastest animal?")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the largest animal?")
check_guess(guess3, " Blue wheel")

print(f"Your score is {score} .")