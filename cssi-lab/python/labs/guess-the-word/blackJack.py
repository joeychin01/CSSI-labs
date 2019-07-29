import random
random.seed()
money = 500
moneyBet = 0
userScore = 0
compScore = 0
random.seed()
deckBackup = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]

def deal():
    global userScore
    global compScore
    global money
    global moneyBet
    if money == 0:
        money = 500
        print("You're broke - so we gave you another 500 dollars")
    moneyBet = raw_input("Please put how much you want to bet: ")
    if int(moneyBet) > money:
        print("You don't have that much money, so you're all in!")
        moneyBet = money
    elif int(moneyBet) < 0:
        print("You can't bet that little, so you are betting $1")
        moneyBet = 1
    card1 = getCard()
    card2 = getCard()
    print("You drew a "+str(card1)+" and a "+str(card2))
    userScore = int(card1) + int(card2)
    compScore = getCard()+getCard()

def getCard():
    index = random.randint(0, len(deck) - 1)
    returnVal = deck[index]
    deck.remove(returnVal)
    return returnVal

def play():
    # check to see blackjack/bust
    # ask for another card
    global money
    global moneyBet
    while(True):
        global userScore
        if userScore > 21:
            print("Sorry, you busted, so you lose your money")
            userScore = -2
            break
        else:
            print("You currently have "+ str(userScore) + " points, do you want to get another card?")
            choice = raw_input("[y/n] :")
            if choice == "y":
                card = getCard()
                userScore = userScore + card
                print("You drew a " + str(card) + " and your total is now " + str(userScore))
            elif choice == "n":
                print("Your final total is "+ str(userScore) + ", now let us see how the computer does")
                computerTurn()
                break
            else:
                print("Enter a valid guess")

def computerTurn():
    # let the computer go until over 17 or busts
    global compScore
    print("The computer currently has "+str(compScore)+" points")
    while True:
        if compScore > 21:
            print("The computer busted!")
            compScore = -1
        elif compScore >= 17 and compScore <= 21:
            print("The computer rests at "+str(compScore))
            break
        else:
            card = getCard()
            compScore = compScore + card
            print("The computer hits, and draws a "+str(card)+" bringing their total up to "+str(compScore))
    checkWin()

def checkWin():
    global money
    if userScore > compScore:
        print("You beat the computer!")
        money = int(money) + int(moneyBet)
        print("You have "+ str(money) + " dollars")
    elif userScore < compScore:
        print("The computer beat you.")
        money = int(money) - int(moneyBet)
        print("You have "+ str(money)+ " dollars left")
    else:
        print("You tied, so nothing happened")

while True:
    if len(deck) < 10:
        print("The deck is running low, so we are refreshing the deck")
        deck = deckBackup
    deal()
    play()
    choice = raw_input("Do you want to play again? [y/n]")
    if choice == "n":
        break
    else:
        "You are playing again!"
