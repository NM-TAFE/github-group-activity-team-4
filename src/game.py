from app import board


class Game:

    def __init__(self):
        self.board = [' '] * 9
        self.players = None


    def check_winner(self):
        # Winning combinations
        return None

    def check_draw(self):
        return ' ' not in board

    def play(self, cell):
        ...
