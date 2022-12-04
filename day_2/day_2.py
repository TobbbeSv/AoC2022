import os
import sys
from enum import Enum

ROCK_BASE_POINT = 1
PAPER_BASE_POINT = 2
SCISSOR_BASE_PONT = 3

LOOSE_POINT = 0
DRAW_POINT = 3
WIN_POINT = 6


def day_2_part_1():
    print("day 2 part 2")
    with open(os.path.join(sys.path[0], 'day_2/input.txt')) as games:
        points = 0

        for game in games:
            game_points = 0
            opponent_attack = get_attack_for_strategy(game[0])
            player_attack = get_attack_for_strategy(game[2])
            game_points += get_point_for_attack(player_attack)
            print(f"Points for attack {game_points}")
            game_points += get_match_point(opponent_attack, player_attack)
            print(f"Total points for game {game_points}")
            points += game_points

        return points


def get_attack_for_strategy(strategy):
    print(f"Strategy {strategy}")
    if strategy == "A" or strategy == "X":
        return Attack.Rock
    elif strategy == "B" or strategy == "Y":
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
    print(f"opponent attack {opponent_attack}, player attack {player_attack}")
    if player_attack == opponent_attack:
        return DRAW_POINT

    if player_attack == Attack.Rock:
        if opponent_attack == Attack.Paper:
            return LOOSE_POINT
        else:
            return WIN_POINT
    elif player_attack == Attack.Paper:
        if opponent_attack == Attack.Scissor:
            return LOOSE_POINT
        else:
            return WIN_POINT
    else:
        if opponent_attack == Attack.Rock:
            return LOOSE_POINT
        else:
            return WIN_POINT


class Attack(Enum):
    Rock = 1
    Paper = 2
    Scissor = 3
