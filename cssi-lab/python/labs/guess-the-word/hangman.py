import random
random.seed()
words = ["javascript", "monkey", "amazing", "pancake", "galvainze", "cohort", "concatenate", "iteration", "index", "code", "angular", "react", "python", "allonsy"]
word = words[random.randint(0, len(words))]
spaces = []
haveWon = False
mistakes = 0
guesses = []
print("Thank you for choosing to play hangman. Guess letters, but remember, three mistakes means game over!")
for i in range(len(word)):
    spaces.append(False)
while "true":
    if mistakes < 3:
        if not haveWon:
            hint = ""
            for i in range(len(word)):
                if(spaces[i]):
                    hint += word[i]
                else:
                    hint += "_"
                hint += " "
            print hint
            guess = raw_input("Please enter your guess: ")
            for i in range(len(guesses)):
                if guess == guesses[i]:
                    print("You already guessed that!")
            guesses.append(guess)
            if(len(guess) == 1):
                numRight = 0
                for i in range(len(word)):
                    if word[i] == guess:
                        spaces[i] = True
                        numRight = numRight + 1
                if numRight != 0:
                    print("There are " + str(numRight) +
                          " mentions of " + str(guess) + " in the word")
                else:
                    mistakes = mistakes + 1
                    print("You made a mistake, and now have a total of "+str(mistakes)+" mistakes! Remember, three mistakes equals game over...")

            else:
                print("That guess is longer than a letter")
            haveWon = True
            for i in range(len(word)):
                if not spaces[i]:
                    haveWon = False
        else:
            print("You won!")
            break
    else:
        print("You Lost!")
        break
