from player import Player

class Ai(Player):
    def __init__(self,name):
        super().__init__(name)
        
    def choose_gesture(self, win_lose_pairs):
        self.list_of_gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.win_lose_pairs = [('Scissors', 'Paper'), ('Paper', 'Rock'), ('Rock','Lizard'), ('Lizard', 'Spock'), ('Spock', 'Scissors'), ('Lizard', 'Paper'), ('Paper','Spock'),('Spock', 'Rock'),('Rock', 'Scissors')]

    def list_index(self): 
        self.list_index = 0,1,2,3,4
        self.chosen_gesture = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        pass

    print('Please choose one of the options below:')
    print('-> 0 for Rock\n -> 1 for Paper\n -> 2 for Scissors\n -> 3 for Lizard\n -> 4 for Spock')

    player_input = int(input('Your choice (0-4):'))

