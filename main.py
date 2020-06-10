import random

print("this simple Python program asks for 8 diferent names and picks one of them at random")

x = 1  #start counter
names = []  #list that holds names

while x <= 8:
  name = input(str(x) + ". Enter name: ")
  names.append(name)
  x += 1

pos = random.randint(0,8)
print("random name selected is at position ", pos)
print("random name is", names[pos])