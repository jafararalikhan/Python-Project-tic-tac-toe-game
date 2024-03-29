import random
import math

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter


    # we want to all players get to there next move given a game
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get random valid spot for our next move
        square = random.choice(game.available_moves())
        return square 

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn input move (0-8) : ')
            # we' re going to check that this is correct value by trying to cast
            # it to an integer, and if it's not, then we say it's invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if this are succesful, then yay!
            except ValueError:
                print('Invalid square Please try again.')
            return val

                