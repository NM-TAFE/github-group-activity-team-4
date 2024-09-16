<<<<<<< HEAD
import unittest
from src.game import Game
from src.app import App

class TestGame(unittest.TestCase):
    def test_winner_check():
        game = Game(board=['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '])
        assert game.check_winner() == 'X'


=======
# PLACEHOLDER SO FOLDER IS DETECTED BY GIT
>>>>>>> main
