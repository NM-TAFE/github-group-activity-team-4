
import unittest
from src.game import Game
from src.app import App

class TestGame(unittest.TestCase):
    def test_winner_check(self):
        game = Game(board=['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '])
        assert game.check_winner() == 'X'



