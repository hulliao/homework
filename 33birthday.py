# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

# variables: people in classroom, school days
# n = 23
# c = 365
# practicing lists, loops, conditionals

import random
import math

# method 1
trials = 10000
classroom = 23
days = 365
success = 0

for a in range(trials):
    same = 0
    birthdays = []
    for i in range(classroom):
        birthdays.append(random.randint(1,days))
    for j in range(len(birthdays)):
        for k in range(j+1, len(birthdays)):
            if birthdays[j] == birthdays [k]: same +=1
    if same >= 1: success += 1

print(success / trials)

# method 2
list = []
days = 365
people = 23
trials = 1000
success = 0

for a in range(trials):
    calendar = [0] * days
    same = 0
    for i in range(people):
        birthday = random.randint(0, days-1)
        calendar[birthday] += 1
    for j in range(len(calendar)):
        if calendar[j] > 1: same += 1
    if same > 0: success += 1
print(success / trials)

"""
python3 33birthday.py 365 23
0.571
"""

