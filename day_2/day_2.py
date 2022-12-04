import os
import sys
from enum import Enum

ROCK_BASE_POINT = 1
PAPER_BASE_POINT = 2
SCISSOR_BASE_PONT = 3

LOOSE_POINT = 0
DRAW_POINT = 3
WIN_POINT = 6

ROCK = ["A", "X"]
PAPER = ["B", "Y"]
SCISSOR = ["C", "Z"]


def day_2_part_1():
    print("day 2 part 1")
    with open(os.path.join(sys.path[0], 'day_2/input.txt')) as games:
        points = 0

        for game in games:
            opponent_attack = get_attack_for_strategy(game[0])
            player_attack = get_attack_for_strategy(game[2])
            points += get_point_for_attack(player_attack)
            points += get_match_point(opponent_attack, player_attack)

        return points


def day_2_part_2():
    print("day 2 part 2")
    with open(os.path.join(sys.path[0], 'day_2/input.txt')) as games:
        points = 0

        for game in games:
            opponent_attack = get_attack_for_strategy(game[0])
            needed_outcome = get_outcome_for_strategy(game[2])
            player_attack = get_attack_for_outcome(opponent_attack, needed_outcome)
            points += get_point_for_attack(player_attack)
            points += get_match_point(opponent_attack, player_attack)

        return points


def get_attack_for_strategy(strategy):
    if strategy in ROCK:
        return Attack.Rock
    elif strategy in PAPER:
        return Attack.Paper
    else:
        return Attack.Scissor


def get_point_for_attack(attack):
    if attack == Attack.Rock:
        return ROCK_BASE_POINT
    elif attack == Attack.Paper:
        return PAPER_BASE_POINT
    else:
        return SCISSOR_BASE_PONT


def get_match_point(opponent_attack, player_attack):
    if player_attack == opponent_attack:
        return DRAW_POINT

    if player_attack is Attack.Rock:
        if opponent_attack is Attack.Paper:
            return LOOSE_POINT
        else:
            return WIN_POINT
    elif player_attack is Attack.Paper:
        if opponent_attack is Attack.Scissor:
            return LOOSE_POINT
        else:
            return WIN_POINT
    else:
        if opponent_attack is Attack.Rock:
            return LOOSE_POINT
        else:
            return WIN_POINT


def get_outcome_for_strategy(strategy):
    if strategy == "X":
        return Outcome.LOOSE
    elif strategy == "Y":
        return Outcome.DRAW
    else:
        return Outcome.WIN


def get_attack_for_outcome(opponent_attack, needed_outcome):
    if needed_outcome is Outcome.DRAW:
        return opponent_attack
    elif opponent_attack is Attack.Rock:
        if needed_outcome is Outcome.WIN:
            return Attack.Paper
        else:
            return Attack.Scissor
    elif opponent_attack is Attack.Scissor:
        if needed_outcome is Outcome.WIN:
            return Attack.Rock
        else:
            return Attack.Paper
    elif needed_outcome is Outcome.WIN:
        return Attack.Scissor
    else:
        return Attack.Rock


class Attack(Enum):
    Rock = 1
    Paper = 2
    Scissor = 3


class Outcome(Enum):
    WIN = 1
    LOOSE = 2
    DRAW = 3
