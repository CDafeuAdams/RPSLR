from player import Player

class Human(Player):
    def __init__(self,name):
        super().__init__(name)
        # THESE ARE THE VALUES IT GETS FROM INHARETANCE 
        self.list_of_gestures = ['Rock','Paper','Scissors','Lizard','Spock']
        self.chosen_gesture = ""
        self.wins = 0
        self.name = name

    def select_gesture(self):
        user_choice = int(input("press 0 for rock, 1 for paper, 2 for scissors, 3 for Lizard, 4 for Spock"))
        self.chosen_gesture = self.list_of_gestures[user_choice]
        print(f'{self.name} picked {self.chosen_gesture}')
