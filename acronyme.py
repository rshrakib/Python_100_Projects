user_input = input("Enter you word: ")

word = user_input.split( )

a = ""

for i in word:
    a = a+str(i[0].upper())
print(a)