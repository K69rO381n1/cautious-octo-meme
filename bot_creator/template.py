import numpy as np
def act(game, instructions):
    # currently recieves [num(0-4),num(0-3),num(0-3)]*6 
    directions = ['' for ship in game.all_my_pirates()]
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
#content
    ]
    return mats[0][inp]


def parse(game):
    return game.get_turn()


def do_turn(game):
    act(game, calculate(parse(game)))