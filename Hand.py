# Name: Hand class for OO Poker Game
# Programmer: Shaian
# Date: Nov 22, 2022
# Description: Hand class for OO Poker Game. Contains game mechanics 
#              for a hand in poker. Contains the cards of a player, 
#              and is able to add, show, and swap cards, and determine 
#              the type of hand.

class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.card_values = []
        self.card_suits = set ()
        self.hand_evals = [0, 0, "", ""]

    # Adds a card to the hand.
    def add_card (self, card):
        self.cards.append (card)

    # Prints the hand, with or without the order.
    def show_cards (self, card_nums = False):
        # If the card_nums parameter is True, 
        # the cards will be printed with their place in the hand.
        if card_nums:
            for i in range (0, len (self.cards)):
                print (" " * 17 + f"{i + 1}: {self.cards [i].get_name ()}")

        # Otherwise, just print the cards normally. 
        else:
            for card in self.cards:
                print (" " * ((50 - len (card.get_name ())) // 2) 
                       + card.get_name ())

    # Swap cards in the hand with a new card.
    def swap_card (self, card, new_card):
        self.cards = [new_card if x == card else x for x in self.cards]
    
    # Check the highest card in the hand. Used for some tiebreakers.
    def check_highest_card (self):
        highest_card = 0

        # For each card in the hand, check if it's higher 
        # than the current highest card.
        for card in self.cards:
            if (card.get_value () > highest_card):
                highest_card = card.get_value ()

        return highest_card

    # Check for a four of a kind, full house, three of a kind, 
    # two pairs, or a pair.
    def check_kind (self):
        # Initialize variables
        unique_cards = set ()
        counts = [] 
        tmp_count = 0
        kind_type = ""
        highest_card = 0

        # For each card in the hand, add to a set.
        for card in self.card_values:
            unique_cards.add (card)

        # Sort the set from least to greatest.
        sorted (unique_cards, reverse = True)

        # For each unique card, count how many times it appears in the hand.
        for i in (unique_cards.copy ()):
            tmp_count = self.card_values.count (i)
            counts.append (tmp_count)
            unique_cards.remove (i)

            # If the count is greater than 1, store it as the highest card.
            # This is used for tiebreakers.
            if (tmp_count > 1):
                highest_card = i
        
        # Determine the type of kind in the hand.
        if (4 in counts):
            kind_type = "four_of_a_kind"
        
        elif (3 in counts):
            # If there is a three of a kind, check if there is also a pair.
            if (2 in counts):
                kind_type = "full_house"
            else:
                kind_type = "three_of_a_kind"
        
        elif (2 in counts):
            # If there is a pair, check if there are 2 pairs.
            if (counts.count (2) == 2):
                kind_type = "two_pairs"
            else:
                kind_type = "pair"

        return kind_type, highest_card

    # Evaluate the hand and return the type of hand.
    def evaluate_hand_type (self):
        tier = 0
        hand_type_names = ["straight flush", "four of a kind", "full house",
                           "flush", "straight", "three of a kind", 
                           "two pairs", "pair", "high card"]
        highest_card_name = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
                             "10", "Jack", "Queen", "King"]
        i = 0

        # Store values of the cards in the hand and sort them.
        self.card_values = [card.get_value () for card in self.cards]
        self.card_values.sort ()

        # Store the suits of the cards in a set to check for flushes.
        self.card_suits = {card.get_suit () for card in self.cards}

        # Determine highest card in the hand.
        highest_rank_card = self.check_highest_card ()

        # Evaluate if the hand contains a four of a kind, full house,
        # three of a kind, two pairs, or a pair.
        kind, kind_highest_card = self.check_kind ()

        # General format:
        # Type = [if it is the type, the highest card in the hand]

        # Store the types of "kinds" found in the hand.
        four_of_a_kind = [(kind == "four_of_a_kind"), kind_highest_card]
        full_house = [(kind == "full_house"), kind_highest_card]
        three_of_a_kind = [(kind == "three_of_a_kind"), kind_highest_card]
        two_pairs = [(kind == "two_pairs"), kind_highest_card]
        pair = [(kind == "pair"), kind_highest_card]

        # Check for a flush, straight, and then straight flush.
        flush = [(len (self.card_suits) == 1), highest_rank_card]

        # If the hand is a straight by comparing the difference between
        # the highest and lowest card. 
        # A difference of 4 means it is a straight.
        straight = [(self.card_values [-1] - self.card_values [0]) == 4,
                     highest_rank_card]
        straight[0] = not((four_of_a_kind [0]) or (full_house [0])
                          or (three_of_a_kind [0]) or (two_pairs [0])
                          or (pair[0])) and (straight [0])

        straight_flush = [flush [0] and straight [0], highest_rank_card]

        # High card is the default hand type.
        high_card = [(True), highest_rank_card]

        # Store all evaluated hand types in a list.
        hand_evaluations = [straight_flush, four_of_a_kind, full_house, flush,
                            straight, three_of_a_kind, two_pairs, pair, 
                            high_card]
        
        # Determine the strongest type in the hand and store it as the "tier"
        # Higher tiers are stronger hands.
        while (i < len (hand_evaluations)):
            if hand_evaluations [i] [0]:
                tier = 9 - i
                self.hand_evals = [tier, hand_evaluations[i] [1], 
                                   hand_type_names[i], 
                                   highest_card_name [hand_evaluations[i] [1]
                                                                         - 1]]
                i = len (hand_evaluations)
            i += 1

    # Return the evaluation of the hand.
    def get_hand_evaluation (self):
        return self.hand_evals 