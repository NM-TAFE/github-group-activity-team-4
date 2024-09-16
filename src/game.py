from flask import Flask, render_template, request, redirect, url_for

class Game:

    def __init__(self, board=[' ']* 9, current_player='X'):
        self.board = board
        self.current_player = current_player

    def check_winner(self):
        # Winning combinations
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
                return self.board[a]
            return None


    def check_draw(self):
        return ' ' not in self.board

    def play(self, cell):
        # breakpoint()
        if self.board[cell] == ' ':
            self.board[cell] = self.current_player
            if not self.check_winner():
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        return redirect(url_for('index'))

    def reset(self):
        self.current_player = 'X'
        self.board = [' ']* 9
        return redirect(url_for('index'))