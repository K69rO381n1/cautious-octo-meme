"""

Write/Read parameters matrix protocol:

    Summery:
        The parameters matrix will be presented in Python's list syntax in predetermined .py file,
        under the global space-name PARAM_MATRIX.

        The conditions are python function (That return Boolean value),
        found in predetermined .py file (Default is conditions.py).
        The actions are Python functions, found in predetermined .py file (Default is actions.py).

    The matrix will address the following form:

        Explanation:
            Comb_i / Act_i should be interpreted as the i conditions Combination / Action in the matrix;
            The conditions are predicate that gets Game and int represent the game-state and bot-index,
            analyze it and return True if the bot position in the board meets the requirements.
            A combination is a set of conditions which will have to be True,
            and the remaining conditions are must to be False. For n conditions there are 2^n combinations.
            The action can be combination of several basic operations from the bots's op interface.

         | Comb_1 | Comb_2 | Comb_3 | ...
    -----+-------+-------+-------+-...
    Ac_1 | ...
    -----+-...
    Ac_2 | ...
    -----+-...
    Ac_3 | ...
    -----+-...
    ...

    The value in the I row and j column is the score for preforming the action Ac_i in case the Comb_j is True.

    Why?
    This method seems easy to write, and even more easy to read by a python coded bot.

    How to build the matrix?
    This is the step that may combine some ML techniques which I'll describe samples in the next paragraph.
    Idea_1:
        Building an analyzer extension for generic bot;

        It added to the competing bot's do_turn function, and wrap the basic operations
        so it will be able to monitor it.

        In each turn he takes the True-conditions and
        increase the value in the row of every action that took place in the move.
        At the end it normalize the values in the matrix.

        Using that method we can watch demo battles and fit matrix to each competing bot.

    Idea_2:
        Building evolutionary system that runs on the parameters matrix generated using #Idea_1,
        and by doing that finds MLE for building that best guided bot.
"""
from random import randint, choice

NUM_OF_PIRATES_IN_GROUP = 4


# ************************************************ Conditions ************************************************
def is_right_to_initial_loc(game, pirate_id):
    return game.get_my_pirate(pirate_id).location.column > game.get_my_pirate(pirate_id).initial_loc.column


def is_carrying_treasures(game, pirate_id):
    return game.get_my_pirate(pirate_id).has_treasure


def is_enemy_guarding_island(game, enemy_id):
    return game.in_range(game.get_my_pirate(0).initial_loc, game.get_enemy_pirate(enemy_id))


# Idea: add another conditions, that checks when the pirates are about to get loaded / sobered.
# Prevent the use of weapons /
def are_weapons_loaded(game, pirate_id):
    return game.get_my_pirate(pirate_id).reload_turns == 0


def is_defense_measures_available(game, pirate_id):
    return game.get_my_pirate(pirate_id).defense_reload_turns == 0


def is_sober(game, pirate_id):
    return game.get_my_pirate(pirate_id).turns_to_sober == 0


# TODO: is_poweruped? What kind of powerup?


ENEMY_IN_RANGE = [lambda game, pirate_id:
                  game.in_range(game.get_my_pirate(pirate_id), game.get_enemy_pirate(enemy_id))
                  for enemy_id in range(NUM_OF_PIRATES_IN_GROUP)]

ENEMY_ARE_CLOSING_IN = [(lambda game, pirate_id:
                         game.distance(
                             game.get_my_pirate(pirate_id).location,
                             game.get_enemy_pirate(enemy_id).location)
                         < game.get_my_pirate(0).attack_radius) for enemy_id in range(NUM_OF_PIRATES_IN_GROUP)]

conditions = [is_right_to_initial_loc, is_carrying_treasures, is_enemy_guarding_island, are_weapons_loaded,
              are_weapons_loaded, is_defense_measures_available, is_sober] + ENEMY_IN_RANGE + ENEMY_ARE_CLOSING_IN


# ************************************************ Actions ************************************************
# Available actions: sail north\east\south\west, shot enemy, defend ship & summon bermuda zone at location
def _direction_to_location(initial_loc, direction):
    coordinate_addition = {'n': (-1, 0), 's': (1, 0), 'w': (0, -1), 'e': (0, 1), '-': (0, 0)}[direction]
    return Location(initial_loc.row + coordinate_addition[0], initial_loc.col + coordinate_addition[1])


SAIL = [lambda game:
        game.set_sail(game.get_my_pirate(pirate_id),
                      _direction_to_location(game.get_my_pirate(pirate_id).initial_loc, direction))
        for direction in 'nswe-' for pirate_id in range(NUM_OF_PIRATES_IN_GROUP)]

SHOT = [lambda game: game.attack(game.get_my_pirate(pirate_id), game.get_enemy_pirate(enemy_id))
        for pirate_id in range(NUM_OF_PIRATES_IN_GROUP) for enemy_id in range(NUM_OF_PIRATES_IN_GROUP)]

DEFEND = [lambda game: game.defend(pirate_id) for pirate_id in range(NUM_OF_PIRATES_IN_GROUP)]

BERMUDA_SUMMON = [lambda game: game.summon_bermuda_zone(game.get_my_pirate(pirate_id))
                  for pirate_id in range(NUM_OF_PIRATES_IN_GROUP)]

actions = SAIL + SHOT + DEFEND + BERMUDA_SUMMON

SAIL_BASE_INDEX = 0


def get_sail_index(pirate_id, direction):
    return SAIL_BASE_INDEX + 'nswe-'.index(direction) + 4 * pirate_id


SHOT_BASE_INDEX = 20


def get_shot_index(pirate_id, enemy_id):
    return SHOT_BASE_INDEX + pirate_id + 4 * enemy_id


DEFEND_BASE_INDEX = 34


def get_defend_index(pirate_id):
    return DEFEND_BASE_INDEX + pirate_id


BERMUDA_SUMMON_BASE_INDEX = 38


def get_bermuda_zone_summon_index(pirate_id):
    return BERMUDA_SUMMON_BASE_INDEX + pirate_id


# ************************************************ Utils ************************************************


def get_matching_column(game):
    """
    Receive a game and returns the index of the column in the matrix, which 
    :param game: 
    :return:    The matrix's column's index which the i digit in its binary representation
                equal to truth value of the the i condition
    """
    status = 0
    for i in range(len(conditions)):
        if conditions[i](game):
            status += 2 ** i
    return status