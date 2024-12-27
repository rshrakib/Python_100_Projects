import random
import os

def dice_num():
    while True:
        try:
            num_dice = input("Number of dice: ")
            valid_response = ['1', 'one', '2', 'two']
            if num_dice not in valid_response:
                raise ValueError ('1 or 2 only')
            else:
                return num_dice
        except ValueError as err:
            print(err)

def role_dice():
    min_val = 1
    max_val = 6
    roll_again = 'y'

    while roll_again.lower()=='y':
        os.system('cls' if os.name == 'nt' else 'clear')
        amount =  dice_num()

        if amount =='2' or amount == 'two':
            print("Rolling dice....")
            dice_1= random.randint(min_val,max_val)
            dice_2 = random.randint(min_val,max_val)

            print('The values are: ')
            print("Dice one: ", dice_1)
            print('Dice Two: ', dice_2)
            print('Total: ', dice_1+dice_2)

            roll_again = input('Roll again? : ')
        else:
            print("Rolling the dice...")
            dice_1 = random.randint(min_val, max_val)
            print("The value is: ", dice_1)

            roll_again = input("Roll again? : ")


if __name__ == "__main__":
    role_dice()

