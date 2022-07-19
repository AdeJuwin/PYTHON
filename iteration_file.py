class Numbers:
    def __iter__(self):
        self.a =1
        return self

    def __next__(self):
        if self.a <=5:
            x = self.a
            self.a+=1
            return x
        else:
            raise StopIteration

my_num = Numbers()
my_it = iter(my_num)
for x in my_it:
    print(x)


my_tuples = ("Nigeria")
my_char = iter(my_tuples)
print(next(my_char))
print(next(my_char))
print(next(my_char))
print(next(my_char))



