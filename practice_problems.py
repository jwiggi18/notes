#!/usr/bin/env python3

GAME_STATS = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


def print_game_stats(games_won):
    """Loop through games_won's dict (key, value) pairs (dict.items)
       printing (print, not return) how many games each person has won,
       pluralize 'game' based on number.

       Expected output (ignore the docstring's indentation):

       sara has won 0 games
       bob has won 1 game
       tim has won 5 games
       julian has won 3 games
       jim has won 1 game

       (Note that as of Python 3.7 - which we're using atm - dict insert order
       is retained so no sorting is required for this Bite.)
    """
    for k, v in GAME_STATS.items():
        if v >= 2 or v == 0:
            print('{} has won {} games'.format(k, str(v)))
        else:
            print('{} has won {} game'.format(k, str(v)))


MESSAGE = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

print(MESSAGE)

s_MESSAGE = MESSAGE.split('/n')

print(s_MESSAGE)

js_MESSAGE = '|'.join(s_MESSAGE)

print(js_MESSAGE)