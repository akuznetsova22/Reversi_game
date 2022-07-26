scores = {'X': 20, 'O':25}
if scores['X'] == scores['O']:
    winner = 'It was a draw'
else:
    winner_score = max(scores.values())
    if scores['X'] == winner_score:
        winner = 'X'
    else:
        winner = 'O'
print(winner)