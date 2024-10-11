import random

secret_number = random.randint(1, 10)

guess = int(input("guess a number from 1 to 10. "))

if guess > secret_number:
    print("too high")

elif guess < secret_number:
    print("too low")

else:
    print("correct")