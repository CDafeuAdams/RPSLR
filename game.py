from human import Human
from player import Player
from ai import Ai
import random

class Game:

    def __init__ (self):
        self.player1 = Human()
        self.player2 = Ai()

    def run_game(self):
        self.display_welcome()
        self.game_rules()
        pass

    def display_welcome(self):
        print("Welcome to Rock,Paper,Scissors,Lizard,Spock")
        pass

    def game_rules(self):
        print(f"\nRock crushes Scissors \nRock crushes Scissors \n Scissors cuts Paper \n Paper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock \n Spock smashes Scissors \n Scissors decapitates Lizard \n Lizard eats Paper \n Paper disproves Spock \n Spock vaporizes Rock")
        pass


    def game_round(self):
        if Ai(Player).list_of_chosen_gestures == Human.list_of_chosen_gestures:
            result = 'Draw!'
        elif(Human.choose_gesture, Ai.choose_gesture) in self.win_lose_pairs:
            result = 'You Won!'
        else:
            result = 'You Lose!'

    print(Human.chosen_gestures)
    print('Ai:', Human)
    print('Result:', result)

