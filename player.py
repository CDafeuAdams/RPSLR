class Player:

    def __init__(self, name, win_lose_pairs,result):
        self.list_of_gestures = []
        self.chosen_gesture = ""
        self.wins = 0
        self.name = name
        self.win_lose_pairs = win_lose_pairs [('Scissors', 'Paper'), ('Paper', 'Rock'), ('Rock','Lizard'), ('Lizard', 'Spock'), ('Spock', 'Scissors'), ('Lizard', 'Paper'), ('Paper','Spock'),('Spock', 'Rock'),('Rock', 'Scissors')]
        self.result = result

    def list_index(self): 
        self.list_index = 0,1,2,3,4
        self.chosen_gesture = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        pass

    print('Please choose one of the options below:')
    print('-> 0 for Rock\n -> 1 for Paper\n -> 2 for Scissors\n -> 3 for Lizard\n -> 4 for Spock')

    player_input = int(input('Your choice (0-4):'))



