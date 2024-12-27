import PyCurrency_Converter

user_input = float(input("Enter your currency: "))
curr_type = input("Enter your currency type (e.g. USD, INR, BDT) : ").upper()
conver_type = input("Enter your convert type (e.g. USD, INR, BDT): ").upper()

result = PyCurrency_Converter.convert(curr_type, user_input, [conver_type])
print(result)