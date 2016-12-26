"""
Strategy:
    in every step in the game:
        1.  Call each predicate in condition_for_bot on each bot and add it to a list if True.
        2.  Select the set of actions (that doesn't conflict) that produce the greatest score combine.
        3.  Perform the selecting actions.
"""

from conditions import condition_for_bot

NUM_OF_BOTS = 4


def act(game, instructions):
    pass


def calculate(inp):
    mats = [
#content
    ]
    pass


def parse(game):
    pass


def do_turn(game):

    act(game, calculate(parse(game)))

    true_condition = [[] for _ in range(NUM_OF_BOTS)]

    for i in range(len(condition_for_bot)):
        for bot_index in range(NUM_OF_BOTS):

            if condition_for_bot[i](game, bot_index):
                true_condition[bot_index].append(condition_for_bot[i])

                # TODO: Calculate the set of actions (for every bot) that gives the highest total score.
                # TODO: Check that actions doesn't collide.
