from flask import Flask, render_template, request, redirect, url_for

class Game:

    def __init__(self, board=[' ']* 9, current_player='X'):
        self.board = board
        self.current_player = current_player

    def check_winner(self):
        pass

    def check_winner(self):
    # Winning combinations
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
