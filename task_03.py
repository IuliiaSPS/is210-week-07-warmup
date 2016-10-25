#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_03"""


import decimal


def lexicographics(to_analyze):
    """This function does some culculations of strings.

    Args:
        to_analyze(str): Just a random string written in sepatate lines.
    Returns:
        int: max_words return umber of words in the longest line, min_words retu
        rn number of words in the shortest line, avg_words return avarage number
        of words per text.
    Examples:
        >>>lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal(4))
        >>>lexicographics('''This is my first line.
        This is second.
        This is the longest third line.''')
        (6, 3, Decimal('4.666666666666666666666666667'))
    """
    words_nums = []
    raws = to_analyze.split('\n')
    for pos, _ in enumerate(raws):
        words = raws[pos].split(' ')
        words_nums.append(len(words))
    max_words = max(words_nums)
    min_words = min(words_nums)
    avg_words = decimal.Decimal(sum(words_nums)) / len(words_nums)
    return (max_words, min_words, avg_words)
