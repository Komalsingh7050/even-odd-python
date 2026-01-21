import random

number = random.randint(1, 100)
while True:
   try:
    guess = int(input("guess this number between 1 to 100 "))
    if guess < number:
      print("too low")
    elif guess > number:
      print("too high")
    else:
      print("Well Done")
   except ValueError:
    print("Enter a valid number ")
