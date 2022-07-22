import math

def even_odd(data): # a function to check if a number is even or odd
    for i in data:
        if i%2 == 0:
            print(i,"True")
        else:
            print(i, "False")

def perfect_sqrt(data): # function to check wheter a number is perfect or not
    for i in data:
        sqrt = math.sqrt(i)
        if int(sqrt)**2 == i:
            print(f"The number {i} is a perfect number")
        else:
            print(f"The number {i} is not a perfect number")


my_list = [79,128,1024,512,490,625,225,370,300,80,81,36,100,125] #given list


user = input("Select Operation (perfect, e&d):") #e&d mean even and odd operation while perfect means Perfect sq.
ops = "Operation not listed"                    #letting the user choose it operation
if user == 'perfect':
    perfect_sqrt(my_list)
elif user == 'e&d':
    even_odd(my_list)
else:
    print(ops)