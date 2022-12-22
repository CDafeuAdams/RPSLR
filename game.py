from human import Human
from player import Player
from ai import Ai

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
        while self.player1.wins < 2 and self.player2.wins < 2:
            self.player1