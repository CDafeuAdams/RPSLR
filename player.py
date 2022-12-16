class Player:

    def __init__(self, name):
        self.list_of_gestures = ['Rock','Paper','Scissors','Lizard','Spock']
        # "" using quotes as a placeholder, it will hold items from out list eventually
        self.chosen_gesture = ""
        self.wins = 0
        self.name = name