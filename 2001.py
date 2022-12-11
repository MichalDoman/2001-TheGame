from flask import Flask, request
from random import randint

app = Flask(__name__)


@app.route('/2001', methods=['GET', 'POST'])
def main():
    html_init = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>2001 - The Game</title>
</head>
<body>
<h1>Welcome to 2001!</h1>
<h2>First one to reach the score of 2001 wins!</h2>
<form action="" method="POST">
    <input type="hidden" name="player_score" value="0">
    <input type="hidden" name="computer_score" value="0">
    <input type="submit" value="Play!">
</form>
</body>
</html>'''
    html_main = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>2001 - The Game</title>
</head>
<body>
<h2>Computer score: {computer_score}</h2>
<h2>Your score: {player_score}</h2>
<form action="" method="POST">
    <input type="hidden" name="player_score" value="{player_score}">
    <input type="hidden" name="computer_score" value="{computer_score}">
    <input type="submit" value="Play!">
</form>
</body>
</html>'''
    if request.method == 'GET':
        return html_init
    elif request.method == 'POST':
        computer_score = int(request.form['computer_score'])
        player_score = int(request.form['player_score'])
        return html_main.format(player_score=player_score,  computer_score=computer_score)
if __name__ == '__main__':
    app.run(debug=True)
