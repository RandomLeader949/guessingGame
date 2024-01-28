import random
number = random.randint(1, 10)
guess = int(input("What number am I thinking of? "))
while guess != number:
    if guess > number:
        print("This is too high")
    else:
        print("This is too low")
    guess = int(input("What number am I thinking of? "))
if guess == number:
    print("Correct!")