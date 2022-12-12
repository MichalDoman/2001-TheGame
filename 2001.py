from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)


@app.route('/2001', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('start.html')
    elif request.method == 'POST':
        # Variables:
        dice_types = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
        dice_types_str = ', '.join(dice_types)
        turn = int(request.form['turn'])
        throw_announcement_1 = ''
        throw_announcement_2 = ''
        throw_announcement_3 = ''
        winner = ''
        is_winner = False
        computer_score = int(request.form['computer_score'])
        player_score = int(request.form['player_score'])

        # Calculates user's score:
        throw_1 = request.form['throw_1']
        throw_2 = request.form['throw_2']
        if throw_1.upper() not in dice_types or throw_2.upper() not in dice_types:
            return render_template('game.html', player_score=player_score, computer_score=computer_score,
                                   dice_types_str=dice_types_str,
                                   turn=turn) + '<h2>These are not valid dice types!!!</h2>'
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
            throw_announcement_1 = f'Your throws: {throw_1}, {throw_2}'
            throw_announcement_2 = f'Computer dice types: {comp_dice_1_code}, {comp_dice_2_code}'
            throw_announcement_3 = f'Computer throws: {comp_throw_1}, {comp_throw_2}'


        # Checks for the winner:
        if player_score >= 2001:
            winner = 'Player'
            is_winner = True
        elif computer_score >= 2001:
            winner = 'Computer'
            is_winner = True

        if is_winner:
            return render_template('game_over.html', winner=winner, player_score=player_score, computer_score=computer_score)

        turn += 1
        return render_template('game.html', player_score=player_score, computer_score=computer_score,
                               dice_types_str=dice_types_str, turn=turn, throw_announcement_1=throw_announcement_1,
                               throw_announcement_2=throw_announcement_2, throw_announcement_3=throw_announcement_3)


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
