import random

print("""Choose the difficulty of the game
a. easy
b. medium
c. hard """)
dif=input(': ')
if dif == "a" :
    n=1
elif dif == "b" :
    n=2
else :
    n=3
guessNumb = random.randrange(1,n*10)
print(f"choose a number in range 1,{n*10}")
print('You have 5 tries to guess the number')
choiceArrey=['first','second', 'third','forth' , 'fifth']
for i in choiceArrey :
    userGuess = int(input(f'Your {i} guess is: '))

    if userGuess < guessNumb and i != 'fifth':
        print(f"It's greater than {userGuess}")
    elif userGuess > guessNumb and i != 'fifth':
        print(f"It's lower than {userGuess}")
    elif userGuess == guessNumb:
        print(f"{userGuess} is the correct number")
        break
else:
    print(f"The number was {guessNumb} You've lost")