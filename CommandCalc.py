import os

def addition():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Addition")


    continue_cal = 'y'

    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))

    ans = num1 + num2
    values_entered = 2
    print(f"Current result: {ans}")

    while continue_cal.lower() == 'y':
        continue_cal = (input("Enter more (y/n): "))

        while continue_cal.lower() not in ['y','n']:
            print("Please enter \'y\' or '\'n\' ")
            continue_cal = input("Enter more (y/n): ")

        if continue_cal.lower() == 'n':
            break
        num = float(input("Enter another number: "))
        ans = ans + num
        print(f"Current result: {ans}")
        values_entered +=1
    return [ans, values_entered]

def subtraction():
    os.system('cls' if os.name=='nt' else 'clear')
    print("Subtraction")
    continue_cal = 'y'
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    ans  = num1 - num2
    values_entered = 2
    print(f"Current result: {ans}")

    while continue_cal.lower() == 'y':
        continue_cal = (input("Enter more (y/n): "))
        while continue_cal.lower() not in ['y','n']:
            print("Please enter \'y\' or \'n\' ")
            continue_cal = (input("Enter more (y/n): "))

        if continue_cal.lower() == 'n':
            break

        num = float(input("Enter another number: "))
        ans-=num
        print(f"Current result: {ans}")
        values_entered+=1
        return [ans, values_entered]


def multiplication():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Multiplication")

    continue_cal = 'y'
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))

    ans = num1 * num2
    value_entered = 2

    print(f"Current result : {ans}")

    while continue_cal.lower() == 'y':
        continue_cal = (input("Enter more (y/n): "))
        while continue_cal.lower() not in ['y','n']:
            print("Please enter \'y\' or \'n\'")
            continue_cal = (input("Enter more (y/n): "))
        if continue_cal.lower() == 'n':
            break
        num = float(input("Enter another number: "))
        ans = ans * num
        print(f"Current result: {ans}")
        value_entered+=1
        return [ans,value_entered]

def division():
    os.system('cls' if os.name == 'nt' else "clear")
    print("Division")

    continue_cal = 'y'
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))

    ans = num1/num2
    value_entered = 2
    print(f"Current result: {ans}")

    while continue_cal.lower() == 'y':
        continue_cal = (input("Enter more (y/n): "))
        while continue_cal.lower() not in ['y','n']:
            print("Please enter \'y\' or \'n\' ")
        if continue_cal.lower() == 'n':
            break
        while True:
            num = float(input("Enter another number: "))
            if num == 0:
                print("Cannot divide by zero. Please enter a valid number.")
            else:
                break
        ans = ans/num
        print(f"Current result: {ans}")
        value_entered+=1
        return [ans, value_entered]

def main():
    print("Welcome to calculator!!")
    print("1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. Exit")
    user_input = input("Enter your choice(1/2/3/4/5): ")
    if user_input == '1':
        result = addition()
        print("Ans = ", result[0], "Total input: ", result[1])
    elif user_input == '2':
        result = subtraction()
        print("Ans = ", result[0], "Total input: ", result[1])
    elif user_input == '3':
        result = multiplication()
        print("Ans = ", result[0], "Total input: ", result[1])
    elif user_input == '4':
        result = division()
        print("Ans = ", result[0], "Total input: ", result[1])
    elif user_input == '5':
        print("Thank you.. Exiting... ")
        exit()
    else:
        print("Enter correct choice...")

while True:
    main()

