print("this simple Python program asks for 8 diferent names and picks one of them at random")

import random

x = 1
names = []

while x <= 8:
  name = input(str(x) + ". Enter name: ")
  names.append(name)
  x += 1

pos = random.randint(0,8)
print("random name selected is at position ", pos)
print("random name is", names[pos])
