import random
import os
import subprocess

#kit_path = u'C:\Ilia_proj\big8starter_kit\starter_kit' #do not erase, only commnet out!
#kit_path = u'D:\Users\J\Downloads\big8starter_kit\starter_kit'
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
    map_dir = os.path.join(kit_path, 'maps')
    return os.listdir(map_dir)

def bots():
    bot_dir = os.path.join(kit_path, 'bots')
    return os.listdir(bot_dir)

def run(bot1_file, bot2_file, map = ''):
    if map == 'random':
        map = random.choice(maps())
    run_path = os.path.join(kit_path,'run.bat')
    bots_dir = os.path.join(kit_path, 'bots')
    maps_dir = os.path.join(kit_path, 'maps')
    if not os.path.isabs(bot1_file):
        bot1_file = os.path.join(bots_dir, bot1_file)
    if not os.path.isabs(bot2_file):
        bot2_file = os.path.join(bots_dir, bot2_file)
    if not os.path.isabs(map) and not map == '':
        map = os.path.join(maps_dir, map)
    comm = [run_path,bot1_file,bot2_file]
    if map != '':
        comm.append(map)
    out = subprocess.check_output(comm)
    out = out.split('\n')
    score_ln = out[-3]
    win_ln = out[-2]
    scores = tuple(int(s) for s in score_ln.split(' ')[1:])
    winner = int(win_ln.split(' ')[1])
    return scores, winner
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) not in (3,4):
        print 'Usage: battle_interface.py <bot1> <bot2> [<map> or \'random\']'
        sys.exit(0)
    scores,winner = run(*sys.argv[1:])
    print ' '.join([str(e) for e in scores])
    print winner