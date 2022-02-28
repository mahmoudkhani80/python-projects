import random

random_number = random.randint(0,100)
guessed_number =int(input("i guess a number can you tell it :"))

if guessed_number < random_number:
    print("no, more than that")
elif guessed_number > random_number:
    print("no, less than that")
else:
    print("right")
y = 0
x = 1
while x < 2:
    after_first_guess = int(input("test your luck one more time :"))
    if after_first_guess < random_number:
        y = y + 1
        print("nope, more")
    elif after_first_guess > random_number:
        y = y + 1
        print("nope, less")
    else:
        print("right")
        print("you try",y,"times well done")
        break
input("Press 'ENTER' to quit")