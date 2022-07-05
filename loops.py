x: int
for x in [2, 3, 5, 7, 8, 10]:
    product = x*2
    if product >6:
       continue
    if x == 5:
        product=x*3
    print(product)
if __name__ == "__main__":
    import math as m
    z=m.sqrt(25)
    print(z)

    u = eval(input("Enter your digit"))
    y = eval(input("Enter second digit"))
    w= u+y
    print(w)
b = bin(23)
print(b)

a = 3
c = 6
a,c = c,a

print(a)
print(c)
def add_num():
    a = int(input("User enter first digit:"))
    b = int(input("User enter second digit:"))
    z = a+ b
    print(z)
def sub_num():
    a = int(input("User enter first digit:"))
    b = int(input("User enter second digit:"))
    z = a-b
    print(z)

user= input('user enter operation *, -, +, /')
result ="Valid operation"

if user == '*':
    result = mul_num()

elif user == '-':
    result = sub_num()
elif user == '+':
    result = add_num()
else:
    print(result)


a = input('user enter 1st values:')
b = input('user enter 2nd values:')
c= input('user enter 3rd values:')

print(max(a,b,c))

e = int(input('enter desired number:'))
if e > 0:
    print("Positive Integer entered")
elif e < 0:
    print("Negative Integer entered")
else:
    print("Netural")
