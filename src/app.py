from game import Game
from flask import Flask, render_template, request, redirect, url_for
from game import Game

class App(Flask):
    def __init__(self):
        super().__init__(__name__)
        self.game = Game()

app = App()

@app.route('/')
def index():
<<<<<<< HEADgit
    winner = Game.check_winner()
    draw = Game.check_draw()
    return render_template('index.html', board=board, current_player=current_player, winner=winner, draw=draw)


@app.route('/play/<int:cell>')
def play(cell):
    # breakpoint()
    global current_player
    if board[cell] == ' ':
        board[cell] = current_player
        if not Game.check_winner():
            current_player = 'O' if current_player == 'X' else 'X'
    return redirect(url_for('index'))


@app.route('/reset')
def reset():
    global board, current_player
    board = [' '] * 9
    current_player = 'X'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

    winner = app.game.check_winner()
    draw = app.game.check_draw()

        return render_template('index.html', board=app.game.board, current_player=app.game.current_player, winner=winner, draw=draw)

app.route('/play/<int:cell>')(app.game.play)
app.route('/reset')(app.game.reset)

