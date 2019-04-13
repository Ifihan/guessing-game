import random
number = random.randint(0,1000)
print(number)

while True:
    guess = input('Guess the number>>')
    if guess.isdigit() is True:
        guess = int(guess)
        if guess == number:
            print('You got it right!')
            break
        else:
            print('Wrong! Try again')
    else:
        print('Input a number')