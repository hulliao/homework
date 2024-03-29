# dnd2-piercer.py

import random

# If you have the "Piercer" feat, you may re-roll a damage die. You must
# take the new roll regardless if it was lower than the previous roll. Assume
# you have a weapon that does 1d8 damage. Clearly, you should re-roll any die
# with an initial roll of 1 damage. But what about higher rolls? Your friend
# Jorg re-rolls 1-5. But Gastin says that's too high and re-rolls 1-3.
# What is the optimal strategy? Simulate it.
# Make a table showing reroll threshold (use <=) and average damage.

trials = 10000
for threshold in range(2,8):
    jorg = 0
    for j in range(trials):
        roll = random.randint(1,8)
        if roll <= threshold: roll = random.randint(1,8)
        jorg += roll
    print(threshold, f'{jorg / trials}')

"""
python3 dnd2-piercer.py
2 5.251
3 5.437
4 5.500
5 5.438
6 5.250
7 4.938
"""
