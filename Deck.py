# Name       : Standard Deck class
# Programmer : 
# Date       : Mar 30 2022
# Description: Contains Deck class
# History    : Mar 31 2022 Changed variable names to card_ref in a few places
#              Replaced raise with print()
#              Rewrite test main to properly use OO techniques
#              Nov 12, 2022 Separated Classes


import random
from Card import *


class Deck():
    SUIT_TUPLE = ("Diamonds", "Clubs", "Hearts", "Spades")
    # Dictionary maps each card rank to a value for a standard deck
    STANDARD_DICT = {"Ace":1, "2":2, "3":3, "4":4, "5":5,
                                  "6":6, "7":7, "8": 8, "9":9, "10":10,
                                  "Jack":11, "Queen":12, "King":13}

    def __init__(self):
        self.starting_deck_list = []
        self.playing_deck_list = []
        for suit in Deck.SUIT_TUPLE:
            for rank, value in Deck.STANDARD_DICT.items():
                new_card = Card(rank, suit, value)
                self.starting_deck_list.append(new_card)

    def shuffle(self):
        # Copy the starting deck and save it in the playing deck list
        self.playing_deck_list = self.starting_deck_list.copy()
        random.shuffle(self.playing_deck_list)

    def get_card(self):
        if (len(self.playing_deck_list) == 0):
            print ("No more cards")
        # Pop one card off the deck and return it
        card_ref = self.playing_deck_list.pop()  
        return card_ref

    def return_card(self, card_ref):
        # Put a card back into the deck
        self.playing_deck_list.insert(0, card_ref)        


#Test code
if (__name__ == "__main__"):
    # Main code to test the Deck class
    print ("\nTest Deck class")
    deck_ref = Deck()

    deck_ref.shuffle()
    for i in range(52):
        card_ref = deck_ref.get_card()
        print("Name: ", card_ref.get_name(), "  Value:", card_ref.get_value())



