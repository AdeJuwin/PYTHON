my_tuple=("green",)
print(my_tuple)

y = ("Nigeria",)
my_tuple+=y
print(my_tuple)

my_list=list(my_tuple)
my_list.append("Dummy")
my_tuple=tuple(my_list)
print(my_tuple)

my_type=type(my_tuple)
print(my_type)

second=my_tuple[2]
print(second)

#unpacking Tuples
my_2tuple = ("Nigeria", "Ghana", "Senegal")
(purple, Red, *Blue) = my_2tuple
print(Blue)
