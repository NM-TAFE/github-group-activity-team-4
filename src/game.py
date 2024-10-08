from flask import Flask, render_template, request, redirect, url_for

class Game:
    """
    Game class to handle the game logic, acts independently of the Flask application
    """
    def __init__(self, board=[' ']* 9, current_player='X'):
        self.board = board
        self.current_player = current_player

    def check_winner(self):
        """
        Check if there is a winner and return the winner character
        """
        # Winning combinations
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
                return self.board[a]
        return None


    def check_draw(self):
        """
        Check if the game is a draw
        """
        return ' ' not in self.board

    def play(self, cell):
        """
        Play a move in the cell if it is empty

        Args:
            cell (int): The cell in the board to play the move on
        
        Returns:
            redirect: Redirect to the index page
        """
        # breakpoint()
        if self.board[cell] == ' ':
            self.board[cell] = self.current_player
            if not self.check_winner():
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        return redirect(url_for('index'))

    def reset(self):
        """
        Reset the game to its initial state
        """
        self.current_player = 'X'
        self.board = [' ']* 9
        return redirect(url_for('index'))
