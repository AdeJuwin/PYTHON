class Mystring:
    def __iter__(self):
       self.user = input("enter string:")
       self.char_index = 0
       return self

    def __next__(self):
        if self.char_index < len(self.user):
            x = self.user[self.char_index]
            self.char_index += 1
            return x
        else:
            raise StopIteration

new= Mystring()
for i in new:
    print(i)

