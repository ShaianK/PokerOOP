# Name: Game class for OO Poker Game
# Programmer: Shaian
# Date: Nov 22, 2022
# Description: Game class for OO Poker Game. Contains the game logic and 
#              manages the game. Deals cards, swaps cards, and determines
#              the winner (or tie).

from Hand import *
from Deck import *
import time

class Game:
    def __init__ (self, players):
        # Create deck, list of players, and their hands.
        self.deck = Deck ()
        self.players = players
        self.hands = []

        # Shuffle the deck
        self.deck.shuffle ()

        # Create a hand for each player.
        for i in players:
            self.hands.append (Hand(i))

    # Function that deals the cards to each player.
    def deal (self):
        # Deal 10 cards in total.
        for i in range (10):
            # Deal 5 to player one.
            if (i % 2 == 0):
                self.hands [0].add_card (self.deck.get_card ())

            # Deal 5 to player two.
            else:
                self.hands [1].add_card (self.deck.get_card ())

            # Pause for 0.5 seconds between each card and display the 
            # current hands.
            time.sleep (0.5)
            print ("\n*************************************************")
            print ("\n" + " " * ((50 - len (f"{self.players [0]}'s Hand:"))
                                                                      // 2)
                   + f"{self.players [0]}'s Hand:")
            self.hands [0].show_cards ()

            print ("\n" + " " * ((50 - len (f"{self.players [1]}'s Hand:")) 
                                                                      // 2)
                   + f"{self.players [1]}'s Hand:")
            self.hands [1].show_cards ()
            print ("\n*************************************************")

        print ("\nDealing is done!\n")

    # Function to allow player one to swap 1 or 2 of their cards. 
    def swap_cards_process (self, player):
        # Ask player one if they want to swap any cards.
        choice = input (f"{player} would you like to swap 1" +
                        " or 2 cards? (y/n): ")

        # If they say yes, ask them which cards they want to swap.
        if (choice.lower () in ["y", 'yes']):
            print ()
            self.hands [0].show_cards (True)
            valid_input = False

            # Loop until the player enters number within range 
            # or enters nothing.
            while (not valid_input):
                print ("\nEnter the number of the card(s) you would like"
                       + " to swap")
                print ("Leave blank if you don't want to swap any cards:")
                card_nums = input ().split ()

                for i in card_nums:
                    if ((int (i) > 0) and (int (i) < 6)):
                        valid_input = True
                    else:
                        valid_input = False

                if (card_nums == []):
                    valid_input = True

            # If they entered the same card twice, remove the second entry.
            if ((len (card_nums) == 2) and (card_nums [0] == card_nums [1])):
                card_nums.pop ()

            # For each selected card, remove it from the hand 
            # and add a new card.
            for i in card_nums:
                # Return the card to the deck.
                self.deck.return_card (self.hands [0].cards [int (i) - 1])

                # Call the swap_card method in Hand.py to swap the card 
                # with a new one.
                self.hands [0].swap_card (self.hands [0].cards[int (i) - 1],
                                          self.deck.get_card ())

            # Show player one their new hand.
            print (f"\n{player}, your new hand is: \n")
            self.hands [0].show_cards ()
            
            time.sleep (2)
            print()
    
    # Game ending sequence, determine winner and print results.
    def evaluate_game (self):
        # Get the hand evaluation for each player.
        self.hands [0].evaluate_hand_type ()
        self.hands [1].evaluate_hand_type ()

        hand_one_eval = self.hands [0].get_hand_evaluation ()
        hand_two_eval = self.hands [1].get_hand_evaluation ()

        print ("*************************************************")

        # Print final hands of each player.
        print ("                    Final hands:")
        print ("\n" + " " * ((50 - len (f"{self.players [0]}'s Hand:")) // 2)
               + f"{self.players [0]}'s Hand:")
        self.hands [0].show_cards()

        print ("\n" + " " * ((50 - len (f"{self.players [1]}'s Hand:")) // 2)
               + f"{self.players [1]}'s Hand:")
        self.hands [1].show_cards()

        print ("\n*************************************************")

        print (f"{self.players[0]} has a {hand_one_eval [2]}" 
               + " and their tie breaker card is a " + f"{hand_one_eval [3]}")

        print (f"{self.players[1]} has a {hand_two_eval [2]}" 
               + " and their tie breaker card is a " + f"{hand_two_eval [3]}")

        print ()
        
        # Dramatic pause.
        time.sleep (2)

        # Compare the hand types to see who wins.
        if (hand_one_eval [0] > hand_two_eval [0]):
            print(f"{self.players [0]} wins!")

        elif (hand_one_eval [0] < hand_two_eval [0]):
            print(f"{self.players [1]} wins!")

        # If the hands are the same type, compare the highest card.
        else:
            print ("It's a tie! Comparing highest cards...")
            time.sleep (1)

            if (hand_one_eval [1] > hand_two_eval [1]):
                print (f"{self.players [0]} wins!")
            
            elif (hand_one_eval [1] < hand_two_eval [1]):
                print (f"{self.players [1]} wins!")

            # If the highest card is the same, it's a tie.
            else:
                print ("Tie!")
        
        print ("Game over!")
        print ("*************************************************")