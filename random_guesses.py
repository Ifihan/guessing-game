#A GUESSING GAME
import random
import sys #to ensure the code runs from terminal
number = random.randint(int(sys.argv[1]),int(sys.argv[2])) #set the boundaries by typing them into the terminal
#print(number)
while True: 
    guess = input('Guess the number: ')
    if guess.isdigit() is True:
        guess = int(guess)
        if guess >= 0 and guess <= 1000:
            if guess == number:
                print('You got it right!')
                break
        else:
            print('Wrong! Try again')
            break                
    else:
        print('Input a number when next you run this!')
    
    
