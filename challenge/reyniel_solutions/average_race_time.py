# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import datetime
import os
from os.path import dirname, abspath

directory = dirname(dirname(abspath(__file__)))


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open(os.path.join(directory, '10k_racetimes.txt'), 'rt', encoding="utf-8") as file:
        content = file.read()
    return content


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""

    # Equivalent code
    # for line in races.splitlines():
    #   if 'Jennifer Rhines' in line:
    #     rhines_times.append(str(line).split()[0])

    return [str(line).split()[0]
            for line in get_data().splitlines() if
            'Jennifer Rhines' in line]


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total = datetime.timedelta()
    for racetime in racetimes:
        msecs = '0'
        mins, secs = str(racetime).split(':')
        if '.' in secs:
            secs, msecs = secs.split('.')

        total += datetime.timedelta(minutes=int(mins),
                                  seconds=int(secs), milliseconds=int(msecs))
    return f'{total/len(racetimes)}'[2:-5]

