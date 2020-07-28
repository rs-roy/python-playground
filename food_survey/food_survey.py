#!/usr/bin/env python3

""" This program reads from a file named food.txt and shows if another person likes the same food"""

food_count = dict()
with open('food.txt', 'r') as handle:
    for line in handle:
        line = line.strip()
        food_count[line] = food_count.get(line, 0) + 1

for key in food_count:
    print("{}".format(key))

myfood = input("\nWhich of the above foods do you like? ")

if myfood.lower() in food_count:
    print("Wow, {} of your friends like the same food". format(food_count[myfood.lower()]))
else:
    print("You didn't choose any of the mentioned items. Exiting...")
