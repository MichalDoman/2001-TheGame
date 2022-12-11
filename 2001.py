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
    <input type="hidden" name="turn" value="0">
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
    <input type="hidden" name="turn" value="{turn}">
    <input type="submit" value="Roll">
</form>
</body>
</html>'''
    html_end = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>2001 - The Game</title>
    </head>
    <body>
    <h1>{winner} wins!</h1>
    <h2>Computer's score: {computer_score}</h2>
    <h2>Player's score: {player_score}</h2>
    </body>
    </html>'''
    if request.method == 'GET':
        return html_init
    elif request.method == 'POST':
        # Variables:
        dice_types = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
        dice_types_str = ', '.join(dice_types)
        turn = int(request.form['turn'])
        throw_announcement = ''
        winner = ''
        is_winner = False
        computer_score = int(request.form['computer_score'])
        player_score = int(request.form['player_score'])

        # Calculates user's score:
        throw_1 = request.form['throw_1']
        throw_2 = request.form['throw_2']
        if throw_1.upper() not in dice_types or throw_2.upper() not in dice_types:
            return html_main.format(player_score=player_score, computer_score=computer_score,
                                    dice_types_str=dice_types_str, turn=turn) + 'This is not a valid code!'
        dice_1_size = int(throw_1.upper().strip('D'))
        dice_2_size = int(throw_2.upper().strip('D'))
        throw_1 = randint(1, dice_1_size)
        throw_2 = randint(1, dice_2_size)

        # Calculates computer's score:
        comp_dice_1_code = dice_types[randint(0, len(dice_types) - 1)]
        comp_dice_2_code = dice_types[randint(0, len(dice_types) - 1)]
        comp_dice_1_size = int(comp_dice_1_code.upper().strip('D'))
        comp_dice_2_size = int(comp_dice_2_code.upper().strip('D'))
        comp_throw_1 = randint(1, comp_dice_1_size)
        comp_throw_2 = randint(1, comp_dice_2_size)

        if turn > 0:
            player_score += (throw_1 + throw_2)
            computer_score += (comp_throw_1 + comp_throw_2)
            if turn > 1:
                player_score = modify_score(throw_1 + throw_2, player_score)
                computer_score = modify_score(comp_throw_1 + comp_throw_2, computer_score)
            throw_announcement = f'''\n Your throws:  {throw_1} ,  {throw_2}\n
            Computer dice types:  {comp_dice_1_code} ,  {comp_dice_2_code}\n
            Computer throws:  {comp_throw_1} ,  {comp_throw_2}'''

        if player_score >= 2001:
            winner = 'Player'
            is_winner = True
        elif computer_score >= 2001:
            winner = 'Computer'
            is_winner = True

        if is_winner:
            return html_end.format(winner=winner, player_score=player_score, computer_score=computer_score)

        turn += 1
        return html_main.format(player_score=player_score, computer_score=computer_score,
                                dice_types_str=dice_types_str, turn=turn) + throw_announcement


def modify_score(throws_outcome, total_score):
    """Calculates the modified score.

    :param throws_outcome: The amount of points granted for one turn.
    :param total_score: The total score that a player or computer has currently.
    :return: Total score, modified depending on the throws_outcome.
    """
    if throws_outcome == 7:
        total_score = int(total_score / 7)
    elif throws_outcome == 11:
        total_score = total_score * 11
    return total_score


if __name__ == '__main__':
    app.run(debug=True)
