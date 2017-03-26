# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 21:49:12 2017

@author: Jonatan Hadas
"""

import os

import battle_interface as b_int
import bot_analyzer.analyzer as anal
from bot_analyzer import param_dict_protocol

bots_path = os.path.join(b_int.kit_path, 'bots')


def join_param_dict_into(mat1, mat2):
    """
    Adds mat2 into mat1
    """
    for x in mat2:
        if x not in mat1:
            mat1[x] = dict(mat2[x])
        else:
            for y in mat2[x]:
                if y in mat1[x]:
                    mat1[x][y] += mat2[x][y]
                else:
                    mat1[x][y] = mat2[x][y]


def analyze_bot(name, map=''):
    """
    Take the bot named $name from $bots_path,
    inject to its code the adapter and run it against all the bots in $bots_path.
    For every game the adapter will produce characters dictionary (also known as param_dict).
    At the end of the process we will join all the dictionaries into single one.
    :param name: Bot name with its extension. The bot need to be found in $bots_path
    :param map:  Map which the games will be running on.
                 empty parameter tells the function to use the game's default map.
    :return: The complete characters matrix.
    """
    matrix = {}

    cur_bot_name = os.path.join(bots_path, name)
    new_bot_name = os.path.abspath('bots/current_experiment_bot.py')

    anal.inject_adapter(cur_bot_name, new_bot_name)

    name_m = os.path.splitext(name)[0] + '.pd'

    matrix_name = os.path.abspath(os.path.join('bots', 'param_dictionaries', name_m))

    for bot in b_int.bots():
        # run
        b_int.run(cur_bot_name, bot, map)
        # load matrix from file
        cur_matrix = param_dict_protocol.str2param_dict(anal.load(matrix_name))

        join_param_dict_into(matrix, cur_matrix)

    return matrix


if __name__ == "__main__":
    from sys import argv

    print analyze_bot(*argv[1:])