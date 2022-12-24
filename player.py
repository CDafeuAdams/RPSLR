class Player:

    def __init__(self, name, win_lose_pairs):
        self.list_of_gestures = ['Rock','Paper','Scissors','Lizard','Spock']
        # "" using quotes as a placeholder, it will hold items from out list eventually
        self.chosen_gesture = ""
        self.wins = 0
        self.name = name
        self.win_lose_pairs = [('Scissors', 'Paper'), ('Paper', 'Rock'), ('Rock','Lizard'), ('Lizard', 'Spock'), ('Spock', 'Scissors'), ('Lizard', 'Paper'), ('Paper','Spock'),('Spock', 'Rock'),('Rock', 'Scissors')]

        