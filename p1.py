number = 205
def outer_func(a):
    global number
    number = 103


    def inner_func():
        print(f"from the inner_func {number}")

    inner_func()
outer_func(210)

print(number)
