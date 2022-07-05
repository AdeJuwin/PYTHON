def multiple_number():
    a = int(input("kindly enter an integer:"))
    b = int(input("kindly enter an integer:"))
    return a*b

def add_number():
    a = int(input("kindly enter an integer:"))
    b = int(input("kindly enter an integer:"))
    return a+b

def division_number():
    a = int(input("kindly enter an integer:"))
    b = int(input("kindly enter an integer:"))
    return a/b

def sub_number():
        a = int(input("kindly enter an integer:"))
        b = int(input("kindly enter an integer:"))
        return a-b

user = input("Enter Operation (*,-,+,/):")
result ="Operation not Valid"

if user == "*":
    result = multiple_number()
elif user == "-":
    result = sub_number()
elif user == "/":
    result = division_number()
elif user == "+":
    result = add_number()
print(result)


