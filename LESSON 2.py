my_list=['windows', 'israel', 'love', 'lola']
#print(my_list)

my_list.sort(key=str.lower)
#print(my_list)

#for item in my_list:
 #   print(item)

#i = 0
#while i < len(my_list):
 #   print(my_list[i])
  #  i = i +1

#my_list.append("Cynthia")
#print(my_list)

my_list.insert(0, "Parrot")
print(my_list)

my_list.pop()
print(my_list)

#my_list.extend()

my_list.sort(key=str.lower)
print(my_list)

#my_list[0:2] = "New Element", "bad", "Rain"
#print(my_list)

#print(my_list[0])
#def closest(numbers, k):
 #   return numbers.sort[min(range(len(numbers)), key = lambda i: abs(numbers[i]-k))]


def modify(x):
    return abs(x-50)
numbers=[100,30,40, 20, 30, 40, 60, 90]
numbers.sort(key=modify)
print(numbers)
