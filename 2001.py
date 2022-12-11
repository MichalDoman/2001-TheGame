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
    <input type="hidden" name="throw_1" value="d6">
    <input type="hidden" name="throw_2" value="d6">
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
<h3>Choose types of dice that you want to use: </h3>
<form action="" method="POST">
    <p>Possible dice types: {dice_types_str}</p>
    <label>Throw No.1: <input type="text" name=throw_1></label>
    <label>Throw No.2: <input type="text" name=throw_2></label>
    <input type="hidden" name="player_score" value="{player_score}">
    <input type="hidden" name="computer_score" value="{computer_score}">
    <input type="submit" value="Roll">
</form>
</body>
</html>'''
    if request.method == 'GET':
        return html_init
    elif request.method == 'POST':
        dice_types = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
        dice_types_str = ', '.join(dice_types)
        computer_score = int(request.form['computer_score'])
        player_score = int(request.form['player_score'])
        throw_1 = request.form['throw_1']
        throw_2 = request.form['throw_2']
        if throw_1.upper() not in dice_types or throw_2.upper() not in dice_types:
            return html_main.format(player_score=player_score, computer_score=computer_score,
                                    dice_types_str=dice_types_str) + 'This is not a valid code!'

        return html_main.format(player_score=player_score, computer_score=computer_score, dice_types_str=dice_types_str)


if __name__ == '__main__':
    app.run(debug=True)
