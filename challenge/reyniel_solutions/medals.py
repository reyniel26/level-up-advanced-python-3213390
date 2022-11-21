import os
from collections import namedtuple
from os.path import dirname, abspath

directory = dirname(dirname(abspath(__file__)))

with open(os.path.join(directory, 'olympics.txt'), 'rt', encoding="utf-8") as file:
    olympics = file.read()

medal = namedtuple('medal', ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender',
       'Event', 'Event_gender', 'Medal'])

# Complete this - medals is a list of medal namedtuples
# Based on the solution, they use list comprehension
# and Using Asterisks for Unpacking Iterables and Destructuring Assignments
medals = [medal(*line.split(';')) for line in olympics.splitlines()[1:]]

def get_medals(**kwargs):
    '''Return a list of medal namedtuples '''
    # And they use again the list comprehension
    return [medal
            for medal in medals
            if all(getattr(medal, key) == value
                   for key, value in kwargs.items())]
