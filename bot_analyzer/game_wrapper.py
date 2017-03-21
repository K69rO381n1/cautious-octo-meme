from pythonRunner import Pirates
from numpy import zeros

from param_matrix_protocol import *

DEFAULT_PARAM_DICT_FOLDER = u'\param_dictionaries\\'
PARAM_DICT_EXT = '.pd'


class GameWrapper(Pirates):
    class SavedDictionary(dict):
        def __del__(self):
            with open(DEFAULT_PARAM_DICT_FOLDER + GameWrapper.enemy_name + PARAM_DICT_EXT, 'r') as param_dict_file:
                from bot_analyzer.analyzer import param_dict2str
                param_dict_file.write(param_dict2str(GameWrapper.param_dict))
                param_dict_file.close()

    param_dict = SavedDictionary()
    enemy_name = None

    def __init__(self, game):
        assert isinstance(game, Pirates)
        Pirates.__init__(self)
        self.game = game
        self.situation = get_matching_column(game)
        self.actions_been_taken = []

        if GameWrapper.enemy_name is None:
            GameWrapper.enemy_name = game.get_opponent_name()

    def __del__(self):
        if GameWrapper.param_dict.has_key(self.situation):
            if GameWrapper.param_dict[self.situation].has_key(self.actions_been_taken):
                GameWrapper.param_dict[self.situation][self.actions_been_taken] += 1
            else:
                GameWrapper.param_dict[self.situation][self.actions_been_taken] = 1
        else:
            GameWrapper.param_dict[self.situation] = {self.actions_been_taken: 1}

    # ####################################################################


    def all_my_pirates(self):
        return self.game.all_my_pirates()

    def my_pirates(self):
        return self.game.my_pirates()

    def my_lost_pirates(self):
        return self.game.my_lost_pirates()

    def my_drunk_pirates(self):
        return self.game.my_drunk_pirates()

    def my_sober_pirates(self):
        return self.game.my_sober_pirates()

    def my_pirates_with_treasures(self):
        return self.game.my_pirates_with_treasures()

    def my_pirates_without_treasures(self):
        return self.game.my_pirates_without_treasures()

    def all_enemy_pirates(self):
        return self.game.all_enemy_pirates()

    def enemy_pirates(self):
        return self.game.enemy_pirates()

    def enemy_lost_pirates(self):
        return self.game.enemy_lost_pirates()

    def enemy_drunk_pirates(self):
        return self.game.enemy_drunk_pirates()

    def enemy_sober_pirates(self):
        return self.game.enemy_sober_pirates()

    def enemy_pirates_with_treasures(self):
        return self.game.enemy_pirates_with_treasures()

    def enemy_pirates_without_treasures(self):
        return self.game.enemy_pirates_without_treasures()

    def get_my_pirate(self, id):
        return self.game.get_my_pirate(id)

    def get_enemy_pirate(self, id):
        return self.game.get_enemy_pirate(id)

    def treasures(self):
        return self.game.treasures()

    def get_sail_options(self, pirate, destination, moves):
        return self.game.get_sail_options(pirate, destination, moves)

    def set_sail(self, pirate, destination):
        if pirate.location.col < destination.col:
            self.actions_been_taken.append(get_sail_index(pirate.id, 'e'))
        elif pirate.location.col > destination.col:
            self.actions_been_taken.append(get_sail_index(pirate.id, 'w'))

        if pirate.location.row < destination.row:
            self.actions_been_taken.append(get_sail_index(pirate.id, 'n'))
        elif pirate.location.row > destination.row:
            self.actions_been_taken.append(get_sail_index(pirate.id, 's'))

        if pirate.location.col == destination.col or pirate.location.row == destination.row:
            self.actions_been_taken.append(get_sail_index(pirate.id, '-'))

        self.game.set_sail(pirate, destination)

    def distance(self, loc1, loc2):
        return self.game.distance(loc1, loc2)

    def destination(self, obj, directions):
        return self.game.destination(obj, directions)

    def debug(self, *args):
        self.game.debug(args)

    def stop_point(self, message):
        self.game.stop_point(message)

    def get_turn(self):
        return self.game.get_turn()

    def attack(self, pirate, target):
        self.actions_been_taken.append(get_shot_index(pirate.id, target.id))
        return self.game.attack(pirate, target)

    def in_range(self, obj1, obj2):
        return self.game.in_range(obj1, obj2)

    def is_occupied(self, loc):
        return self.game.is_occupied(loc)

    def defend(self, pirate):
        self.actions_been_taken.append(get_defend_index(pirate.id))
        self.game.defend(pirate)

    def powerups(self):
        return self.game.powerups()

    def scripts(self):
        return self.game.scripts()

    def get_required_scripts_num(self):
        return self.game.get_required_scripts_num()

    def get_my_scripts_num(self):
        return self.game.get_my_scripts_num()

    def get_enemy_scripts_num(self):
        return self.game.get_enemy_scripts_num()

    def get_bermuda_zone_active_turns(self):
        return self.game.get_bermuda_zone_active_turns()

    def get_my_bermuda_zone(self):
        return self.game.get_my_bermuda_zone()

    def get_enemy_bermuda_zone(self):
        return self.game.get_enemy_bermuda_zone()

    def summon_bermuda_zone(self, pirate):
        self.actions_been_taken.append(get_bermuda_zone_summon_index(pirate.id))
        self.game.summon_bermuda_zone(pirate)

    def get_max_points(self):
        return self.game.get_max_points()

    def get_spawn_turns(self):
        return self.get_spawn_turns()

    def get_sober_turns(self):
        return self.game.get_sober_turns()

    def get_reload_turns(self):
        return self.get_reload_turns()

    def get_defense_expiration_turns(self):
        return self.game.get_defense_expiration_turns()

    def get_defense_reload_turns(self):
        return self.game.get_defense_reload_turns()

    def get_actions_per_turn(self):
        return self.game.get_actions_per_turn()

    def get_max_turns(self):
        return self.game.get_max_turns()

    def get_attack_radius(self):
        return self.game.get_attack_radius()

    def get_rows(self):
        return self.game.get_rows()

    def get_cols(self):
        return self.game.get_cols()

    def time_remaining(self):
        return self.game.time_remaining()

    def get_my_score(self):
        return self.game.get_my_score()

    def get_enemy_score(self):
        return self.game.get_enemy_score()

    def get_opponent_name(self):
        return self.game.get_opponent_name()
