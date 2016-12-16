__author__ = 'jc451634'
from random import randint

num_of_picks = int(input("How many quick picks:"))

pick_of_6_numbers = []
num = 0

for i in range(0,num_of_picks):
  num = randint(1,45)
  for j in range(0, 6):
     while num in pick_of_6_numbers:
       num = randint(1,45)
     pick_of_6_numbers.append(num)

  print(sorted(pick_of_6_numbers))
  pick_of_6_numbers = []
