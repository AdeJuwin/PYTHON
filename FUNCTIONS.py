def my_prac(*data):
    if type(data) is tuple:
        print("We have a tuple file")
        if data ==():
                print("An empty data is being entered")
        else:
            x =0
            for y in data:
                x += y
                print (x)

    else:
        print("Enemy in the water")

def my_dict(**data):
    if data == {}:
        print("Empty Dictionary")
    else:
        my_exp =0
        for value in data.values():
            my_exp= my_exp+(value['salary'])
            print(f"My expenses for the month is :{my_exp}")
            if my_exp > 21000:
                print("Sack two workers")
            else:
                print("The Company is in a good shape")
def speed_cal(speed):
    min_speed = 120
    if speed < min_speed:
        print("Everything is Ok")
    elif speed >=120:
        point=(speed-120)//10
        print(f"You have a total number of {point} demerits, be careful")
        if point >= 10:
            print("License Suspended, Report to NPF Headquarters")

if __name__ == '__main__':

    my_prac()
    my_dict(emp1={'name': 'Bille', 'salary': 9000},emp2={'name': 'Israel', 'salary': 8005},
                 emp3={'name': 'Katherine', 'salary': 9010})
    speed_cal(250)