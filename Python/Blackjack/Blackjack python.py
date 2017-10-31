##This is just a quick test of python knowledge that I did after a 1-day course.
##It simulates a blackjack game playing against the dealer.  It does not allow
##the user to split if they get a pair currently.

import math
from random import randint
import time
status = 'playing'

while status == 'playing':
    time.sleep(0.25)
    card_deck=['Ad','Ah','As','Ac','2d','2h','2s','2c',
               '3d','3h','3s','3c','4d','4h','4s','4c',
               '5d','5h','5s','5c','6d','6h','6s','6c',
               '7d','7h','7s','7c','8d','8h','8s','8c',
               '9d','9h','9s','9c','10d','10h','10s','10c',
               'Jd','Jh','Js','Jc','Qd','Qh','Qs','Qc',
               'Kd','Kh','Ks','Kc']

    #-------------------------------------------
    #Defining functions

    #Adding a function that counts the total in the user's hand
    def user_total_hand(user_hand):
        i=0
        total=0
        total_list=[]
        for cards in user_hand:
            card_len=len(user_hand[i])
            if card_len==3: #helps if the card is a 10, having a string length of 3
                card=10
            else:
                card=user_hand[i][:1]
            #if card is an A, J, Q, or K:
            if card == 'J' or card == 'Q' or card == 'K':
                card = 10
            elif card == 'A':
                card = 11
            else:
                card = int(card)
            total_list.insert(0,card)
            total = sum(total_list)
            if total > 21:
                ace = 11 in total_list
                if ace == True:
                    place = total_list.index(11)
                    total_list[place] = 1
                total = sum(total_list)
                if total > 21:
                    ace = 11 in total_list
                    if ace == True:
                        place = total_list.index(11)
                        total_list[place] = 1
                    total = sum(total_list)
                    if total > 21:
                        ace = 11 in total_list
                        if ace == True:
                            place = total_list.index(11)
                            total_list[place] = 1
                        total = sum(total_list)
                        if total > 21:
                            ace = 11 in total_list
                            if ace == True:
                                place = total_list.index(11)
                                total_list[place] = 1
                            total = sum(total_list)
            i = i+1
        return total

    #Adding a function that hits a user's hand (adds a card to the user's hand)
    def user_hit(user_hand):
        uA = card_deck[randint(0,len(card_deck)-1)]
        card_deck.remove(uA)
        user_hand.insert(0,uA)

    #Adding a function that counts the total in the dealer's hand
    def dealer_total_hand(dealer_hand):
        i=0
        total=0
        total_list=[]
        for cards in dealer_hand:
            card_len=len(dealer_hand[i])
            if card_len==3: #helps if the card is a 10, having a string length of 3
                card=10
            else:
                card=dealer_hand[i][:1]
            #if card is an A, J, Q, or K:
            if card == 'J' or card == 'Q' or card == 'K':
                card = 10
            elif card == 'A':
                card = 11
            else:
                card = int(card)
            total_list.insert(0,card)
            total = sum(total_list)
            if total > 21:
                ace = 11 in total_list
                if ace == True:
                    place = total_list.index(11)
                    total_list[place] = 1
                total = sum(total_list)
                if total > 21:
                    ace = 11 in total_list
                    if ace == True:
                        place = total_list.index(11)
                        total_list[place] = 1
                    total = sum(total_list)
                    if total > 21:
                        ace = 11 in total_list
                        if ace == True:
                            place = total_list.index(11)
                            total_list[place] = 1
                        total = sum(total_list)
                        if total > 21:
                            ace = 11 in total_list
                            if ace == True:
                                place = total_list.index(11)
                                total_list[place] = 1
                            total = sum(total_list)
            i = i+1
        return total

    #Adding a function that hits a dealer's hand (adds a card to the user's hand)
    def dealer_hit(dealer_hand):
        dA = card_deck[randint(0,len(card_deck)-1)]
        card_deck.remove(dA)
        dealer_hand.insert(0,dA)

    #-------------------------------------------

    #Starting the game - if they do not type in "deal", it will not continue
    Action=raw_input("Type \"Deal\" to start a game: ").lower()
    time.sleep(0.25)
    while Action <> 'deal':
        print("")
        Action=raw_input("Type \"Deal\" to start a game: ").lower()
        time.sleep(0.25)

    #After they have typed deal, this sets the user's first hand
    #and the dealer's first hand (hiding one of the dealers cards).
    #This also removes the cards from the deck as they are drawn.
    #For right now, there is not going to be an option to split.
    print("")
    print("d=diamonds, s=spades, c=clubs, h=hearts")
    print("")
    uA = card_deck[randint(0,len(card_deck)-1)]
    card_deck.remove(uA)
    uB = card_deck[randint(0,len(card_deck)-1)]
    card_deck.remove(uB)
    user_hand=[uA,uB]

    dA = card_deck[randint(0,len(card_deck)-1)]
    card_deck.remove(dA)
    dB = card_deck[randint(0,len(card_deck)-1)]
    card_deck.remove(dB)
    dealer_hand=[dA,dB]
    user_hand_sentence = user_hand[0] + ", " + user_hand[1]
    dealer_hand_sentence = dealer_hand[0] + ", " + dealer_hand[1]

    print("Your cards are: " + user_hand_sentence) + " (" + str(user_total_hand(user_hand)) + ")"
    print("The Dealer's cards are: " + dealer_hand[0] + ", ?")
    print("")



    #Now that the initial hands are set, the user get's to decide whether to stay or hit
    #This will automatically end if the user busts.

    Action=raw_input("Type \"Hit\" to receive a card or \"Stay\" to keep your cards: ").lower()
    time.sleep(0.25)
    user_status = 'good' #means the user has not busted yet
    dealer_status = 'good' #means the dealer has not busted yet
    while Action <> 'stay': #will loop through this until the user selects stay or they bust
        while Action <> 'hit':
            print("")
            Action=raw_input("Please type \"Hit\" to receive a card or \"Stay\" to keep your cards: ").lower()
        print("")
        user_hit(user_hand)
        
        print("You received: " + user_hand[0])
        user_hand_sentence = ""
        i=0
        for cards in user_hand:
            if i==0:
                user_hand_sentence = user_hand_sentence + user_hand[i]
            else:
                user_hand_sentence = user_hand_sentence +", " + user_hand[i]
            i = i+1
        print "Your cards are: " + user_hand_sentence + " (" + str(user_total_hand(user_hand)) + ")"
        if user_total_hand(user_hand) > 21:
            user_status = 'bust'
            break
        print("")
        Action=raw_input("Type \"Hit\" to receive a card or \"Stay\" to keep your cards: ").lower()
    print("")
    time.sleep(0.25)
    if user_status == 'bust':
        print("You busted! Let's see how the dealer does...")
        print("")
    else:
        print("Your cards are: " + user_hand_sentence + " for a total of " + str(user_total_hand(user_hand)) + ".  Let's see how the dealer does...")
        print("")
    #This will see how the dealer does.  By dealer rules the dealer will stay when they are at 16 or above
    time.sleep(2)
    print("The dealer's cards are: " + dealer_hand_sentence) + " (" + str(dealer_total_hand(dealer_hand)) + ")"
    time.sleep(2)
    print("")

    while dealer_total_hand(dealer_hand) <16: #hits the dealer
        dealer_hit(dealer_hand)
        print("The dealer hits and receives: " + dealer_hand[0])
        dealer_hand_sentence = ""
        i=0
        for cards in dealer_hand:
            if i==0:
                dealer_hand_sentence = dealer_hand_sentence + dealer_hand[i]
            else:
                dealer_hand_sentence = dealer_hand_sentence +", " + dealer_hand[i]
            i = i+1
        print("The dealer's cards are: " + dealer_hand_sentence + " (" + str(dealer_total_hand(dealer_hand)) + ")")
        print("")
        time.sleep(2)
        if dealer_total_hand(dealer_hand) > 21:
            dealer_status = 'bust'
            break
    if dealer_status == 'bust':
        print("Dealer busted!")
        print("")
    else:
        print("The dealer stays.  Their final hand is: " + dealer_hand_sentence) + " (" + str(dealer_total_hand(dealer_hand)) + ")"
    print("--------------------------")
    print("")
    time.sleep(2)

    #Final presentation of who wins!
    ut = user_total_hand(user_hand)
    dt = dealer_total_hand(dealer_hand)
    if user_status == 'good' and dealer_status == 'bust':#You win
        game_status = "You Win!"
        print("Your cards: " + user_hand_sentence + " (" + str(ut) + ")")
        print("Dealer's cards: " + dealer_hand_sentence + " (Bust!)")
    elif user_status == 'bust' and dealer_status == 'good':#Dealer win
        game_status = "You lose."
        print("Your cards: " + user_hand_sentence + " (Bust!)")
        print("Dealer's cards: " + dealer_hand_sentence + " (" + str(dt) + ")")
    elif user_status == 'bust' and dealer_status == 'bust':#Both Lose
        game_status = "Tie - you both busted!"
        print("Your cards: " + user_hand_sentence + " (Bust!)")
        print("Dealer's cards: " + dealer_hand_sentence + " (Bust!)")
    else:
        print("Your cards: " + user_hand_sentence + " (" + str(ut) + ")")
        print("Dealer's cards: " + dealer_hand_sentence + " (" + str(dt) + ")")
        if ut > dt:
            game_status = "You Win!"
        elif dt > ut:
            game_status = "You Lose."
        else:
            game_status = "You Tied!"

    time.sleep(1)
    print(game_status)
    print("")
    status=raw_input("Type \"Replay\" to play again or anything else to end the session: ").lower()
    if status == 'replay':
        status = 'playing'
