from random import randint

from bot_analyzer.param_dict_protocol import get_matching_column, actions

# Keep this unfilled !!!
param_dict =


def choose_actions_set(game):
    """
    :param game: Game object, given by the game engine.
    :return: actions set which selected using weighted random, based on the game's current situation.
    """
    situation = get_matching_column(game)

    if not param_dict.has_key(situation):
        # TODO: complete undefined behavior
        return []

    possible_actions_sets = param_dict[situation].keys()
    likelihood = [param_dict[situation][actions_set] for actions_set in possible_actions_sets]

    total_sum = sum(likelihood)

    required_sum = randint(total_sum)
    current_action_index = 0
    current_sum = 0

    while current_sum < required_sum:
        current_sum += likelihood[current_action_index]
        current_action_index += 1

    return possible_actions_sets[current_action_index - 1]


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

    for action_id in choose_actions_set(game):
        actions[action_id](game)
