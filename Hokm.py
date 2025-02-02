import random
from time import sleep

# Diamond = D
# Clubs = C
# Spades = S
# Harts = H
# Jack = J
# Queen = Q
# King = K
# Ace = A

# note: you can understand the whole program by looking at codes in line ,its the algorithm

# The necessary variables
suits = ['D', 'C', 'S', 'H']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [s + r for s in suits for r in ranks]
deckCopy = deck[:]
players = ["user", "player2", "player3", "player4"]
winsA = 0
winsB = 0
userHand = []
player2Hand = []
player3Hand = []
player4Hand = []
j = 0
t = 0
turn = players[j]
handWonA = 0
handWonB = 0
trumper = ''
trump = ''
choiceCard = ''
groundCards = []
goneCards = []


# The functions
def WhoIsTrumper(j, t, trumper):
    # its the first game
    if winsA == 0 and winsB == 0:
        j = random.randint(0,3)
        t = j
        trumper = players[j]
        print(f'\nThe trumper is {trumper}')

    # its not the first game
    else:
        # trumper is in team A and they won: just continue
        if (j == 0 or j == 2) and handWonA == 7:
            t = j
            trumper = players[j]
            print(f'\nThe trumper is {trumper}')
        # trumper is in team B and they won: just continue
        elif (j == 1 or j == 3) and handWonB == 7:
            t = j
            trumper = players[j]
            print(f'\nThe trumper is {trumper}')
        # if trumper is in team A or B and they loses: trumper is the next one
        else:
            j += 1
            if j == 4:
                j = 0
            t = j
            trumper = players[j]
            print(f'\nThe trumper is {trumper}')
    return j, t, trumper

def ShuffleAndSpread():
    random.shuffle(deckCopy)
    for times in range(13):
        userHand.append(deckCopy[0])
        deckCopy.pop(0)
    for times in range(13):
        player2Hand.append(deckCopy[0])
        deckCopy.pop(0)
    for times in range(13):
        player3Hand.append(deckCopy[0])
        deckCopy.pop(0)
    for times in range(13):
        player4Hand.append(deckCopy[0])
        deckCopy.pop(0)

def SortHand(hand):
    suit_order = {'C': 0, 'D': 1, 'H': 2, 'S': 3}
    rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
    return sorted(hand, key=lambda x: (suit_order[x[0]], rank_order[x[1:]]))



def ShowHand(hand):
    print(hand)

def WhatIsTrump(trumper):
    if trumper == 'user':
        while True:
            trump = input('You are the trumper, Please determine the trump by interring D, H, C or S:')
            trump = trump.upper()
            if trump in suits:
                break
            else:
                print('error, please just type D, H, C or S to determining the trump.')
    else:
        trump = random.choice(suits)
    print(f'\n***  The trump is {trump}  ***\n')
    return trump

def WhoseTurn(t):
    turn = players[t]
    return turn

def AskWhatToPlay(userHand, groundCards):
    while True:
        choiceCard = input('Your turn, What card do you play:')
        choiceCard = choiceCard.upper()
        # check the card is in his/her hand if yes(more checking) if not (no)
        if choiceCard in userHand:
            # check if it's the first card that is played if yes(ok) if no (more checking)
            if len(groundCards) != 0:
                # check if it's the same suit with the first card played if yes(ok) if trump (more checking) if etc(more checking)
                if choiceCard[0] == groundCards[0][0]:
                    groundCards.append(choiceCard)
                    userHand.remove(choiceCard)
                    return choiceCard
                    break
                elif choiceCard[0] == trump:
                    # (more checking)
                    for card in userHand:
                        if card[0] == groundCards[0][0]:
                            print("error,you have that suit;) play that,retry.")
                            break
                    else:
                        groundCards.append(choiceCard)
                        userHand.remove(choiceCard)
                        return choiceCard
                        break
                else:
                    # (more checking)
                    for card in userHand:
                        if card[0] == groundCards[0][0]:
                            print("error,you have that suit;) play that,retry.")
                            break
                    else:
                        groundCards.append(choiceCard)
                        userHand.remove(choiceCard)
                        return choiceCard
                        break
            # first card
            else:
                groundCards.append(choiceCard)
                userHand.remove(choiceCard)
                return choiceCard
                break
        else:
            print('error, this is not in your hand, retry.')

def WhatCardToPlay(playerHand, groundCards, player_name):    
    pickedCard = random.choice(playerHand)
    groundCards.append(pickedCard)
    playerHand.remove(pickedCard)
    if player_name == 'player3':
        print(f'{player_name} dropped: {pickedCard} (your teammate)')
    else:
        print(f'{player_name} dropped: {pickedCard}')
    return pickedCard

