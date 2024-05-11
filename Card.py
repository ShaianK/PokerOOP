# Name       : Standard Cards
# Programmer : 
# Date       : Mar 30 2022
# Description: Contains Card classes
# History    : Mar 31 2022 Changed variable names to card_ref in a few places
#              Replaced raise with print()
#              Rewrite test main to properly use OO techniques
#              Nov 21 2022 Separated classes


class Card():

    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.card_name = rank + ' of ' + suit #Build and store name
        self.value = value


    def get_name(self):
        return self.card_name

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank


#Test code
if (__name__ == "__main__"):
    # Main code to test the Card and Deck classes
    print ("Test Card class")
    test_card = Card("Ace", "Diamonds", 1)
    print (test_card.get_name () )
    print (test_card.get_value () )
    print (test_card.get_suit () )
    print (test_card.get_rank () )

    print ("\nTest Deck class")
    
