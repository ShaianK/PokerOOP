# Name: Hand class for OO Poker Game
# Programmer: Shaian
# Date: Nov 25, 2022
# Description: Main program for OO Poker Game. Manages starting, restarting, 
#              and ending the game. 

from Game import *

def main():
    run_game = True

    while run_game:
        # Get the player names.
        player_one = input ("Enter player one's name: ")
        player_two = input ("Enter player two's name: ")

        print()

        # Create game object with player names and start game sequence.
        game = Game ([player_one, player_two])
        game.deal ()
        game.swap_cards_process (player_one)
        game.evaluate_game ()
    
        # Ask the user if they want to play again.
        run_game = input ("\nWould you like to play again? (y/n): ").lower ()
        
        if (run_game in ["y", "yes"]):
            run_game = True
        else:
            run_game = False

main()