def WhoWins(t, groundCards, trump):
    firstCard = groundCards[0]
    winnerCard = firstCard  # Initialize with the first card  # Initialize with the first card
    hasTrump = False

    def CheckTrump():
        nonlocal winnerCard, hasTrump  # Use nonlocal to modify the outer variable
        hasTrump = False
        for card in groundCards:
            # find the trump cards
            if card[0] == trump:
                # when it's the first trump found
                if not hasTrump:
                    winnerCard = card
                    hasTrump = True
                # when it's not the first trump found check witch one is higher rank
                elif ranks.index(card[1:]) > ranks.index(winnerCard[1:]):
                    winnerCard = card
            else:
                pass
    def CheckNotTrump():
        nonlocal winnerCard
        winnerCard = firstCard # Start with the first card
        for card in groundCards[1:]:  # Skip the first card
            # when is the same suit to firstCard
            if card[0] == firstCard[0]:
                # check witch one is higher rank
                if ranks.index(card[1:]) > ranks.index(winnerCard[1:]):
                    winnerCard = card
            # when is not the same suit to firstCard
            else:
                pass

    # Determine if there is a trump card in groundCards
    for card in groundCards:
        if card[0] == trump:
            hasTrump = True
            break

    # Check for trump cards or determine the winner based on the first card's suit
    if hasTrump:
        CheckTrump()
    else:
        CheckNotTrump()
    
    print("Ground cards:", groundCards)
    print("Winner card:", winnerCard)

    # determine the winnerCard was from witch player

    # we have to find t of that player by index of winnerCard in the groundCards:
    # we know how dropped the last card(by the current value of t)
    # we plus it 1 to reach the first player who dropped card
    # then we add the index of that winnerCard to determine the winner
    winner_index = groundCards.index(winnerCard)
    t = (t + 1 + winner_index) % 4
    # now we had specified t to winner player so he/she will start next round
    return t
    
def CountHandWins(t, handWonA, handWonB):
    if t == 0 or t == 2:
        handWonA += 1
        print('\nTeam A wins a hand!!')
    elif t == 1 or t == 3:
        handWonB += 1
        print('\nTeam B wins a hand!!')
    return handWonA, handWonB

def CountWins(winsA, winsB):
    # Hakem kot
    if handWonA == 7 and handWonB == 0 and (trumper == 'player2' or trumper == 'player4'):
        winsA += 3
    # kot
    elif handWonA == 7 and handWonB == 0 and (trumper == 'user' or trumper == 'player3'):
        winsA += 2
    # just a normal win
    elif handWonA == 7:
        winsA += 1
    # Hakem kot
    elif handWonB == 7 and handWonA == 0 and (trumper == 'user' or trumper == 'player3'):
        winsB += 3
    # kot
    elif handWonB == 7 and handWonA == 0 and (trumper == 'player2' or trumper == 'player4'):
        winsB += 2
    # just a normal win
    else:
        winsB += 1
    return winsA, winsB


# # The algorithm
while winsA < 7 and winsB < 7   :
    j, t, trumper = WhoIsTrumper(j, t, trumper)
    handWonA = 0
    handWonB = 0
    deckCopy = deck[:]
    ShuffleAndSpread()
    userHand = SortHand(userHand)
    player2Hand = SortHand(player2Hand)
    player3Hand = SortHand(player3Hand)
    player4Hand = SortHand(player4Hand)
    ShowHand(userHand[:5])
    trump = WhatIsTrump(trumper)

    while handWonA < 7 and handWonB < 7:
        ShowHand(userHand)
        groundCards = []

        for i in range(4):
            turn = WhoseTurn(t)
            if turn == 'user':
                AskWhatToPlay(userHand, groundCards)
                sleep(1)
                if i == 3:
                    break
            elif turn == 'player2':
                WhatCardToPlay(player2Hand, groundCards, "player2")
                sleep(1)
                if i == 3:
                    break
            elif turn == 'player3':
                WhatCardToPlay(player3Hand, groundCards, "player3")
                sleep(1)
                if i == 3:
                    break
            else:
                WhatCardToPlay(player4Hand, groundCards, "player4")
                sleep(1)
                if i == 3:
                    break
            t = (t + 1) % 4
        t = WhoWins(t,groundCards, trump)
        handWonA, handWonB = CountHandWins(t, handWonA, handWonB)
        print(f'Number of hands A = {handWonA} , B = {handWonB}\n')
        sleep(2)
        goneCards += groundCards
    winsA, winsB = CountWins(winsA, winsB)
    print(f'Number of wins A = {winsA} , B = {winsB}\n\n')

if winsA == 7:
    print('Congratulation your team won!!')
else:
    print('Game Over')