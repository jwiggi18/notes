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


def split_in_columns(message=MESSAGE):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output string"""
    lines = message.split('\n')
    return '|'.join(lines)


TEXT = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""

#had hell with this one - 'return results` had to be a return of the first for loop`
def slice_and_dice(text: str = TEXT) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    #iterate over the lines of the text split by line
    results = []
    for line in text.splitlines():
        #strip whitespace from each line
        clean = line.strip()
        for line in clean.splitlines():
            #check if the first character is lowercase,
            if line[0].islower():
                #split by word, extract the last word
                lw = line.split().pop(-1)
                #remove the last character if it is a period or exclaimation point
                lws = lw.strip('.!')
                #add the last word to the results list
                results.append(lws)
    return results

#other way to do it - NOT MY WORK

def slice_and_dice(text: str = TEXT) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    results = []
    for line in text.strip().split("\n"):
        if line.lstrip()[0].islower() == True:
            results.append(line.split()[-1].strip(". !"))
    return results


def slice_and_dice(text: str = text) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    results = []
    for raw_line in text.strip().splitlines():
        if (line := raw_line.lstrip())[0] in ascii_lowercase:
            results.append(line.split()[-1].rstrip('.!'))
    return results


"""If you use a single list comprehension, the results variable isn't really needed 
because you can just return the resulting list. This solution is harder to read if you 
haven't got your head around list comprehensions [they still make my head hurt a bit] but 
splitting the list comprehension over three lines does help to make things clearer. 
The first line is making the selection of the word and stripping off the unwanted "." or "!" where applicable. 
The second line does what a for loop would do i.e. selects a line from our text. 
The third line is the condition that decides whether the word is added to the list, 
which depends on whether the line of text starts with a lowercase ASCII character or not. 
I am not sure whether this is good practice or not. It is definitely compact, but readability is sacrificed."""


def slice_and_dice(text: str = text) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    return [line.split()[-1].rstrip(".!")
            for line in text.strip().split('\n')
            if line.lstrip()[0] in ascii_lowercase]
