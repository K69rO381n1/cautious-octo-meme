from random import choice, randint

from param_matrix_protocol import get_matching_column, choose_action, actions

matrix = {}
def act(game, instructions):
    # currently receives [num(0-4),num(0-3),num(0-3)]*6
    directions = ['' for _ in game.all_my_pirates()]
    turn = instructions

    for i in xrange(len(turn)/3):
        inst = turn[3 * i: 3 * i + 3]
        if inst[0] == 1:
            directions[int(inst[1])] += 'nswe'[int(inst[2])]

        elif inst[0] == 2:
            ms = game.get_my_ship_by_id(int(inst[1]))
            es = game.get_enemy_ship_by_id(int(inst[2]))
            game.attack(ms, es)

        elif inst[0] == 3:
            ms = game.get_my_ship_by_id(int(inst[1]))
            game.defend(ms)

        elif inst[0] == 4:
            ms = game.get_my_ship_by_id(int(inst[1]))
            game.summon_bermuda_zone(ms)

    for ship in game.all_my_pirates():
        dest = game.destination(ship, directions[ship.id])
        game.set_sail(ship, dest)


def calculate(inp):
    mats = [
    ]
    return mats[0][inp]


def parse(game):
    return game.get_turn()


def is_valid_actions_list(actions_list):
    # TODO: !!
    return True


def choose_actions(game):
    situation = get_matching_column(game)

    if not matrix.has_key(situation):
        # TODO: complete undefined behavior
        return []

    keys = matrix[situation].keys()
    values = [matrix[situation][key] for key in keys]

    total_sum = sum(values)

    required_sum = randint(total_sum)
    current_action_index = 0
    current_sum = 0

    while current_sum < required_sum:
        current_sum += values[current_action_index]
        current_action_index += 1

    return keys[current_action_index - 1]


def do_turn(game):
    """
    New idea:
        Since most of the cases wont be examined during the bot's analytics,
        and since the order that the actions are been made is crucial;
        I think it would be better to save a Dictionary:
         The keys will be the so called column index (condition combinations)
         The value will be a Dictionary:
            The keys will be a list of actions that has been performed by the bot
            The values will be the number of encounters with this list of actions
    :param game: 
    :return: 
    """
    # act(game, calculate(parse(game)))

    for action_id in choose_actions(game):
        actions[action_id](game)
