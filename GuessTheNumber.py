import random
 
hidden = random.randrange(1, 10)
print(hidden)
 
guess = int(input("Guess a number between 1 and 10: "))
 
if guess == hidden:
    print("Correct!!")
elif guess < hidden:
    print("Your guess is too low")
else:
    print("Your guess is too high")
