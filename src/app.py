from flask import Flask, render_template, request, redirect, url_for
from game import Game

class App(Flask):
    """
    Flask application class to handle the routes, modified slightly to include the game object
    """
    def __init__(self):
        super().__init__(__name__)
        self.game = Game()

app = App()

@app.route('/')
def index():
    """
    Handle the index route and render the board
    """
    winner = app.game.check_winner()
    draw = app.game.check_draw()
    return render_template('index.html', board=app.game.board, current_player=app.game.current_player, winner=winner, draw=draw)

app.route('/play/<int:cell>')(app.game.play)
app.route('/reset')(app.game.reset)