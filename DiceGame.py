from random import randint

name = input("What is your name?\n> ")
print(f"Hello, {name}!")

die1 = randint(1, 6)
die2 = randint(1, 6)
print("Rolling dice...")
print(f"Die 1: {die1}")
print(f"Die 2: {die2}")
print(f"Total value: {die1 + die2}")