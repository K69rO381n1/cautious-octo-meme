import numpy as np
def act(game, instructions):
    # currently recieves [num(0-4),num(1-4),num(1-4)]*6 
    directions = [None] + ['' for ship in game.all_my_pirates()]
    for turn in instructions:
        for i in xrange(6):
            inst = turn[3 * i, 3 * i + 3]
            if inst[0] == 1:
                directions[inst[1]] += 'nswe'[inst[2] - 1]
            elif inst[0] == 2:
                ms = game.get_my_ship_by_id(inst[1])
                es = game.get_enemy_ship_by_id(inst[2])
                game.attack(ms, es)
            elif inst[0] == 3:
                ms = game.get_my_ship_by_id(inst[1])
                game.defend(ms)
            elif inst[0] == 4:
                ms = game.get_my_ship_by_id(inst[1])
                game.summon_bermuda_zone(ms)
    for ship in game.get_all_my_pirates():
        dest = game.destination(ship, directions[ship.id])
        game.set_sail(ship, dest)


def calculate(inp):
    mats = [
# content
    ]
    return mats[0][inp]


def parse(game):
    return game.get_turn()


def do_turn(game):
    act(game, calculate(parse(game)))