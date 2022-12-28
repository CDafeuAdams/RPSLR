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

    def game_confirmation (self,list_of_random_gestures):
        self.random_list = list_of_random_gestures

    def game_round(self):
        while self.player1.wins < 2 and self.player2.wins < 2:
            print(f"\nYou will only win 2 out of 3 tries! Player1: {self.player1.chosen_gesture} Player2: {self.player2.chosen_gesture}")
        if Ai(Player).list_of_gestures == Player.list_of_gestures:
            result = 'Draw!'
        elif(Human.choose_gesture, Ai.choose_gesture) in self.win_lose_pairs:
            result = 'You Won!'
        else:
            result = 'You Lose!'

    print(Player.list_of_gestures)
    print(Ai.list_of_gestures)
    print(run_game)

    play_again = input('Play again? (Y/N):')
    if play_again.lower() == 'n':
        pass

random()

