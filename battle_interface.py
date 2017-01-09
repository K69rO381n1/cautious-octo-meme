import random
import os
import subprocess

kit_path = u'C:\Ilia_proj\big8starter_kit\starter_kit' #do not erase, only commnet out!

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
    if not os.path.isabs(map):
        map = os.path.join(maps_dir, map)
    out = subprocess.check_output([run_path,bot1_file,bot2_file, map])
    out = out.split('\n')
    score_ln = out[-3]
    win_ln = out[-2]
    scores = tuple(int(s) for s in score_ln.split(' ')[1:])
    winner = int(win_ln.split(' ')[1])
    return scores, winner