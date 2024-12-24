height = float(input("Enter your Height (cm): "))
weight = float(input("Enter your Weight (kg):"))

BMI = weight/(height/100)**2

print(f"Your BMI is {BMI:.2f}")

if BMI < 18.5:
    print("You are Underweight.")
elif 18.5 <= BMI <= 24.9:
    print("You are Normal weight.")
elif 25.00 <= BMI <= 29.9:
    print("You are Overweight.")
elif 30.00 <= BMI <= 34.9:
    print("You are Obesity (Class 1).")
elif 35.00 <= BMI <= 39.9:
    print("You are Obesity (Class 2)")
else:
    print("You are Extreme Obesity (Class 3)")
