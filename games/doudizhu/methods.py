# -*- coding: utf-8 -*-
"""for formatting"""
from core import Card


def get_doudizhu_index(card: Card):
    """Get valid index of a card in order to check type

    Return:
        string: Eg: As, 2h, Kc, BJ, CJ
    """
    index = card.rank+card.suit.lower()
    if index == 'rj':
        index = 'CJ'
    if index == 'bj':
        index = 'BJ'
    return index


def get_play_string(hand, nums):
    """Get valid string of the cards played by a player in order to check type

    Return:
        String: Eg: 2c-2d-2h-2s-BJ-CJ

    """
    play_cards = ''
    for num in nums:
        play_cards += (get_doudizhu_index(hand[num]) + '-')
    return play_cards[:-1]


def check_play_cards(nums, total):
    """Check if 'nums' contains invalid index of the card

    Args:
        nums: a list of index of cards to be played
        total: the length of current hand
    """
    try:
        for index, num in enumerate(nums):
            if int(num) >= total:
                return False
            nums[index] = int(num)
    except:
        return False
    else:
        return True