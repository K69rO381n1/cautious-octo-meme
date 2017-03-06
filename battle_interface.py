import random
import os
import subprocess

# kit_path = u'C:\Ilia_proj\big8starter_kit\starter_kit' #do not erase, only commnet out!
# kit_path = u'D:\Users\J\Downloads\big8starter_kit\starter_kit'
kit_path = u''
try:
    with open('kit_path.txt', 'r') as f:
        kit_path = f.read()
except IOError:
    pass
if kit_path == u'':
    print 'No path found for kit, try to add path to file \'kit_path.txt\' in this directory'
    exit(0)


def maps():
    """
    returns list of all available maps
    """
    map_dir = os.path.join(kit_path, 'maps')
    ret = os.listdir(map_dir)
    return [f for f in ret if os.path.isfile(os.path.join(map_dir, f))]


def bots():
    """
    returns list of all available bots
    """
    bot_dir = os.path.join(kit_path, 'bots')
    ret = os.listdir(bot_dir)
    return [f for f in ret if os.path.isfile(os.path.join(bot_dir, f))]


def run(bot1_file, bot2_file, map=''):
    """
    runs game between two bots, file names are given
    map can be given or not, if not default map is used
    supports random map with parameter 'random'
    returns result (winner, scores)
    scores: (player1, player2)
    winner 1,2 or 0 for tie
    """
    if map == 'random':
        map = random.choice(maps())
    run_path = os.path.join(kit_path, 'run.bat')
    bots_dir = os.path.join(kit_path, 'bots')
    maps_dir = os.path.join(kit_path, 'maps')
    if not os.path.isabs(bot1_file):
        bot1_file = os.path.join(bots_dir, bot1_file)
    if not os.path.isabs(bot2_file):
        bot2_file = os.path.join(bots_dir, bot2_file)
    if not os.path.isabs(map) and not map == '':
        map = os.path.join(maps_dir, map)
    comm = [run_path, bot1_file, bot2_file]
    if map != '':
        comm.append(map)
    null_file = open(os.devnull, 'w')
    out = subprocess.check_output(comm, stderr=null_file)
    out = out.split('\n')
    i = -2
    if out[-1] != '':
        i += 1
    score_ln = out[i - 1]
    win_ln = out[i]
    scores = tuple(int(s) for s in score_ln.split(' ')[1:])
    winner = win_ln.split(' ')[1]
    if winner == 'finished':
        winner = 0
    else:
        winner = int(winner)
    return scores, winner


if __name__ == "__main__":
    import sys

    if '-b' in sys.argv:
        print '\n'.join(bots())
        sys.exit(0)
    if '-m' in sys.argv:
        print '\n'.join(maps())
        sys.exit(0)
    if len(sys.argv) not in (3, 4):
        print 'Usage: battle_interface.py <bot1> <bot2> [<map> or \'random\'] to run bot'
        print '       battle_interface.py -b                                to get all bots'
        print '       battle_interface.py -m                                to get all maps'
        sys.exit(0)
    scores, winner = run(*sys.argv[1:])
    print ' '.join([str(e) for e in scores])
    print winner
