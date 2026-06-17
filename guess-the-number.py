import random
print("Welcome to the Guess the Number Game!")
x=int(input("Enter the maximum number for the range (1 to x): "))
random_number = random.randint(1, x)
guess=int(input("Guess the number:"))
while guess!=random_number:
    if guess<random_number:
        print("sorry your guess is too low, try again")
    else:
        print("sorry your guess is too high, try again")
    guess=int(input("Guess the number:"))
print("Congratulations! You guessed the number correctly:", random_number)